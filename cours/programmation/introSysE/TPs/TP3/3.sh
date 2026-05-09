#!/bin/bash
# check if a number is greater than 10 and less than 20
if [ "$1" -gt "10" && "$1" -lt "20" ]; then
    echo "Le nombre est compris entre 10 et 20."
else
    echo "Le nombre n'est pas compris entre 10 et 20."
fi