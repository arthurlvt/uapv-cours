#!/bin/bash
# check if document is a file or a directory
if [ -f "$1" ]; then
    echo "The document is a file."
elif [ -d "$1" ]; then
    echo "The document is a directory."
else
    echo "The document is neither a file nor a directory."
fi