#!/bin/bash
#
if [ $# -eq 0 ]; then
    echo "Usage: $0 prenom"
    exit 1
fi
prenom=$1
for i in {1..99}; do
    echo "$prenom" >> prenom.txt
done