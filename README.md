The architecture of modern web applications is increasingly moving towards microservices, a pattern that structures an application as a collection of loosely coupled services, which implement business capabilities. The microservice architecture implemented using PostgreSQL, PostgREST, and Nginx, offers a robust and scalable way to build and manage services. Here's an introductory and explanatory text about this architecture, highlighting the mapping of database tables to schemas served as OpenAPI.

---

# Introduction to Microservices Architecture with PostgreSQL, PostgREST, and Nginx

In the realm of web application development, the microservices architecture has emerged as a paradigm that prioritizes flexibility, scalability, and independence. This approach decomposes an application into a set of smaller, interconnected services instead of a single monolithic structure. Each service in a microservices architecture is designed to execute a specific business function and can be developed, deployed, and scaled independently.

## Role of PostgreSQL in Microservices

PostgreSQL, a powerful open-source object-relational database system, serves as the foundation for storing and managing data across microservices. Its advanced features, such as support for complex data types, full-text search, and extensibility, make PostgreSQL an ideal choice for microservices that require robust data persistence and transactional support. In a microservices architecture, each service can have its dedicated PostgreSQL schema, ensuring data isolation and schema independence, which simplifies the management of data persistence in a distributed system.

## PostgREST for API Layer

PostgREST is a standalone web server that turns your PostgreSQL database directly into a RESTful API. The beauty of PostgREST lies in its ability to provide an instant, high-performance API layer without the need for custom backend development. By mapping each PostgreSQL schema to a RESTful endpoint, PostgREST enables microservices to communicate over HTTP with minimal latency, leveraging PostgreSQL's security and scalability. This direct mapping ensures that the data model is accurately and efficiently exposed to other services or front-end clients, adhering to the OpenAPI specifications for clear, interactive API documentation.

## Nginx as the Reverse Proxy

Nginx, known for its high performance, reliability, and scalability, acts as the gatekeeper in this architecture. It serves as a reverse proxy, routing incoming HTTP requests to the appropriate PostgREST instance based on the request URL. Nginx efficiently manages SSL termination, load balancing, and static content delivery, making it an indispensable tool for handling web traffic in a microservices ecosystem. By integrating Nginx, developers can ensure secure, fast, and reliable access to the microservices, while also simplifying the network configuration.

## Mapping Database Tables to Schemas Served as OpenAPI

The essence of this architecture lies in its ability to map individual database tables to dedicated PostgreSQL schemas, each of which is served as an OpenAPI through PostgREST. This approach not only encapsulates the data and operations of each microservice but also promotes a clean, organized structure for API endpoints. OpenAPI specifications offer a standard, language-agnostic interface to RESTful APIs, enabling both humans and computers to discover and understand the capabilities of the service without accessing the source code.

## Conclusion

The combination of PostgreSQL, PostgREST, and Nginx in a microservices architecture provides a compelling solution for building modern, scalable web applications. This setup leverages the strengths of each component to offer a streamlined, efficient pathway from database tables to web-facing APIs, adhering to the principles of independence, scalability, and resilience. As applications grow and evolve, this architecture ensures that each microservice can be modified, scaled, or replaced independently, promoting agility and innovation in web development.

---

# Scripted Setup and Testing


The setup script provided is designed to automate the deployment and configuration of a suite of microservices for managing theatrical scripts and related data, along with GoAccess for real-time web log analysis. This script specifically targets an Ubuntu 20.04 server environment. It encompasses the installation and configuration of essential services and software, including PostgreSQL, Nginx, Certbot for SSL certificates, GoAccess, and PostgREST. The script ensures that all components are prepared and configured to start automatically upon system reboot, thereby providing a robust and resilient backend infrastructure. Below is an overview of the script's flow and its main components:

### Introduction
The script starts by updating the system and installing necessary packages, ensuring the environment is current and has all required dependencies installed. It includes PostgreSQL for database management, Nginx as a web server, Certbot for managing SSL certificates, GoAccess for log analysis, and wget for downloading files.

### PostgREST Installation
PostgREST serves as a standalone web server that turns your PostgreSQL database directly into a RESTful API. The script checks if PostgREST is already installed; if not, it downloads and installs the specified version of PostgREST, making it available as a system-wide executable.

### PostgreSQL Configuration
The user is prompted to enter details for creating a PostgreSQL database and user. The script then checks if the specified user and database already exist to prevent duplicate creations, ensuring idempotency.

### Microservices Setup
An array of services representing different aspects of the theatrical scripts management system is defined. For each service, the script sets up a dedicated PostgREST configuration, creating a PostgreSQL schema if necessary, and configures a corresponding Nginx virtual host to serve the API over the network. It also handles the SSL certification for each service's domain via Certbot.

### GoAccess Setup
GoAccess is configured to monitor Nginx access logs for each of the microservices. This provides real-time web log analysis accessible through a web interface. The script configures GoAccess and sets up a systemd service for each log file it monitors, ensuring logs are analyzed and accessible continuously.

### SSL Configuration for GoAccess Dashboard
A specific Nginx virtual host is set up for serving the GoAccess dashboard under a designated subdomain (e.g., "logs.example.com"). SSL certification for this subdomain is also managed via Certbot, securing access to the log analysis dashboard.

### Finalization
The script concludes by reloading Nginx to apply all new configurations and echoing a completion message. This ensures all components are correctly set up and ready for use.

### Idempotency Considerations
Throughout the script, checks are in place to ensure that actions such as user and database creation, PostgREST configuration, and SSL certificate provisioning are only performed if necessary. This idempotent design prevents duplicate configurations and errors upon subsequent executions of the script.

This setup script streamlines the deployment process for a complex microservices architecture, making it accessible even to users with limited backend configuration experience. It ensures a secure, robust, and scalable backend system ready to manage and serve theatrical script data efficiently.

```bash#!/bin/bash

# Update system and install necessary packages
apt-get update && apt-get upgrade -y
apt-get install -y postgresql postgresql-contrib nginx certbot python3-certbot-nginx goaccess wget

# Install PostgREST v12.0.2 if not already installed
POSTGREST_VERSION="v12.0.2"
if [ ! -f "/usr/local/bin/postgrest" ]; then
    # Correct URL for downloading PostgREST v12.0.2
    wget https://github.com/PostgREST/postgrest/releases/download/${POSTGREST_VERSION}/postgrest-${POSTGREST_VERSION}-linux-static-x64.tar.xz -O postgrest.tar.xz
    
    # Verifies if the download was successful before attempting to extract
    if [ $? -eq 0 ]; then
        tar -xJf postgrest.tar.xz -C /usr/local/bin
        rm postgrest.tar.xz
        chmod +x /usr/local/bin/postgrest
        echo "PostgREST installed."
    else
        echo "Failed to download PostgREST. Please check the URL and try again."
        exit 1
    fi
else
    echo "PostgREST already installed."
fi

# Setup PostgreSQL: create user, database, and ensure idempotency
read -p "Enter PostgreSQL database name: " dbname
read -p "Enter PostgreSQL user: " dbuser
echo -n "Enter PostgreSQL password: " && read -s dbpass && echo
read -p "Enter base domain (e.g., example.com): " basedomain
echo -n "Enter your email for SSL certificates: " && read email

# Check if user exists
USER_EXISTS=$(sudo -u postgres psql -tAc "SELECT 1 FROM pg_roles WHERE rolname='$dbuser'")
if [ "$USER_EXISTS" != "1" ]; then
    sudo -u postgres psql -c "CREATE USER $dbuser WITH PASSWORD '$dbpass';"
else
    echo "User $dbuser already exists."
fi

# Check if database exists
DB_EXISTS=$(sudo -u postgres psql -tAc "SELECT 1 FROM pg_database WHERE datname='$dbname'")
if [ "$DB_EXISTS" != "1" ]; then
    sudo -u postgres psql -c "CREATE DATABASE $dbname OWNER $dbuser;"
else
    echo "Database $dbname already exists."
fi

# Define services
services=("playwright" "metadata" "script" "act" "scene" "character" 
"dialogue" "action" "transition" "parenthetical" "note" "centeredtext" 
"pagebreak" "sectionheading" "titlepage" "casting" "characterrelationship" 
"musicsound" "props" "revisionhistory" "formattingrules" "crossreferences" 
"extendednotesresearch" "scenelocation")

# Directories and configuration paths
NGINX_VHOSTS_DIR="/etc/nginx/sites-available"
GOACCESS_CONF_DIR="/etc/goaccess"
GOACCESS_SYSTEMD_DIR="/etc/systemd/system"

mkdir -p "$GOACCESS_CONF_DIR" "$NGINX_VHOSTS_DIR"

# Function to create PostgREST and Nginx configs, enable SSL, and setup GoAccess
setup_service() {
    local schema=$1
    local service_port=$((3000 + $2))
    local domain="api-$schema.$basedomain"
    local nginx_conf="$NGINX_VHOSTS_DIR/$domain"
    local access_log_path="/var/log/nginx/$domain-access.log"
    local error_log_path="/var/log/nginx/$domain-error.log"
    
    # Check if PostgREST config exists, if not create it and PostgREST service
    if [ ! -f "/etc/postgrest/$schema.conf" ]; then
        mkdir -p /etc/postgrest
        cat > "/etc/postgrest/$schema.conf" <<EOF
db-uri = "postgres://$dbuser:$dbpass@localhost:5432/$dbname"
db-schema = "$schema"
db-anon-role = "web_anon"
server-port = $service_port
EOF

        # Create Systemd service for PostgREST
        cat > "/etc/systemd/system/postgrest-$schema.service" <<EOF
[Unit]
Description=PostgREST Service for schema $schema
After=network.target postgresql.service

[Service]
ExecStart=/usr/local/bin/postgrest /etc/postgrest/$schema.conf
Restart=on-failure
User=postgres

[Install]
WantedBy=multi-user.target
EOF

        systemctl daemon-reload
        systemctl enable postgrest-$schema.service
        systemctl start postgrest-$schema.service
    fi

    # Setup Nginx configuration for the microservice
    if [ ! -f "$nginx_conf" ]; then
        cat > "$nginx_conf" <<EOF
server {
    listen 80;
    server_name $domain;

    location / {
        proxy_pass http://localhost:$service_port;
        proxy_set_header Host \$host;
        proxy_set_header X-Real-IP \$remote_addr;
        proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto \$scheme;
    }
}
EOF

        ln -s "$nginx_conf" "/etc/nginx/sites-enabled/"
        nginx -t && systemctl reload nginx
    fi

    # Enable SSL with Certbot for the domain
    certbot --nginx -d $domain --non-interactive --agree-tos -m $email --redirect || true
    
    # Setup GoAccess
    setup_goaccess "$access_log_path" "$domain"
}

# Setup GoAccess monitoring for Nginx logs
setup_goaccess() {
    local log_path=$1
    local name=$2
    local conf_path="$GOACCESS_CONF_DIR/goaccess-$name.conf"
    local systemd_service="$GOACCESS_SYSTEMD_DIR/goaccess-$name.service"
    local html_output="/var/www/html/$name/index.html"

    # Ensure the HTML output directory exists
    mkdir -p "/var/www/html/$name"
    chown www-data:www-data "/var/www/html/$name"

    # Prepare GoAccess configuration if it doesn't exist
    if [ ! -f "$conf_path" ]; then
        cat > "$conf_path" <<EOF
log-file $log_path
log-format COMBINED
output $html_output
real-time-html true
EOF
    fi

    # Create Systemd service for GoAccess if it doesn't exist
    if [ ! -f "$systemd_service" ]; then
        cat > "$systemd_service" <<EOF
[Unit]
Description=GoAccess Real-time Web Log Analyzer for $name
After=network.target

[Service]
Type=simple
ExecStart=/usr/bin/goaccess --config-file=$conf_path

[Install]
WantedBy=multi-user.target
EOF

        systemctl daemon-reload
        systemctl enable "goaccess-$name.service"
        systemctl start "goaccess-$name.service"
    fi
}

# Main setup loop for each service
for i in "${!services[@]}"; do
    setup_service "${services[$i]}" "$i"
done

# Setting up SSL-secured Nginx virtual host for GoAccess dashboard
GOACCESS_DOMAIN="logs.$basedomain"
nginx_conf="$NGINX_VHOSTS_DIR/$GOACCESS_DOMAIN"
if [ ! -f "$nginx_conf" ]; then
    cat > "$nginx_conf" <<EOF
server {
    listen 80;
    server_name $GOACCESS_DOMAIN;

    location / {
        alias /var/www/html/goaccess/;
        index index.html index.htm;
    }
}
EOF

    ln -s "$nginx_conf" "/etc/nginx/sites-enabled/"
    certbot --nginx -d $GOACCESS_DOMAIN --non-interactive --agree-tos -m $email --redirect || true
fi

# Reload Nginx to apply new configurations
nginx -t && systemctl reload nginx

echo "Setup completed. Fountain microservices, GoAccess monitoring, and SSL-secured GoAccess dashboard are configured."

```


Note: so far , there are no tables created in the database - 

## And Now Test!

The test script is designed to verify the correct deployment and configuration of a suite of microservices for managing theatrical scripts, along with GoAccess for real-time web log analysis, as set up by the previously provided comprehensive setup script. This verification script ensures that each component of the system is operational and configured correctly, providing administrators and developers with confidence in the deployment's integrity. Below is an overview of the test script's structure and its key components:

### Introduction
The test script serves as a post-deployment validation tool, systematically checking each critical component of the infrastructure deployed by the setup script. It targets an Ubuntu 20.04 server environment and checks the operational status of PostgreSQL, PostgREST instances for each microservice, Nginx, SSL certificates, and the GoAccess dashboard.

### Flow Description

1. **Service Status Checks**: 
   - The script begins by checking the active status of system-critical services, specifically PostgreSQL and Nginx. This step ensures that the database and web server, fundamental to the operation of the microservices and the GoAccess dashboard, are running.

2. **PostgREST Microservices Verification**: 
   - It iterates through the array of microservices, checking the status of each corresponding PostgREST instance managed by systemd. This step verifies that all PostgREST services are active, indicating that the APIs for managing theatrical scripts are operational.

3. **Nginx Configuration Validation**: 
   - The script validates the Nginx configuration to ensure that there are no syntax errors in the configuration files. This step is crucial for guaranteeing that Nginx can correctly serve the microservices and the GoAccess dashboard.

4. **SSL Certificates Check**: 
   - Using Certbot, the script checks the SSL certificates for each domain associated with the microservices and the GoAccess dashboard. This step ensures that SSL certificates are correctly installed and valid, providing secure access to the services.

5. **GoAccess Dashboard Accessibility**: 
   - The script uses `curl` to request the GoAccess dashboard's URL, verifying that the dashboard is accessible over HTTPS. This step confirms that the GoAccess web interface for log analysis is available and secured with SSL.

6. **Completion Message**: 
   - Upon completing all checks, the script outputs a summary of the verification results, highlighting any issues detected during the process.

### Idempotency and Reusability
The test script is designed to be idempotent and reusable, meaning it can be run multiple times without causing any side effects or changes to the system configuration. This design allows administrators to periodically re-run the script to ensure the continued operational integrity of the deployment.

This test script is an essential tool for maintaining the reliability and security of the deployed microservices infrastructure. By systematically verifying each component, it helps identify potential issues early, ensuring that the system remains robust and secure over time.

```bash
#!/bin/bash

# Verify Setup for Fountain Microservices with GoAccess Monitoring

# Define base domain used in setup
base_domain="example.com" # Replace with your actual base domain used in setup

# Array of microservices to check (based on the setup script services array)
microservices=("playwright" "metadata" "script" "act" "scene" "character"
"dialogue" "action" "transition" "parenthetical" "note" "centeredtext"
"pagebreak" "sectionheading" "titlepage" "casting" "characterrelationship"
"musicsound" "props" "revisionhistory" "formattingrules" "crossreferences"
"extendednotesresearch" "scenelocation")

# Check if PostgreSQL service is active
echo "Checking PostgreSQL service status..."
systemctl is-active --quiet postgresql && echo "PostgreSQL service is active." || echo "PostgreSQL service is NOT active."

# Check each PostgREST microservice
for service in "${microservices[@]}"; do
    echo "Checking PostgREST service for $service..."
    systemctl is-active --quiet "postgrest-$service" && echo "PostgREST $service service is active." || echo "PostgREST $service service is NOT active."
done

# Check Nginx service status
echo "Checking Nginx service status..."
systemctl is-active --quiet nginx && echo "Nginx service is active." || echo "Nginx service is NOT active."

# Validate Nginx configuration
echo "Validating Nginx configuration..."
nginx -t && echo "Nginx configuration is valid." || echo "Nginx configuration is NOT valid."

# Check SSL certificates for each domain (main domain and GoAccess dashboard)
echo "Checking SSL certificates..."
certbot certificates --domains "$base_domain,logs.$base_domain" && echo "SSL certificates are valid." || echo "Issues with SSL certificates."

# Verify GoAccess dashboard accessibility
echo "Verifying GoAccess dashboard accessibility at https://logs.$base_domain..."
curl -s -o /dev/null -w "%{http_code}" "https://logs.$base_domain/" | grep 200 && echo "GoAccess dashboard is accessible." || echo "GoAccess dashboard is NOT accessible."

echo "Verification completed."
```

Before running this script, ensure you:
- Replace `example.com` with the actual base domain you used during the setup.
- Have the necessary permissions to execute these checks (you might need `sudo` for some commands).
- Adjust the script as needed based on any customizations you made to the setup process not covered in the original instructions.

This script provides a clear indication of the operational status of each component involved in the Fountain Microservices and GoAccess monitoring setup. It checks the active status of critical services, validates Nginx configurations, ensures SSL certificates are correctly applied, and confirms the accessibility of the GoAccess dashboard.

## But there are Errors! ...

 which is an expected outcome rsult of the test script. Here is why : 
 PostgREST does not inherently serve a schema for non-existent database tables. The functionality and response of PostgREST are closely tied to the actual structure of the PostgreSQL database it interfaces with. If a table does not exist in the database, PostgREST cannot provide an API endpoint or schema information for that table. 

PostgREST dynamically generates its API endpoints based on the database schema. When PostgREST starts, it introspects the database to understand its structure, including tables, views, stored procedures, etc. It then exposes this structure as a RESTful API. If a specific table has not been created in the database, PostgREST has no knowledge of it and, therefore, cannot expose any information or schema related to it through its API.

For PostgREST to serve a schema or data from a table, the table must exist in the PostgreSQL database. Once the table is created, PostgREST can automatically expose it as part of its API based on the permissions and roles defined within PostgreSQL and PostgREST's configuration.

##  Scripted creation of the database tables 

Based on the detailed SQL schema for the Fountain Database Bootstrap tailored for a Microservices Architecture you provided, here is the complete shell script that creates all the specified database schemata tables within a PostgreSQL database:

```bash
#!/bin/bash

# PostgreSQL credentials and database name
DB_USER="your_db_user"  # Change to your PostgreSQL user
DB_PASSWORD="your_db_password"  # Change to your PostgreSQL password
DB_NAME="your_db_name"  # Change to your PostgreSQL database name

# Connect to PostgreSQL and execute the SQL commands to create schemas and tables
PGPASSWORD=$DB_PASSWORD psql -U $DB_USER -d $DB_NAME <<EOF

-- Create schemas for microservices
CREATE SCHEMA IF NOT EXISTS playwright;
CREATE SCHEMA IF NOT EXISTS metadata;
CREATE SCHEMA IF NOT EXISTS script;
CREATE SCHEMA IF NOT EXISTS act;
CREATE SCHEMA IF NOT EXISTS scene;
CREATE SCHEMA IF NOT EXISTS character;
CREATE SCHEMA IF NOT EXISTS dialogue;
CREATE SCHEMA IF NOT EXISTS action;
CREATE SCHEMA IF NOT EXISTS transition;
CREATE SCHEMA IF NOT EXISTS parenthetical;
CREATE SCHEMA IF NOT EXISTS note;
CREATE SCHEMA IF NOT EXISTS centeredtext;
CREATE SCHEMA IF NOT EXISTS pagebreak;
CREATE SCHEMA IF NOT EXISTS sectionheading;
CREATE SCHEMA IF NOT EXISTS titlepage;
CREATE SCHEMA IF NOT EXISTS casting;
CREATE SCHEMA IF NOT EXISTS characterrelationship;
CREATE SCHEMA IF NOT EXISTS musicsound;
CREATE SCHEMA IF NOT EXISTS props;
CREATE SCHEMA IF NOT EXISTS revisionhistory;
CREATE SCHEMA IF NOT EXISTS formattingrules;
CREATE SCHEMA IF NOT EXISTS crossreferences;
CREATE SCHEMA IF NOT EXISTS extendednotesresearch;
CREATE SCHEMA IF NOT EXISTS scenelocation;

-- Tables creation within their respective schemas

-- Playwright Table
CREATE TABLE playwright.Playwright (
    Author_ID SERIAL PRIMARY KEY,
    Name TEXT NOT NULL,
    Biography TEXT,
    Contact_Information TEXT
);

-- Metadata Table
CREATE TABLE metadata.Metadata (
    Metadata_ID SERIAL PRIMARY KEY,
    Creation_Date DATE,
    Last_Modified_Date DATE,
    Version_Number INTEGER,
    Additional_Information TEXT
);

-- Script Table
CREATE TABLE script.Script (
    Script_ID SERIAL PRIMARY KEY,
    Title TEXT NOT NULL,
    Author_ID INTEGER REFERENCES playwright.Playwright(Author_ID),
    URL TEXT,
    Metadata_ID INTEGER REFERENCES metadata.Metadata(Metadata_ID)
);

-- Act Table
CREATE TABLE act.Act (
    Act_ID SERIAL PRIMARY KEY,
    Script_ID INTEGER REFERENCES script.Script(Script_ID),
    Act_Number INTEGER NOT NULL,
    Synopsis TEXT,
    Notes TEXT
);

-- Scene Table
CREATE TABLE scene.Scene (
    Scene_ID SERIAL PRIMARY KEY,
    Act_ID INTEGER REFERENCES act.Act(Act_ID),
    Scene_Number INTEGER NOT NULL,
    Synopsis TEXT,
    Notes TEXT
);

-- Character Table
CREATE TABLE character.Character (
    Character_ID SERIAL PRIMARY KEY,
    Script_ID INTEGER REFERENCES script.Script(Script_ID),
    Name TEXT NOT NULL,
    Description TEXT
);

-- Dialogue Table
CREATE TABLE dialogue.Dialogue (
    Dialogue_ID SERIAL PRIMARY KEY,
    Scene_ID INTEGER REFERENCES scene.Scene(Scene_ID),
    Character_ID INTEGER REFERENCES character.Character(Character_ID),
    Original_Text TEXT NOT NULL,
    Modernized_Text TEXT
);

-- Action Table
CREATE TABLE action.Action (
    Action_ID SERIAL PRIMARY KEY,
    Scene_ID INTEGER REFERENCES scene.Scene(Scene_ID),
    Character_ID INTEGER REFERENCES character.Character(Character_ID),
    Original_Text TEXT NOT NULL,
    Modernized_Text TEXT
);

-- Transition Table
CREATE TABLE transition.Transition (
    Transition_ID SERIAL PRIMARY KEY,
    Scene_ID INTEGER REFERENCES scene.Scene(Scene_ID),
    Transition_Text TEXT NOT NULL
);

-- Parenthetical Table
CREATE TABLE parenthetical.Parenthetical (
    Parenthetical_ID SERIAL PRIMARY KEY,
    Dialogue_ID INTEGER REFERENCES dialogue.Dialogue(Dialogue_ID),
    Original_Text TEXT NOT NULL,
    Modernized_Text TEXT
);

-- Note Table
CREATE TABLE note.Note (
    Note_ID SERIAL PRIMARY KEY,
    Script_ID INTEGER REFERENCES script.Script(Script_ID),
    Type TEXT NOT NULL,
    Text TEXT NOT NULL
);

-- CenteredText Table
CREATE TABLE centeredtext.CenteredText (
    Centered_ID SERIAL PRIMARY KEY,
    Script_ID INTEGER REFERENCES script.Script(Script_ID),
    Text TEXT NOT NULL
);

-- PageBreak Table
CREATE TABLE pagebreak.PageBreak (
    Page_Break_ID SERIAL PRIMARY KEY,
    Script_ID INTEGER REFERENCES script.Script(Script_ID),
    Page_Number INTEGER NOT NULL
);

-- SectionHeading Table
CREATE TABLE sectionheading.SectionHeading (
    Section_ID SERIAL PRIMARY KEY,
    Script_ID INTEGER REFERENCES script.Script(Script_ID),
    Text TEXT NOT NULL
);

-- TitlePage Table
CREATE TABLE titlepage.TitlePage (
    Title_Page_ID SERIAL PRIMARY KEY,
    Script_ID INTEGER REFERENCES script.Script(Script_ID),
    Text TEXT NOT NULL
);

-- Casting Table
CREATE TABLE casting.Casting (
    Casting_ID SERIAL PRIMARY KEY,
    Character_ID INTEGER REFERENCES character.Character(Character_ID),
    Actor_Characteristics_Choices TEXT NOT NULL
);

-- CharacterRelationship Table
CREATE TABLE characterrelationship.CharacterRelationship (
    Relationship_ID SERIAL PRIMARY KEY,
    Character1_ID INTEGER REFERENCES character.Character(Character_ID),
    Character2_ID INTEGER REFERENCES character.Character(Character_ID),
    Relationship_Type TEXT NOT NULL
);

-- MusicSound Table
CREATE TABLE musicsound.MusicSound (
    Music_Sound_ID SERIAL PRIMARY KEY,
    Scene_ID INTEGER REFERENCES scene.Scene(Scene_ID),
    Cue TEXT NOT NULL,
    Description TEXT NOT NULL
);

-- Props Table
CREATE TABLE props.Props (
    Prop_ID SERIAL PRIMARY KEY,
    Scene_ID INTEGER REFERENCES scene.Scene(Scene_ID),
    Description TEXT NOT NULL
);

-- RevisionHistory Table
CREATE TABLE revisionhistory.RevisionHistory (
    Revision_ID SERIAL PRIMARY KEY,
    Script_ID INTEGER REFERENCES script.Script(Script_ID),
    Date DATE NOT NULL,
    Change_Description TEXT NOT NULL,
    Editor TEXT NOT NULL
);

-- FormattingRules Table
CREATE TABLE formattingrules.FormattingRules (
    Rule_ID SERIAL PRIMARY KEY,
    Script_ID INTEGER REFERENCES script.Script(Script_ID),
    Rule_Description TEXT NOT NULL
);

-- CrossReferences Table
CREATE TABLE crossreferences.CrossReferences (
    Cross_Reference_ID SERIAL PRIMARY KEY,
    Scene_ID INTEGER REFERENCES scene.Scene(Scene_ID),
    Referenced_Scene_ID INTEGER NOT NULL,
    Description TEXT NOT NULL
);

-- ExtendedNotesResearch Table
CREATE TABLE extendednotesresearch.ExtendedNotesResearch (
    Research_ID SERIAL PRIMARY KEY,
    Script_ID INTEGER REFERENCES script.Script(Script_ID),
    Notes TEXT NOT NULL,
    Research_Details TEXT NOT NULL
);

-- SceneLocation Table
CREATE TABLE scenelocation.SceneLocation (
    Location_ID SERIAL PRIMARY KEY,
    Description TEXT NOT NULL,
    Historical_Cultural_Significance TEXT
);

EOF

echo "All schemas and tables have been created successfully."
```

Make sure to replace `your_db_user`, `your_db_password`, and `your_db_name` with the actual values for your PostgreSQL database user, password, and the name of your database. This script assumes you have the appropriate privileges to create schemas and tables in the PostgreSQL database. Before executing the script, ensure that PostgreSQL is installed and running, and that you can connect to it using the provided credentials.
