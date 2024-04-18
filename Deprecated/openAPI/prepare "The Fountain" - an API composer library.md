# prepare "The Fountain" - an API composer library

Given the full scope of "The Fountain" backend and the specified naming convention for all 24 clients, here is a script that prepares the directories within "The-Fountain" to be recognizable by Python's import mechanism by ensuring each client directory is properly set up as a Python package. This script adds an `__init__.py` file to each client directory, corresponding to each table of the "Fountain" backend.

```bash
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
```

### Instructions for Using the Script

1. Ensure that "The-Fountain" directory is present at the specified location and contains all the client directories named according to the convention.
2. Save the script to a file, for example, `prepare_the_fountain.sh`, in the parent directory of "The-Fountain".
3. Make the script executable: `chmod +x prepare_the_fountain.sh`.
4. Run the script: `./prepare_the_fountain.sh`.

This script systematically checks each client directory within "The-Fountain" and ensures that an `__init__.py` file is present, making each directory a recognizable Python package. This allows for easy import and use of these packages in your Python projects, including FastAPI applications.

# Example App

To import from "The-Fountain" into a FastAPI application, let's assume you've structured "The-Fountain" as described and have prepared it properly as a Python package with subpackages for each client. Below is an example of how you might structure a simple FastAPI application and import a module from one of "The-Fountain"'s clients.

Assuming you have a function or class within `playwright_client` that you want to use, such as `PlaywrightApi` from an `api.py` file:

### Step 1: Project Structure

Your project directory might look something like this:

```
my_fastapi_project/
├── The-Fountain/
│   ├── __init__.py
│   ├── playwright_client/
│   │   ├── __init__.py
│   │   ├── api.py
│   │   └── models.py
│   ├── script_client/
│   │   ├── __init__.py
│   │   └── ...
│   └── ...
├── app.py
└── requirements.txt
```

### Step 2: FastAPI Application (`app.py`)

Here is how you could import the `PlaywrightApi` from the `playwright_client` within "The-Fountain" into your FastAPI application:

```python
from fastapi import FastAPI
from The-Fountain.playwright_client.api import PlaywrightApi

app = FastAPI()

@app.get("/")
async def get_playwright():
    # Assuming PlaywrightApi has a method to fetch playwright details
    playwright_api = PlaywrightApi()
    details = playwright_api.get_details()  # Example method
    return {"playwright_details": details}
```

### Important Notes

- Make sure the `The-Fountain` directory is in your Python path. This can be achieved by running the FastAPI application from the `my_fastapi_project` directory, ensuring Python recognizes `The-Fountain` as a package.
- Ensure that each client directory inside `The-Fountain`, including `playwright_client`, is a Python package (has an `__init__.py` file).
- This example assumes `PlaywrightApi` class and `get_details` method are placeholders for whatever functionality you have defined within `playwright_client/api.py`.

### Step 3: Running Your FastAPI Application

Run your FastAPI application using Uvicorn or another ASGI server from the root of your project directory (`my_fastapi_project`). For example, if using Uvicorn:

```bash
uvicorn app:app --reload
```

This command starts your FastAPI application, making it available for testing, and allows you to import and use the structured clients within "The-Fountain" seamlessly.

