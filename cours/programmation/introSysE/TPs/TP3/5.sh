#!/bin/bash
# make sum and diff of two numbers
if [ "$1" && "$2" ]; then
    sum=$(($1 + $2))
    diff=$(($1 - $2))
    echo "Sum: $sum"
    echo "Difference: $diff"
else
    echo "Please provide two positive numbers as arguments."
fi