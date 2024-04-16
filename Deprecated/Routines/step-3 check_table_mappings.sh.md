# Is the database correctly boostrapped? 

to check if all tables exist correctly within their respective schema namespaces in the PostgreSQL database, you can use the `psql` command to query the PostgreSQL system catalog. This script will iterate through each schema and table to verify their existence:

```bash
#!/bin/bash

# Ask for PostgreSQL credentials and database name interactively
read -p "Enter PostgreSQL database name: " DB_NAME
read -p "Enter PostgreSQL user: " DB_USER
echo -n "Enter PostgreSQL password: " && read -s DB_PASSWORD && echo

# Define the schema and tables expected to exist
declare -A schema_tables=(
    ["playwright"]="Playwright"
    ["metadata"]="Metadata"
    ["script"]="Script"
    ["act"]="Act"
    ["scene"]="Scene"
    ["character"]="Character"
    ["dialogue"]="Dialogue"
    ["action"]="Action"
    ["transition"]="Transition"
    ["parenthetical"]="Parenthetical"
    ["note"]="Note"
    ["centeredtext"]="CenteredText"
    ["pagebreak"]="PageBreak"
    ["sectionheading"]="SectionHeading"
    ["titlepage"]="TitlePage"
    ["casting"]="Casting"
    ["characterrelationship"]="CharacterRelationship"
    ["musicsound"]="MusicSound"
    ["props"]="Props"
    ["revisionhistory"]="RevisionHistory"
    ["formattingrules"]="FormattingRules"
    ["crossreferences"]="CrossReferences"
    ["extendednotesresearch"]="ExtendedNotesResearch"
    ["scenelocation"]="SceneLocation"
)

# Test database connection
echo "Testing database connection for $DB_USER..."
export PGPASSWORD=$DB_PASSWORD
if psql -h localhost -U $DB_USER -d $DB_NAME -c '\conninfo'; then
    echo "Database connection successful."
else
    echo "Database connection FAILED."
    unset PGPASSWORD
    exit 1
fi

# Function to check if a table exists in the schema
check_table_exists() {
    local schema=$1
    local table=$2
    local query="SELECT to_regclass('${schema}.${table}');"
    local result=$(psql -h localhost -U $DB_USER -d $DB_NAME -tAc "$query")

    if [[ $result == "${schema}.${table}" ]]; then
        echo "Table ${schema}.${table} exists."
    else
        echo "Table ${schema}.${table} does NOT exist."
    fi
}

# Loop through schemas and tables to check existence
for schema in "${!schema_tables[@]}"; do
    table=${schema_tables[$schema]}
    check_table_exists $schema $table
done

# Clean up
unset PGPASSWORD
echo "Verification completed."
```

This script includes:
- A `schema_tables` associative array mapping each schema to its expected table. Adjust the array as needed for your specific tables.
- A function `check_table_exists` to check for the existence of a table within a specific schema.
- A loop that iterates through each schema-table pair, calling `check_table_exists` to verify each table's existence.

**Important Notes:**
- Ensure that the PostgreSQL user (`$DB_USER`) has sufficient permissions to query the system catalog.
- The script now sets and unsets `PGPASSWORD` for password authentication. This method exposes the password to the environment, which may have security implications. Consider using `.pgpass` or another secure method for production environments.
- Adjust the script according to your environment, especially the database host (`-h localhost`) if your PostgreSQL server is not running on the same host.