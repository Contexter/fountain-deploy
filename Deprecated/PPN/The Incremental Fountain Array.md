# walking the path to The Fountain 

Based on the information from "The Fountain Array", which outlines a comprehensive structure for managing and representing the complex structures of theatrical scripts, let's craft a shell script to set up a PostgreSQL playground tailored for exploring a similar database environment. This script will:

1. Install PostgreSQL (if not already installed).
2. Create a database named `fountain_db`.
3. Create a few sample tables that are central to the structure described in "The Fountain Array", such as `Playwright`, `Script`, and `Character`.
4. Insert some dummy data into these tables to kickstart the experimentation.

This script is intended for Debian-based systems (like Ubuntu). Adjustments might be necessary for other environments.

```bash
#!/bin/bash

# PostgreSQL setup for Fountain database playground

DB_NAME="fountain_db"
DB_USER="fountain_user"
DB_PASSWORD="change_this_password"
DB_PORT="5432" # default PostgreSQL port

# Function to check if PostgreSQL is installed
function check_postgres {
    which psql > /dev/null
    return $?
}

# Install PostgreSQL if not installed
if ! check_postgres; then
    echo "PostgreSQL is not installed. Installing..."
    sudo apt update && sudo apt install postgresql postgresql-contrib -y
else
    echo "PostgreSQL is already installed."
fi

# Start PostgreSQL service and enable it to start at boot
sudo systemctl start postgresql
sudo systemctl enable postgresql

# Create user and database
sudo -u postgres psql -c "CREATE USER $DB_USER WITH ENCRYPTED PASSWORD '$DB_PASSWORD';"
sudo -u postgres psql -c "CREATE DATABASE $DB_NAME OWNER $DB_USER;"

# Create tables and insert some data
sudo -u postgres PGPASSWORD=$DB_PASSWORD psql -d $DB_NAME -c "
CREATE TABLE playwright (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    biography TEXT,
    contact_information TEXT
);

CREATE TABLE script (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100),
    playwright_id INTEGER REFERENCES playwright(id),
    metadata TEXT,
    creation_date DATE,
    modification_date DATE,
    version_number INTEGER
);

CREATE TABLE character (
    id SERIAL PRIMARY KEY,
    script_id INTEGER REFERENCES script(id),
    name VARCHAR(100),
    description TEXT
);

-- Sample data
INSERT INTO playwright (name, biography, contact_information) VALUES
('William Shakespeare', 'English playwright, widely regarded as the greatest writer in the English language', 'info@shakespeare.com');

INSERT INTO script (title, playwright_id, metadata, creation_date, modification_date, version_number) VALUES
('Hamlet', 1, 'A tragedy by William Shakespeare', '1600-01-01', '1601-01-01', 1);

INSERT INTO character (script_id, name, description) VALUES
(1, 'Hamlet', 'Prince of Denmark');
"

echo "Fountain database playground setup complete."
```

**Instructions:**

1. Replace `DB_PASSWORD` with a secure password.
2. Save this script to a file, e.g., `setup_fountain_db.sh`.
3. Make the script executable: `chmod +x setup_fountain_db.sh`.
4. Execute the script: `./setup_fountain_db.sh`.

This script sets the stage for exploring database design principles relevant to the management and representation of complex data structures, such as theatrical scripts, within a PostgreSQL environment.

Here is an overview of "The Fountain Array" as described in the provided document:

## **The "Fountain" backend**

. designed to manage and represent the complex structures of theatrical scripts, includes a comprehensive array of tables, each serving a distinct purpose within the ecosystem of script management. Here's a detailed list of 24 key tables within the "Fountain" backend, known as "The Array," highlighting the function and interconnectivity of each:

1. **Playwright**: Stores details about script authors, including names, biographies, and contact information.
2. **Script**: Contains script titles, links (URLs), authorship, and metadata references.
3. **Metadata**: Captures creation dates, modification dates, version numbers, and additional script information.
4. **Act**: Organizes scripts into larger divisions, linking back to the Script table.
5. **Scene**: Breaks down acts into individual scenes, detailing the progression of the narrative.
6. **Character**: Lists characters in scripts, including names and descriptions, linked to specific scripts.
7. **Dialogue**: Stores spoken lines by characters, associated with specific scenes and characters.
8. **Action**: Details non-spoken actions or stage directions, linked to scenes and characters.
9. **Transition**: Manages scene or act transitions within the script, providing pacing and flow.
10. **Parenthetical**: Notes within dialogue blocks, offering additional context or action cues.
11. **Note**: General notes related to scripts, scenes, or characters, for additional information or reminders.
12. **Casting**: Details casting choices for characters, linking actors to roles within scripts.
13. **CharacterRelationship**: Describes relationships between characters, enhancing narrative depth.
14. **MusicSound**: Specifies music and sound effects used within scenes, linked to specific narrative moments.
15. **Props**: Lists physical props required for scenes, ensuring logistical preparation for performances.
16. **RevisionHistory**: Tracks changes to scripts over time, including edits, updates, and version tracking.
17. **FormattingRules**: Defines specific formatting guidelines applied to script texts for consistency.
18. **CenteredText**: Manages text that needs to be centered for stylistic or structural reasons within scripts.
19. **PageBreak**: Controls the pagination of scripts, ensuring clear division and readability.
20. **SectionHeading**: Organizes scripts into sections beyond acts and scenes for additional structure.
21. **TitlePage**: Contains information for the script's title page, including title, author, and copyright.
22. **ExtendedNotesResearch**: Stores extensive notes and research related to scripts for deeper context.
23. **SceneLocation**: Details the setting and location of scenes, providing background and atmosphere.
24. **CrossReferences**: Allows for the referencing of scenes or elements within or across scripts for thematic or narrative linkage.

These 24 tables constitute the foundational structure of the "Fountain" backend, enabling the detailed organization, analysis, and presentation of theatrical scripts. Each table plays a critical role in capturing the multifaceted aspects of scriptwriting and production, from the creative inception of a script to its practical execution on stage.