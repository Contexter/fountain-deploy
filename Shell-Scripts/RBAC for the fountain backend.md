### Introduction

The script presented here is designed as a foundational tool for Role-Based Access Control (RBAC) management within the context of the Fountain backend, specifically tailored for environments utilizing PostgreSQL and PostgREST. RBAC is a method of regulating access to system resources based on the roles assigned to individual users within an organization. This script facilitates a rudimentary yet effective implementation of RBAC by enabling administrators to dynamically create roles, assign them specific permissions across various database schemas, and ensure these roles are properly integrated with PostgREST configurations.

```
#!/bin/bash

# Enhanced Script for Role Creation, Schema Selection, and Dynamic HTTP Verb Permissions Application

echo "Enter the PostgreSQL database name:"
read DB_NAME
echo "Enter the PostgreSQL database user (should have admin privileges):"
read DB_USER
echo "Enter the password for the database user (input will be hidden):"
read -s DB_PASSWORD

# Define an array of schemas
SCHEMAS=("playwright" "metadata" "script" "act" "scene" "character" "dialogue" "action" "transition" "parenthetical" "note" "centeredtext" "pagebreak" "sectionheading" "titlepage" "casting" "characterrelationship" "musicsound" "props" "revisionhistory" "formattingrules" "crossreferences" "extendednotesresearch" "scenelocation")

# Schema selection
echo "Available schemas:"
for i in "${!SCHEMAS[@]}"; do
    printf "%2d. %s\n" $((i+1)) "${SCHEMAS[$i]}"
done
echo "Select a schema by entering the number (1-${#SCHEMAS[@]}):"
read SCHEMA_SELECTION

# Validate selection and assign schema
if ! [[ "$SCHEMA_SELECTION" =~ ^[0-9]+$ ]] || [ "$SCHEMA_SELECTION" -lt 1 ] || [ "$SCHEMA_SELECTION" -gt "${#SCHEMAS[@]}" ]; then
    echo "Invalid selection. Exiting script."
    exit 1
fi
SCHEMA="${SCHEMAS[$SCHEMA_SELECTION-1]}"
echo "Selected schema: $SCHEMA"

# Role creation or selection
echo "Enter the name for the custom role (letters only, 'web_anon' to use the default web anonymous role):"
read ROLE

# Verify role name
if [[ ! "$ROLE" =~ ^[a-zA-Z]+$ ]] && [ "$ROLE" != "web_anon" ]; then
    echo "Role name is invalid. Please use letters only."
    exit 1
fi

export PGPASSWORD=$DB_PASSWORD

# Check if role exists, create if not
if [ "$ROLE" != "web_anon" ]; then
    echo "Checking if role $ROLE exists..."
    if ! psql -h localhost -U $DB_USER -d $DB_NAME -tAc "SELECT 1 FROM pg_roles WHERE rolname='$ROLE'" | grep -q 1; then
        echo "Role $ROLE does not exist. Creating role..."
        psql -h localhost -U $DB_USER -d $DB_NAME -c "CREATE ROLE $ROLE NOLOGIN;"
    else
        echo "Role $ROLE already exists."
    fi
fi

# HTTP Verb selection for CRUD operations
CRUD_OPERATIONS=("SELECT" "INSERT" "UPDATE" "DELETE")
echo "Select HTTP Verbs for CRUD operations (multiple selections allowed, e.g., 1,3):"
echo "1. SELECT (Read)"
echo "2. INSERT (Create)"
echo "3. UPDATE (Update)"
echo "4. DELETE (Delete)"
read -p "Your choice: " CRUD_CHOICES

# Split choices into an array and validate
IFS=',' read -ra SELECTED_CRUD <<< "$CRUD_CHOICES"
for i in "${SELECTED_CRUD[@]}"; do
    if ! [[ "$i" =~ ^[1-4]$ ]]; then
        echo "Invalid CRUD operation selection: $i"
        exit 1
    fi
done

# Apply permissions based on selected CRUD operations
for i in "${SELECTED_CRUD[@]}"; do
    VERB=${CRUD_OPERATIONS[$i-1]}
    echo "Applying $VERB permission on schema $SCHEMA to role $ROLE..."
    psql -h localhost -U $DB_USER -d $DB_NAME -c "GRANT $VERB ON ALL TABLES IN SCHEMA $SCHEMA TO $ROLE;"
done
echo "Permissions applied. Please verify."

unset PGPASSWORD

# Reminder to adjust PostgREST configuration and restart services
echo "Reminder: Adjust your PostgREST configuration to use the newly created role '$ROLE' for enhanced security."
echo "Ensure the 'db-schema' is set to '$SCHEMA', and 'db-anon-role' is updated to '$ROLE'."
echo "Please ensure to restart your PostgREST services to apply changes."

```


### Use Case Description

The primary use case for this script revolves around the need for secure, efficient, and flexible management of access controls within the Fountain backend. As applications grow in complexity and size, the necessity for a granular and scalable permission system becomes paramount. This script addresses several key scenarios:

- **Initial Setup**: For new deployments of the Fountain backend, the script allows for the rapid setup of roles and permissions aligned with the specific access requirements of different parts of the application.
- **Updates and Maintenance**: As the backend evolves, new schemas may be added, or existing ones may undergo changes. The script provides a straightforward way to update roles and permissions to reflect these changes.
- **Security Enhancements**: In scenarios requiring a review or overhaul of access controls to enhance security, the script facilitates the examination and reconfiguration of roles and permissions across the database.
- **Development and Testing**: Developers and testers can use the script to create temporary roles with specific permissions, enabling focused testing and development activities without affecting production roles or permissions.

### Implementation Comment

This script is a rudimentary RBAC solution for the Fountain backend, leveraging the capabilities of PostgreSQL for role and permission management and PostgREST for RESTful API interactions. While it covers the essentials of role creation, schema selection, and permission assignment based on CRUD operations, there are several areas where it could be expanded or refined:

- **Validation and Error Handling**: Enhancements could be made to further validate user inputs and handle potential errors more gracefully, ensuring robustness and user-friendliness.
- **Automation and Integration**: The script could be integrated into a larger suite of administrative tools, offering automated role and permission management based on deployment scripts or configuration files.
- **UI Integration**: For even greater usability, especially for non-technical users, the functionality could be wrapped in a web-based UI, allowing for point-and-click management of roles and permissions.
- **Audit and Compliance Features**: Incorporating logging and reporting features would enable administrators to audit changes to roles and permissions, aiding in compliance with security policies and regulations.

As it stands, the script provides a solid foundation for RBAC within the Fountain backend. However, like any rudimentary solution, it serves as a starting point for further development and customization to meet the specific needs and security requirements of the organization.