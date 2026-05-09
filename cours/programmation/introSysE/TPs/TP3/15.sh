#!bin/bash

if [ $# -eq 0 ]; then
    echo "Usage: $0 <directory>"
    exit 1
fi

if [ ! -d "$1" ]; then
    echo "Error: $1 is not a directory"
    exit 1
fi

num_files=$(find "$1" -type f | wc -l)
num_dirs=$(find "$1" -type d | wc -l) 
echo "Number of files: $num_files"
echo "Number of directories: $((num_dirs - 1))" # on soustrait 1 pour ne pas compter le répertoire lui-même