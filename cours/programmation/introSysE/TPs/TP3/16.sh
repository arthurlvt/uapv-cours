#!bin/bash

if [ ! -d "$1" ]; then
    echo "Error: you must provide a directory as an argument."
    exit 1
fi

for file in "$1"/*.txt; do
    if [ -f "$file" ]; then
        rm "$file"
        echo "Deleted: $file"
    fi
done