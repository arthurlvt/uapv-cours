#!/bin/bash
# check if a number is positive, negative or null
if [ "$1" -lt "0"]; then
    echo "Le nombre est nul"
else [ "$1" -gt "0" ]; then
    echo "Le nombre est positif."
else 
    echo "Le nombre est négatif."
fi