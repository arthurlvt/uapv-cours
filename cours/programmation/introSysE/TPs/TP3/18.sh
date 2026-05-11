#!bin/bash
if [ ! -d "$1" ]; then
    echo "Error: you must provide a directory as an argument."
    exit 1
fi