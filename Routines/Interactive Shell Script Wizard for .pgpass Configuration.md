# Interactive Shell Script Wizard for .pgpass Configuration

This document contains an interactive shell script designed to create a `.pgpass` file for the currently active user. The `.pgpass` file stores PostgreSQL database login credentials in a non-interactive manner, enabling scripts and applications to connect to the database without prompting for a password.

## Security Considerations

Before proceeding, it's crucial to understand the security implications of using a `.pgpass` file:

- The `.pgpass` file contains sensitive information, including database passwords. It should have strict file permissions to prevent unauthorized access.
- Store this file in the user's home directory and ensure it's owned by the user with read and write permissions set only for the owner (chmod 600).
- Never place `.pgpass` in a publicly accessible directory or version control.

## Script Usage

To use the script, copy the following code into a file, make it executable with `chmod +x filename.sh`, and run it with `./filename.sh`.

```bash
#!/bin/bash

# Interactive Shell Script to Create a .pgpass File

echo "Interactive .pgpass Configuration Wizard"
echo "----------------------------------------"

# Ask for the currently active user
echo "Determining the currently active user..."
ACTIVE_USER=$(whoami)
echo "The currently active user is: $ACTIVE_USER"

# Explain security considerations
echo "Before proceeding, please review the security considerations mentioned in the document."
echo "Press enter to acknowledge and continue."
read

# Create .pgpass in user's home directory
PGPASS_FILE="/home/$ACTIVE_USER/.pgpass"
echo "Creating .pgpass file at $PGPASS_FILE..."
touch "$PGPASS_FILE"

# Set strict file permissions
chmod 600 "$PGPASS_FILE"

# Inform the user of success
echo ".pgpass file created and secured with strict permissions."

# Prompt for database credentials
echo "Please enter your PostgreSQL database credentials."

read -p "Hostname (localhost if running locally): " HOSTNAME
read -p "Port (5432 is the default): " PORT
read -p "Database name: " DBNAME
read -p "User: " USER
read -s -p "Password: " PASSWORD
echo

# Write credentials to .pgpass
echo "$HOSTNAME:$PORT:$DBNAME:$USER:$PASSWORD" > "$PGPASS_FILE"

echo "Database credentials saved to $PGPASS_FILE."
echo "Configuration complete. Please ensure to keep your .pgpass file secure."

```

## Final Notes

- After running the script, verify the `.pgpass` file's contents and permissions.
- Ensure the database host is configured to allow connections using password authentication from the specified user.
- This script assumes the PostgreSQL server is accessible at the provided hostname and port, and that the database and user exist.

By following these steps, you can securely store your PostgreSQL credentials for non-interactive authentication purposes.