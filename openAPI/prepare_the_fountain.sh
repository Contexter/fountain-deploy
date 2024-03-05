#!/bin/bash

# Path to the "The-Fountain" directory
THE_FOUNTAIN_DIR="The-Fountain"

# List of all client directories according to the "The Fountain" backend tables
CLIENT_DIRS=(
    "playwright_client"
    "script_client"
    "metadata_client"
    "act_client"
    "scene_client"
    "character_client"
    "dialogue_client"
    "action_client"
    "transition_client"
    "parenthetical_client"
    "note_client"
    "casting_client"
    "character_relationship_client"
    "music_sound_client"
    "props_client"
    "revision_history_client"
    "formatting_rules_client"
    "centered_text_client"
    "page_break_client"
    "section_heading_client"
    "title_page_client"
    "extended_notes_research_client"
    "scene_location_client"
    "cross_references_client"
)

# Iterate over each client directory
for CLIENT_DIR in "${CLIENT_DIRS[@]}"; do
    # Full path to the client directory
    FULL_PATH="${THE_FOUNTAIN_DIR}/${CLIENT_DIR}"
    
    # Check if the directory exists
    if [ -d "$FULL_PATH" ]; then
        # Check if __init__.py exists, create if it doesn't
        if [ ! -f "${FULL_PATH}/__init__.py" ]; then
            touch "${FULL_PATH}/__init__.py"
            echo "Created __init__.py in ${FULL_PATH}"
        else
            echo "__init__.py already exists in ${FULL_PATH}"
        fi
    else
        echo "Directory ${FULL_PATH} does not exist"
    fi
done

echo "All client directories in 'The-Fountain' are prepared for Python's import mechanism."
