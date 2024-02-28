# change test focus on:

- Verifying PostgreSQL service status.
- Checking the status of each PostgREST service.
- Testing the database connection using the `sudo -u` method to match the PostgreSQL user with the system user.
- Verifying the accessibility of the GoAccess dashboard without checking the SSL certificates.

```bash
#!/bin/bash

# Ask for PostgreSQL credentials and database name interactively
read -p "Enter PostgreSQL database name: " DB_NAME
read -p "Enter PostgreSQL user: " DB_USER
echo -n "Enter PostgreSQL password (will not be used but kept for consistency): " && read -s DB_PASSWORD && echo
read -p "Enter base domain (e.g., example.com): " BASEDOMAIN
echo -n "Enter your email for SSL certificates (unused but kept for consistency): " && read EMAIL

# Array of services from the setup script
services=("playwright" "metadata" "script" "act" "scene" "character"
"dialogue" "action" "transition" "parenthetical" "note" "centeredtext"
"pagebreak" "sectionheading" "titlepage" "casting" "characterrelationship"
"musicsound" "props" "revisionhistory" "formattingrules" "crossreferences"
"extendednotesresearch" "scenelocation")

# Check PostgreSQL service status
echo "Checking PostgreSQL service status..."
sudo systemctl is-active --quiet postgresql && echo "PostgreSQL service is active." || echo "PostgreSQL service is NOT active."

# Loop through services to check PostgREST service status
for schema in "${services[@]}"; do
    echo "Checking PostgREST service for $schema..."
    sudo systemctl is-active --quiet postgrest-$schema.service && echo "PostgREST $schema service is active." || echo "PostgREST $schema service is NOT active."
done

# Test database connection using sudo -u method
echo "Testing database connection for $DB_USER using sudo..."
if sudo -u $DB_USER psql -d $DB_NAME -c '\conninfo'; then
    echo "Database connection successful."
else
    echo "Database connection FAILED."
fi

# Check GoAccess dashboard accessibility
GOACCESS_DOMAIN="logs.$BASEDOMAIN"
echo "Verifying GoAccess dashboard accessibility at https://$GOACCESS_DOMAIN..."
if curl -s --head  --request GET https://$GOACCESS_DOMAIN | grep "200 OK" > /dev/null; then
    echo "GoAccess dashboard is accessible."
else
    echo "GoAccess dashboard is NOT accessible."
fi

echo "Verification completed."
```

Changes made:
- Removed the section that checks SSL certificates for each domain.
- Kept the prompt for the email address associated with SSL certificates for consistency, although it's not used in this script. This can be removed if you prefer not to ask for unused information.



Before running this script, ensure that the necessary user permissions and configurations are in place for each step to execute successfully.