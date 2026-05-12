#!/bin/bash
# check if a number is an int and return 1 if yes, 0 if not
if [[ "$1" =~ ^-?[0-9]+$ ]]; then
    echo "1"
else
    echo "0"
fi