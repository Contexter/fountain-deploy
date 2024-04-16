# GoAccess Deployment for "https://log.benedikt-eickhoff.de"

This document outlines the step-by-step process of installing, configuring, and deploying GoAccess for real-time web log analysis, served securely over SSL for the domain "https://log.benedikt-eickhoff.de". The setup includes demonizing the GoAccess WebSocket server process for continuous, real-time monitoring.

## Installation of GoAccess

1. Update the package list:
   ```bash
   sudo apt-get update
   ```
2. Install GoAccess:
   ```bash
   sudo apt-get install goaccess -y
   ```

## SSL Certificate Setup with Certbot

1. Install Nginx and Certbot:
   ```bash
   sudo apt-get install nginx certbot python3-certbot-nginx -y
   ```
2. Obtain an SSL certificate for the domain:
   ```bash
   sudo certbot --nginx -d log.benedikt-eickhoff.de
   ```
   Follow Certbot's prompts to automatically configure Nginx and secure the domain with SSL.

## Nginx Configuration for GoAccess Report

1. Ensure there's an Nginx configuration for `log.benedikt-eickhoff.de` with the `server_name` directive correctly set.
2. Modify the Nginx configuration to serve the GoAccess HTML report at the root URL. Example server block:
   ```nginx
   server {
       listen 443 ssl http2;
       server_name log.benedikt-eickhoff.de;
       root /var/www/html;
       location / {
           try_files /report.html =404;
       }
   }
   ```
3. Reload Nginx to apply changes:
   ```bash
   sudo systemctl reload nginx
   ```

## Setting Up GoAccess as a System Service

1. Create a systemd service file `/etc/systemd/system/goaccess.service` with the following configuration:
   ```ini
   [Unit]
   Description=GoAccess Live Web Log Analyzer
   After=network.target

   [Service]
   Type=simple
   ExecStart=/usr/bin/goaccess /var/log/nginx/access.log -o /var/www/html/report.html --log-format=COMBINED --real-time-html --daemon
   User=www-data
   Group=www-data
   Restart=on-failure
   RestartSec=30

   [Install]
   WantedBy=multi-user.target
   ```
2. Start and enable the GoAccess service:
   ```bash
   sudo systemctl start goaccess.service
   sudo systemctl enable goaccess.service
   ```

## Verifying the Setup

1. Access "https://log.benedikt-eickhoff.de" to view the GoAccess report.
2. Check the status of the GoAccess service:
   ```bash
   sudo systemctl status goaccess.service
   ```

This setup ensures that GoAccess provides continuous, real-time log analysis, accessible securely over SSL. The GoAccess WebSocket server process runs as a daemon, ensuring uptime and reliability for real-time monitoring purposes.