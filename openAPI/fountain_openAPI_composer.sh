#!/bin/bash

# Define the directory containing OpenAPI specs
SPEC_DIR="./openAPI"

# Define an array with the specific filenames of the OpenAPI specs
SPEC_FILES=(
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

# Ensure jq is installed
if ! command -v jq &> /dev/null; then
    echo "jq could not be found, please install jq to continue."
    exit 1
fi

# Temporary file for intermediate merges
TEMP_MERGE_FILE="${SPEC_DIR}/temp_merged_spec.json"

# Final merged file
FINAL_MERGE_FILE="${SPEC_DIR}/final_merged_spec.json"

# Initialize an empty JSON object in the temp file to start the merge
echo "{}" > "${TEMP_MERGE_FILE}"

# Function to merge all specified specs into one
merge_all_specs() {
    echo "Merging specified specs into a single source of truth..."
    for file in "${SPEC_FILES[@]}"; do
        full_path="${SPEC_DIR}/${file}"
        if [ ! -f "${full_path}" ]; then
            echo "Warning: Spec file ${file} not found, skipping..."
            continue
        fi
        echo "Merging $(basename "${full_path}")..."
        jq -s '
            def mergeArraysUnique: reduce .[] as $item ([]; . + [$item] | unique);
            def deepmerge:
                reduce .[] as $item ({}; . * $item | 
                .servers |= (if . then mergeArraysUnique else [] end) |
                .tags |= (if . then mergeArraysUnique else [] end));
            deepmerge' "${TEMP_MERGE_FILE}" "${full_path}" > "${TEMP_MERGE_FILE}.tmp" && mv "${TEMP_MERGE_FILE}.tmp" "${TEMP_MERGE_FILE}"
    done
    # Move the final merged content to the final file
    mv "${TEMP_MERGE_FILE}" "${FINAL_MERGE_FILE}"
    echo "All specified specs have been merged into ${FINAL_MERGE_FILE}"
}

# Start the merging process
merge_all_specs

# Cleanup
if [ -f "${TEMP_MERGE_FILE}" ]; then
    rm "${TEMP_MERGE_FILE}"
fi
if [ -f "${TEMP_MERGE_FILE}.tmp" ]; then
    rm "${TEMP_MERGE_FILE}.tmp"
fi

echo "Process completed."
