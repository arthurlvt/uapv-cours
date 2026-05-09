#!/bin/bash
# check if a number is less than or equal to 10
if [ "$1" -le "10" ]; then
    echo "Le premier paramètre est inférieur ou égal à 10."
else
    echo "Le premier paramètre est supérieur à 10."
fi