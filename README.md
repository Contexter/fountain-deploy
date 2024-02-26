
# Shell Script Automation: setup_microservices.sh

This script automates the setup process for microservices, including creating schemas and tables in PostgreSQL, configuring PostgREST instances, setting up Nginx server blocks, and securing connections with SSL certificates via Certbot.
```
#!/bin/bash
echo "Fountain Microservices Setup Automation"

# Gather PostgreSQL credentials and base domain information
read -p "Enter PostgreSQL database name: " dbname
read -p "Enter PostgreSQL user: " dbuser
echo -n "Enter PostgreSQL password: "
read -s dbpass
echo
read -p "Enter base domain (e.g., benedikt-eickhoff.de): " basedomain

# Service names representing tables and corresponding schemas
services=("playwright" "metadata" "script" "act" "scene" "character" "dialogue" "action" "transition" "parenthetical" "note" "centeredtext" "pagebreak" "sectionheading" "titlepage" "casting" "characterrelationship" "musicsound" "props" "revisionhistory" "formattingrules" "crossreferences" "extendednotesresearch" "scenelocation")

# Path to the SQL bootstrap file
sql_path="/path/to/fountain_microservices_bootstrap.sql"

# Loop to set up schemas and tables, and configure PostgREST and Nginx
for i in "${!services[@]}"; do
  schema="${services[$i]}_schema"

  # Create schema and import table structure
  PGPASSWORD=$dbpass psql -h localhost -U $dbuser -d $dbname <<EOF
CREATE SCHEMA IF NOT EXISTS $schema;
\set ON_ERROR_STOP on
\i $sql_path
EOF

  echo "Schema and tables for $schema created in $dbname."

  # PostgREST configuration
  port=$((3000 + i))
  domain="api-$((i + 1)).$basedomain"

  # PostgREST config file creation
  cat <<EOF > "/etc/postgrest/${schema}.conf"
db-uri = "postgres://$dbuser:$dbpass@localhost:5432/$dbname"
db-schema = "$schema"
db-anon-role = "web_anon"
server-port = $port
EOF

  # Nginx reverse proxy configuration
  cat <<EOF > "/etc/nginx/sites-available/$domain"
server {
    listen 80;
    server_name $domain;
    
    location / {
        proxy_pass http://localhost:$port;
        proxy_set_header Host \$host;
        proxy_set_header X-Real-IP \$remote_addr;
        proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto \$scheme;
    }
}
EOF
  ln -s /etc/nginx/sites-available/$domain /etc/nginx/sites-enabled/

  # Start PostgREST for the schema
  postgrest "/etc/postgrest/${schema}.conf" &

  # Enable HTTPS with Certbot
  certbot --nginx -d $domain --non-interactive --agree-tos -m your-mail@benedikt-eickhoff.de --redirect
done

# Reload Nginx to apply the new configurations
nginx -t && systemctl reload nginx

echo "Fountain backend setup with microservices architecture completed."
```
