#!/bin/bash

# Un script qui éxécute un programme selon le nombre entier passé en argument (de 1 à 18)

if [ "$#" -ne 1 ]; then 
    echo "Usage: $0 <number>"
    exit 1
fi

if [ "$#" -ne 3 ]; then
    echo "Error: You must provide exactly 3 arguments: <executable> <input_file> <expected_output_file>"
    exit 1
fi