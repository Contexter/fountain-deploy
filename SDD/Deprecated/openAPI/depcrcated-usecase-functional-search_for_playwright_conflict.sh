#!/bin/bash

# The path to search for
conflicting_path="/playwright"

# Array of OpenAPI specification filenames from "The Fountain Array"
declare -a files=(
  "https-::api-act.fountain.coach.json"
  "https-::api-action.fountain.coach.json"
  "https-::api-casting.fountain.coach.json"
  "https-::api-centeredtext.fountain.coach.json"
  "https-::api-character.fountain.coach.json"
  "https-::api-characterrelationship.fountain.coach.json"
  "https-::api-crossreferences.fountain.coach.json"
  "https-::api-dialogue.fountain.coach.json"
  "https-::api-extendednotesresearch.fountain.coach.json"
  "https-::api-formattingrules.fountain.coach.json"
  "https-::api-metadata.fountain.coach.json"
  "https-::api-musicsound.fountain.coach.json"
  "https-::api-note.fountain.coach.json"
  "https-::api-pagebreak.fountain.coach.json"
  "https-::api-parenthetical.fountain.coach.json"
  "https-::api-playwright.fountain.coach.json"
  "https-::api-props.fountain.coach.json"
  "https-::api-revisionhistory.fountain.coach.json"
  "https-::api-scene.fountain.coach.json"
  "https-::api-scenelocation.fountain.coach.json"
  "https-::api-script.fountain.coach.json"
  "https-::api-sectionheading.fountain.coach.json"
  "https-::api-titlepage.fountain.coach.json"
  "https-::api-transition.fountain.coach.json"
)

# Loop through the array of filenames
for file in "${files[@]}"; do
  # Use jq to check if the file contains the conflicting path
  if jq -e --arg path "$conflicting_path" '.paths | has($path)' "$file" > /dev/null 2>&1; then
    echo "Found conflict in: $file"
  fi
done
