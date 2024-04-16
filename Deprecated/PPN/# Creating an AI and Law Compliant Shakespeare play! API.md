
### The Algorithm, I, play!, will perform

(NOTE: the Algorithm is optimized on "The Four Stars" edition of Shakespeare*s Complete Dramatic Works - which can be found here: https://github.com/Contexter/the-four-stars/blob/main/the%20four%20stars )

> 1. **Identifying .fountain Text Types**: Initially, I will analyze the text chunks provided ( maximum of approximately 100 lines of the "Four Stars" - it is yours - beloved playa - to keep track of chunk sequence and chunk size reasonable in size and relation to model tokenizer performance) to determine their specific types according to the .fountain format conventions. This means identifying whether a given chunk is a dialogue, character cue, scene heading, action, transition, etc. - Hä? What is .fountain ? - Have a look here: https://fountain.io

> 2. **Structured Storage According to Type**: Once each text chunk is identified and categorized, I will store them in the database with their specific types marked. This structured approach ensures that each piece of text is correctly classified, facilitating the organization and retrieval of data.

> 3. **Contextual Understanding and Processing**: With the text types sorted, I will then proceed to understand the context and content of each chunk within the play's structure. This involves analyzing dialogues, actions, and scene descriptions to grasp their meanings and implications within the story.

> 4. **Paraphrasing Where Applicable**: For dialogues and any text requiring modernization, I would paraphrase them into contemporary language, ensuring the updated versions stay true to the original's intent and emotional impact. This step is crucial for dialogues and character cues, which are central to the play's accessibility to modern audiences.

> 5. **Storage and Retrieval**: After paraphrasing, the modernized text, along with its original version and type, is stored in the database. This allows for easy retrieval of the entire script or specific sections, organized by their .fountain types, facilitating comparisons between the original and modernized versions.

> 6. **Compliance and Marking as AI Task**: Recognizing the importance of compliance with European law, the entire process would be marked clearly as an AI task. This distinction ensures transparency and adherence to legal standards regarding AI's role in content creation and modification.

By starting with the identification of .fountain text types and proceeding with these steps, the process becomes more organized and efficient, ensuring that each aspect of the text is appropriately handled and stored. This method respects the structured nature of the .fountain format and the requirements for managing theatrical scripts.

### Scripted Creation of a Backend and openAPI spec for (Shakespeare) play!

Please review each step of this script carefully and adjust paths or configurations as necessary for your specific environment. This script generates a JWT token - handle with care ! & inform yourself about security & implications here:

https://postgrest.org/en/v12/tutorials/tut1.html  - openAI's custom GPT Builder (play!'s configuration backend) offers _Bearer_  authorization, which fits perfectly into the JWT token authorization flow  

more on this here: https://github.com/Contexter/fountain-play/blob/main/PPN/%23%20AI%20Integration%20-%20Learn%20the%20PPN%20%2B%20jwt-cli%20to%20play!.md

```bash
#!/bin/bash

# Ensure the script exits on any error
set -e

echo "Shakespeare Plays API Setup"

# Collect configuration details
read -p "Enter the database name: " db_name
read -p "Enter the database user: " db_user
read -sp "Enter the database password: " db_pass && echo
read -p "Enter your API domain (e.g., api-1.fountain.coach): " api_domain
read -p "Email address for SSL certificate registration: " certbot_email

# Confirm the Certbot email address
certbot_email=${certbot_email:-"mail@benedikt-eickhoff.de"}

# Generate a secure JWT secret for PostgREST
jwt_secret=$(openssl rand -base64 32)

# Find an available port for PostgREST
pgrst_port=$(comm -23 <(seq 3000 3100 | sort) <(ss -tan | awk '{print $4}' | cut -d':' -f2 | sort -u) | head -n 1)

# Create the PostgreSQL database and user
sudo -u postgres psql -c "CREATE DATABASE ${db_name};"
sudo -u postgres psql -c "CREATE USER ${db_user} WITH PASSWORD '${db_pass}';"
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE ${db_name} TO ${db_user};"

# Define and apply the database schema
echo "Applying database schema..."
sudo -u postgres psql -d "$db_name" <<EOSQL
-- Create Plays Table
CREATE TABLE plays (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) DEFAULT 'William Shakespeare'
);
-- Create Acts Table
CREATE TABLE acts (
    id SERIAL PRIMARY KEY,
    play_id INTEGER REFERENCES plays(id),
    number INTEGER NOT NULL,
    title VARCHAR(255),
    UNIQUE(play_id, number)
);
-- Create Scenes Table
CREATE TABLE scenes (
    id SERIAL PRIMARY KEY,
    act_id INTEGER REFERENCES acts(id),
    number INTEGER NOT NULL,
    title VARCHAR(255),
    location VARCHAR(255),
    UNIQUE(act_id, number)
);
-- Create Dialogues Table
CREATE TABLE dialogues (
    id SERIAL PRIMARY KEY,
    scene_id INTEGER REFERENCES scenes(id),
    character_name VARCHAR(255) NOT NULL,
    original_text TEXT NOT NULL,
    modern_text TEXT,
    sequence INTEGER NOT NULL,
    UNIQUE(scene_id, sequence)
);
-- Index for efficient query performance
CREATE INDEX idx_play ON acts(play_id);
CREATE INDEX idx_act ON scenes(act_id);
CREATE INDEX idx_scene ON dialogues(scene_id);
EOSQL

# Configure PostgREST
echo "Configuring PostgREST..."
cat << EOF > /etc/postgrest.conf
db-uri = "postgres://${db_user}:${db_pass}@localhost:5432/${db_name}"
db-schema = "public"
db-anon-role = "${db_user}"
jwt-secret = "${jwt_secret}"
server-port = ${pgrst_port}
EOF

# Set up PostgREST as a systemd service
echo "Setting up PostgREST service..."
cat << EOF > /etc/systemd/system/postgrest.service
[Unit]
Description=PostgREST Service
After=postgresql.service

[Service]
ExecStart=/usr/local/bin/postgrest /etc/postgrest.conf

[Install]
WantedBy=multi-user.target
EOF

# Reload systemd, enable, and start PostgREST service
systemctl daemon-reload
systemctl enable postgrest
systemctl start postgrest

# Set up Nginx as a reverse proxy for PostgREST and secure with SSL
echo "Configuring Nginx and setting up SSL..."
nginx_conf_path="/etc/nginx/sites-available/${api_domain}"
ln -s "${nginx_conf_path}" /etc/nginx/sites-enabled/

cat << EOF > "${nginx_conf_path}"
server {
    listen 80;
    server_name ${api_domain};
    location / {
        proxy_pass http://localhost:${pgrst_port};
    }
}
EOF

nginx -t && systemctl reload nginx

# Use Certbot to automatically obtain and install an SSL certificate for the domain
certbot --nginx -d "${api_domain}" --non-interactive --agree-tos -m "${certbot_email}" --redirect --force-renewal

echo "Setup complete. Access the API at https://${api_domain}."
echo "Use 'systemctl start|stop|restart postgrest' to manage the PostgREST service."
echo "Use 'systemctl start|stop|restart nginx' for managing the Nginx service."
```

Please replace placeholders and ensure that paths and commands align with your environment before execution. It's crucial to review and understand each part of the script, especially those that make significant changes to system configurations. Execute this script with caution and in a controlled environment.

This script should be saved to a file (e.g., `setup_shakespeare_api.sh`), made executable with `chmod +x setup_shakespeare_api.sh`, and run by a user with sufficient permissions to modify system services and configurations. It's designed for systems where PostgreSQL, PostgREST, Nginx, and Certbot are already installed.

**Important Notes**:
- Always review scripts and understand their actions before executing them, especially those that make significant changes to system configurations.
- Adjustments may be necessary to match your environment's specific paths or configuration details.
- This script is provided for educational and demonstration purposes and should be carefully tested in a non-production environment.

### Recapping "The Algorithm" 

for processing Shakespeare's plays and aligning it with the database schema we've designed allows us to see how each step of the algorithm is supported by the database structure. Here’s how each step of "The Algorithm" maps to our PostgreSQL schema designed for storing and managing original and modernized texts in .fountain format:

### 1. Identify .fountain Text Types
- **Database Support**: The `dialogues` table can store different types of text (dialogue, action, character cue) identified in the analysis, using a column to denote the type (`character_name` for dialogues, potentially extending the schema to include action descriptions and character cues explicitly).

### 2. Structured Storage
- **Database Support**: Text chunks are stored in the `dialogues` table, which is linked to specific `scenes` and `scenes` to `acts`, ensuring organized and retrievable structure. Metadata such as `scene_id` and a sequence number (`sequence`) provides the context for each piece of dialogue.

### 3. Contextual Understanding
- **Database Support**: While the database itself does not analyze context or semantics, this step informs how text is paraphrased and categorized. The understanding gained here influences the paraphrasing process and how dialogues are associated with scenes and characters.

### 4. Paraphrasing
- **Database Support**: The `dialogues` table includes columns for both `original_text` and `modern_text`, allowing us to store the paraphrased (modernized) version alongside the original dialogue. This directly supports the paraphrasing step by keeping original and modernized texts linked within the same structure.

### 5. Storage and Retrieval
- **Database Support**: With both original and modernized texts stored in the `dialogues` table, retrieval for comparison or access is straightforward. The structured relationship between `plays`, `acts`, `scenes`, and `dialogues` ensures that text can be accessed in its proper context, facilitating easy comparison and access as per the algorithm’s requirements.

### 6. Compliance and Transparency
- **Database Support**: While the database itself does not inherently mark processes for compliance, this aspect of the algorithm is more about how we use and interact with the data. Documentation and metadata within the database, such as tracking version history or annotating paraphrasing decisions, can help support transparency. Additionally, implementing logging or audit tables could formalize this aspect further.

By structuring our database to accommodate both the original and modernized texts, along with detailed contextual metadata, we align closely with the steps outlined in "The Algorithm" for processing, storing, and managing the texts. This setup not only supports the efficient execution of each step but also ensures that the data remains organized, accessible, and compliant with relevant standards.