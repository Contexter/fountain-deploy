
```
#!/bin/bash

# Directory containing the files to be checked and corrected
DIRECTORY="/etc/postgrest"

# Pattern to find and the correction to apply
FIND_PATTERN="play\!:"
REPLACE_PATTERN="play:"

# Loop through all files in the specified directory
for file in "$DIRECTORY"/*; do
    # Check if the file contains the problematic pattern
    if grep -q "$FIND_PATTERN" "$file"; then
        echo "Correcting $file"
        # Use sed to replace 'play!:' with 'play:' in-place
        sed -i "s/$FIND_PATTERN/$REPLACE_PATTERN/g" "$file"
    else
        echo "No correction needed for $file"
    fi
done

echo "All files checked and corrected if needed."
```

the postgrest naming convention ... well - ...