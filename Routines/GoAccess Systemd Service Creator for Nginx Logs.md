# GoAccess Systemd Service Creator for Nginx Logs

This script is designed to automate the process of configuring GoAccess to monitor nginx log files by creating systemd service files. It's particularly useful for systems with multiple nginx virtual hosts, ensuring GoAccess monitors all relevant log files, including those in custom locations.

## Features

- **Automated Discovery**: Finds log files specified in nginx virtual host configurations.
- **Custom Log Directory Support**: Includes a predefined custom log directory for additional monitoring.
- **Systemd Service Creation**: Generates a unique systemd service file for each log file, enabling GoAccess to run as a system service.
- **Idempotency**: Safely rerun the script without duplicating configurations or creating extra service files.

## Script

```bash
#!/bin/bash

# Define nginx and GoAccess configurations
NGINX_VHOSTS_DIR="/etc/nginx/sites-enabled"
CUSTOM_LOG_DIR="/home/fastapi-user/fastapi-nginx-gunicorn/logs" # Custom log directory
GOACCESS_CONF_DIR="/etc/goaccess" # Assuming a directory for GoAccess configurations
GOACCESS_SYSTEMD_DIR="/etc/systemd/system" # Systemd service files directory

# Create GoAccess configuration directory if it doesn't exist
mkdir -p "$GOACCESS_CONF_DIR"

# Function to process log files and create systemd service for GoAccess
process_log_file() {
    local log_path=$1
    if [ -n "$log_path" ] && [ -f "$log_path" ]; then
        # Generate a GoAccess configuration file for each log
        local goaccess_conf="${GOACCESS_CONF_DIR}/goaccess_$(basename "$log_path").conf"
        local service_name="goaccess_$(basename "$log_path" | sed 's/\.[^.]*$//').service"
        
        # Create a GoAccess configuration file if it doesn't exist
        if [ ! -f "$goaccess_conf" ]; then
            echo "
log-file $log_path
log-format COMBINED
" > "$goaccess_conf"
        fi

        # Create systemd service file for GoAccess
        if [ ! -f "${GOACCESS_SYSTEMD_DIR}/${service_name}" ]; then
            echo "Creating systemd service for $log_path"
            echo "[Unit]
Description=GoAccess for $(basename "$log_path")
After=network.target

[Service]
Type=simple
ExecStart=/usr/bin/goaccess $log_path -p $goaccess_conf -o /var/www/html/$(basename "$log_path" | sed 's/\.[^.]*$//').html --real-time-html

[Install]
WantedBy=multi-user.target
" > "${GOACCESS_SYSTEMD_DIR}/${service_name}"

            # Reload systemd to recognize new service and start the service
            systemctl daemon-reload
            systemctl start "$service_name"
            systemctl enable "$service_name"
        else
            echo "Systemd service for $log_path already exists."
        fi
    else
        echo "Log file $log_path does not exist."
    fi
}

# Process nginx vhosts configurations
find "$NGINX_VHOSTS_DIR" -type f | while read -r vhost_conf; do
    access_logs=$(grep -Eo 'access_log\s+[^;]+' "$vhost_conf" | awk '{print $2}')
    error_logs=$(grep -Eo 'error_log\s+[^;]+' "$vhost_conf" | awk '{print $2}')
    
    # Process each log file found
    for log_path in $access_logs $error_logs; do
        process_log_file "$log_path"
    done
done

# Process custom log directory
if [ -d "$CUSTOM_LOG_DIR" ]; then
    for log_path in "$CUSTOM_LOG_DIR"/*; do
        process_log_file "$log_path"
    done
else
    echo "Custom log directory $CUSTOM_LOG_DIR does not exist."
fi

echo "GoAccess monitoring has been configured for all found nginx log files."
```

## Behavior on Subsequent Runs

When the script runs on the same machine multiple times, it carefully checks for existing configurations to prevent duplication. Here’s how it handles multiple executions:

- **GoAccess Configuration Files**: Does not overwrite existing GoAccess configuration files, preserving custom settings.
- **Systemd Service Files**: Skips creating new systemd service files if they already exist, ensuring no service disruption or configuration duplication.
- **Service Management**: Avoids restarting or re-enabling existing services, maintaining the current state without unnecessary changes.

This idempotent behavior ensures the script can be safely rerun to accommodate new log files without affecting the existing setup.

## Usage

1. Ensure you have GoAccess and nginx installed on your Ubuntu 20.04 system.
2. Place the script in a suitable directory.
3. Make the script executable with `chmod +x <scriptname.sh>`.
4. Run the script as root or with sudo to ensure it has permissions to create systemd service files and access log files.

This script streamlines the monitoring setup for nginx logs with GoAccess, making it an essential tool for administrators looking to automate their log analysis workflow.