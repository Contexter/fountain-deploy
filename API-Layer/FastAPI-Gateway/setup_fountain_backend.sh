#!/bin/bash

set -e

# Define the root directory for the FastAPI project
PROJECT_ROOT="fountain_backend"
APP_DIR="$PROJECT_ROOT/app"
DIRECTORIES=("api/endpoints" "core" "db/models" "schemas" "services" "tests/api" "tests/core" "tests/services")

echo "Creating FastAPI project structure..."

# Create the project root directory and subdirectories
mkdir -p $PROJECT_ROOT

for dir in "${DIRECTORIES[@]}"; do
    mkdir -p "$APP_DIR/$dir"
done

# Create __init__.py files to make Python treat directories as packages
find "$APP_DIR" -type d -exec touch {}/__init__.py \;

# Generate core files
cat > "$APP_DIR/core/config.py" <<EOF
# Configuration settings
class Settings:
    PROJECT_NAME: str = "Fountain Backend"

settings = Settings()
EOF

cat > "$APP_DIR/core/events.py" <<EOF
# Event handlers for startup and shutdown actions
from fastapi import FastAPI

def create_start_app_handler(app: FastAPI) -> callable:
    async def start_app() -> None:
        # Perform startup actions here
        pass
    return start_app

def create_stop_app_handler(app: FastAPI) -> callable:
    async def stop_app() -> None:
        # Perform shutdown actions here
        pass
    return stop_app
EOF

cat > "$APP_DIR/main.py" <<EOF
# FastAPI application entry point
from fastapi import FastAPI
from .core.config import settings
from .core.events import create_start_app_handler, create_stop_app_handler

app = FastAPI(title=settings.PROJECT_NAME)

@app.get("/")
async def root():
    return {"message": "Hello World"}
EOF

# Define database tables as entities
declare -a entities=("playwright" "metadata" "script" "act" "scene" "character" "dialogue" "action" "transition" \
                     "parenthetical" "note" "centered_text" "page_break" "section_heading" "title_page" "casting" \
                     "character_relationship" "music_sound" "props" "revision_history" "formatting_rules" \
                     "cross_references" "extended_notes_research" "scene_location")

# Function to generate SQLAlchemy model files based on the provided schema
generate_model_files() {
    echo "Generating SQLAlchemy models, Pydantic schemas, service layers, and API endpoints..."
    for entity in "${entities[@]}"; do
        # Model file generation (stub)
        model_file="$APP_DIR/db/models/${entity}.py"
        echo "from sqlalchemy import Column, Integer, String, ForeignKey, Text, Date, Boolean" > "$model_file"
        echo "from sqlalchemy.orm import relationship" >> "$model_file"
        echo "from database import Base" >> "$model_file"
        echo "" >> "$model_file"
        echo "class ${entity^}(Base):" >> "$model_file"
        echo "    __tablename__ = '${entity}'" >> "$model_file"
        echo "    id = Column(Integer, primary_key=True, index=True)" >> "$model_file"
        # Additional fields based on each entity
        # This is a simplified example; you should add all fields according to your schema
        
        # Schema file generation (stub)
        schema_file="$APP_DIR/schemas/${entity}.py"
        echo "from pydantic import BaseModel" > "$schema_file"
        echo "" >> "$schema_file"
        echo "class ${entity^}Base(BaseModel):" >> "$schema_file"
        echo "    # Define common base attributes here" >> "$schema_file"
        echo "" >> "$schema_file"
        echo "class ${entity^}Create(${entity^}Base):" >> "$schema_file"
        echo "    # Define creation-specific attributes here" >> "$schema_file"
        echo "" >> "$schema_file"
        echo "class ${entity^}(${entity^}Base):" >> "$schema_file"
        echo "    id: int" >> "$schema_file"
        echo "    # Define additional attributes here" >> "$schema_file"
        echo "" >> "$schema_file"
        echo "    class Config:" >> "$schema_file"
        echo "        orm_mode = True" >> "$schema_file"
        
        # Service layer file generation (stub)
        service_file="$APP_DIR/services/${entity}_service.py"
        echo "# Service layer for handling ${entity} logic" > "$service_file"
        echo "from sqlalchemy.orm import Session" >> "$service_file"
        echo "from ..schemas import ${entity^}Create, ${entity^}" >> "$service_file"
        echo "from ..db.models import ${entity^}" >> "$service_file"
        echo "" >> "$service_file"
        echo "def create_${entity}(db: Session, ${entity}: ${entity^}Create):" >> "$service_file"
        echo "    # Add service logic here" >> "$service_file"
        echo "" >> "$service_file"
        
        # API endpoint file generation (stub)
        endpoint_file="$APP_DIR/api/endpoints/${entity}.py"
        echo "from fastapi import APIRouter, Depends" > "$endpoint_file"
        echo "from sqlalchemy.orm import Session" >> "$endpoint_file"
        echo "from typing import List" >> "$endpoint_file"
        echo "from ...db.database import get_db" >> "$endpoint_file"
        echo "from ...schemas import ${entity^}Create, ${entity^}" >> "$endpoint_file"
        echo "from ...services import ${entity}_service" >> "$endpoint_file"
        echo "" >> "$endpoint_file"
        echo "router = APIRouter()" >> "$endpoint_file"
        echo "" >> "$endpoint_file"
        echo "@router.post('/', response_model=${entity^})" >> "$endpoint_file"
        echo "def create_${entity}(${entity}: ${entity^}Create, db: Session = Depends(get_db)):" >> "$endpoint_file"
        echo "    return ${entity}_service.create_${entity}(db=db, ${entity}=${entity})" >> "$endpoint_file"
        echo "" >> "$endpoint_file"
        # Add routing to main.py
        echo "from .endpoints.${entity} import router as ${entity}_router" >> "$APP_DIR/main.py"
        echo "app.include_router(${entity}_router, prefix='/${entity}', tags=['${entity}'])" >> "$APP_DIR/main.py"
    done
}

# Call the function to generate model files
generate_model_files

# Finalize main.py
echo "" >> "$APP_DIR/main.py"
echo "# Add additional routes here" >> "$APP_DIR/main.py"

# Generate requirements.txt
cat > "$PROJECT_ROOT/requirements.txt" <<EOF
fastapi==0.65.2
uvicorn==0.14.0
SQLAlchemy==1.4.15
pydantic==

1.8.2
EOF

echo "FastAPI project structure with SQLAlchemy models, Pydantic schemas, service layers, and API endpoints created successfully."
