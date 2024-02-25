#!/bin/bash
echo "Microservices Setup Automation"

# Ask for PostgreSQL credentials and database details
read -p "Enter PostgreSQL database name: " dbname
read -p "Enter PostgreSQL user: " dbuser
read -s -p "Enter PostgreSQL password: " dbpass
echo
read -p "Enter base domain (e.g., benedikt-eickhoff.de): " basedomain

# Define an array of service names to create schemas and configure services
services=("playwright" "metadata" "script" "act" "scene" "character" "dialogue" "action" "transition" "parenthetical" "note" "centeredtext" "pagebreak" "sectionheading" "titlepage" "casting" "characterrelationship" "musicsound" "props" "revisionhistory" "formattingrules" "crossreferences" "extendednotesresearch" "scenelocation")

# PostgreSQL commands to create schemas and tables
for i in "${!services[@]}"; do
  # Define schema name
  schema="${services[$i]}_schema"

  # Create schema
  PGPASSWORD=$dbpass psql -h localhost -U $dbuser -d $dbname -c "CREATE SCHEMA IF NOT EXISTS $schema;"

  # Add table creation here based on schema (Placeholder for actual SQL commands)
  echo "Placeholder: Create table for $schema in database $dbname"
  
  # Configure PostgREST and Nginx
  port=$((3000 + $i + 1))
  domain="api-$((i + 1)).$basedomain"

  # Create PostgREST config
  cat > "/etc/postgrest/${schema}.conf" <<EOF
db-uri = "postgres://$dbuser:$dbpass@localhost:5432/$dbname"
db-schema = "$schema"
db-anon-role = "web_anon"
server-port = $port
EOF

  # Configure Nginx
  cat > "/etc/nginx/sites-available/$domain" <<EOF
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
  
  # Placeholder for starting PostgREST and reloading Nginx
  echo "Starting PostgREST for $schema and reloading Nginx..."
  
  # Enable HTTPS with Certbot (non-interactive mode)
  certbot --nginx -d $domain --non-interactive --agree-tos -m your-email@example.com --redirect
done

# Reload Nginx to apply configurations
nginx -t && systemctl reload nginx

echo "Setup completed."