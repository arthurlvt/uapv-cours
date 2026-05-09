#!/bin/bash
# check which directory contains the most number of files
if [ -d "$1" ] && [ -d "$2" ]; then
    countDir1=$(ls -1q "$1" | wc -l)
    countDir2=$(ls -1q "$2" | wc -l)

    if [ $countDir1 -gt $countDir2 ]; then
        echo "Directory '$1' contains more files ($countDir1) than '$2' ($countDir2)."
    elif [ $countDir2 -gt $countDir1 ]; then
        echo "Directory '$2' contains more files ($countDir2) than '$1' ($countDir1)."
    else
        echo "Both directories contain the same number of files ($count1)."
    fi
else
     echo "Both arguments must be valid directories."
fi