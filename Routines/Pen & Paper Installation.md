# Advanced Installation Script for PostgreSQL, PostgREST, Nginx, and Certbot on Ubuntu 20.04

This script automates the installation of PostgreSQL, PostgREST, Nginx, and Certbot on Ubuntu 20.04. It's designed to guide users through setting up their specific application requirements by asking interactive questions about database configuration, PostgREST setup, and Nginx server block creation.

## Usage Instructions:
1. Download the script to your Ubuntu 20.04 server.
2. Make the script executable: `chmod +x install_services.sh`.
3. Run the script with sudo privileges: `sudo ./install_services.sh`.
4. Follow the interactive prompts to configure your PostgreSQL database, PostgREST, Nginx, and secure your Nginx server with Certbot.

This script ensures a tailored installation and configuration process, making it easier for users to set up their backend services according to their unique use cases.

```bash
#!/bin/bash

echo "Automated Installation and Configuration Script for PostgreSQL, PostgREST, Nginx, and Certbot on Ubuntu 20.04"

# Update system packages
echo "Updating system packages..."
sudo apt update && sudo apt upgrade -y

# Install PostgreSQL
echo "Installing PostgreSQL..."
sudo apt install -y postgresql postgresql-contrib

# Prompt for PostgreSQL setup
read -p "Enter the desired PostgreSQL superuser username [postgres]: " pg_username
pg_username=${pg_username:-postgres}
echo "Creating PostgreSQL superuser: $pg_username"
sudo -u postgres createuser --superuser $pg_username

# Install PostgREST
echo "Installing PostgREST..."
wget https://github.com/PostgREST/postgrest/releases/download/v7.0.1/postgrest-v7.0.1-ubuntu.tar.xz
tar -xf postgrest-v7.0.1-ubuntu.tar.xz
sudo mv postgrest /usr/local/bin
rm postgrest-v7.0.1-ubuntu.tar.xz

# PostgREST configuration prompts
echo "Configuring PostgREST..."
sudo mkdir -p /etc/postgrest
config_path="/etc/postgrest/postgrest.conf"

read -p "Enter the PostgreSQL database name for PostgREST: " db_name
read -p "Enter the database user for PostgREST: " db_user
read -sp "Enter the database password for PostgREST: " db_pass
echo
read -p "Enter the PostgREST server port [3000]: " postgrest_port
postgrest_port=${postgrest_port:-3000}

# Create PostgREST config file
echo "Creating PostgREST configuration file at $config_path..."
sudo bash -c "cat > $config_path << EOF
db-uri = \"postgres://$db_user:$dbpass@localhost:5432/$db_name\"
db-schema = \"public\"
db-anon-role = \"$db_user\"
server-port = $postgrest_port
EOF"

# Install Nginx
echo "Installing Nginx..."
sudo apt install -y nginx

# Install Certbot
echo "Installing Certbot for Nginx..."
sudo apt install -y certbot python3-certbot-nginx

# Nginx configuration prompts
echo "Configuring Nginx to serve PostgREST..."
read -p "Enter the domain name for your PostgREST API (e.g., api.example.com): " domain_name

# Suggest Nginx server block configuration
nginx_conf_path="/etc/nginx/sites-available/$domain_name"
echo "Creating Nginx server block for $domain_name at $nginx_conf_path..."
sudo bash -c "cat > $nginx_conf_path << EOF
server {
    listen 80;
    server_name $domain_name;

    location / {
        proxy_pass http://localhost:$postgrest_port;
        proxy_set_header Host \$host;
        proxy_set_header X-Real-IP \$remote_addr;
        proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto \$scheme;
    }
}
EOF"

sudo ln -s $nginx_conf_path /etc/nginx/sites-enabled/
sudo nginx -t && sudo systemctl reload nginx

# Certbot SSL setup
echo "Securing $domain_name with Certbot..."
sudo certbot --nginx -d $domain_name --non-interactive --agree-tos --redirect --email your-email@example.com

echo "Installation and basic configuration are complete. Please proceed with further customization based on your application requirements."
```