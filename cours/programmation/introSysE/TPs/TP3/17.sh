#!bin/bash

if [ ! -d "$1" ]; then
    echo "Error: you must provide a directory as an argument."
    exit 1
fi

for file in "$1"/*.JPG; do
    if [ -f "$file" ]; then
        new_name="${file%.JPG}.jpg"
        mv "$file" "$new_name"
        echo "Renamed: $file -> $new_name"
    fi
done