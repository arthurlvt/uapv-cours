#!/bin/bash

is_integer() {
    [[ "$1" =~ ^[0-9]+$ ]]
}

get_number_i() {
    if [ -f "$1" ]; then
        basename "$1" | cut -d '.' -f2
    fi
}

get_max_number() {
    if [ -d "$1" ]; then
        max=0
        for file in "$1"/*.tar.gz; do
            if [ -f "$file" ]; then
                i=$(get_number_i "$file")
                if is_integer "$i"; then
                    if [ "$i" -gt "$max" ]; then
                        max=$i
                    fi
                fi
            fi
        done
        echo "Le fichier avec le plus grand i devant .tar.gz est $max"
    else
        echo "Le chemin spécifié n'est pas un répertoire."
    fi
}

rotation_log() {
    if [ -f "test.0.tar.gz" ]; then
        mv "test.0.tar.gz" "$1/"
        echo "Déplacé test.0.tar.gz vers $1/"
    fi
        max=0
    for file in "$1"/*.tar.gz; do
        if [ -f "$file" ]; then
            i=$(get_number_i "$file")
            if is_integer "$i"; then
                if [ "$i" -gt "$max" ]; then
                    max=$i
                fi
            fi
        fi
    done
    for ((i = max; i >= 0; i--)); do
        old_file="$1/nom.$i.tar.gz"
        if [ -f "$old_file" ]; then
            new_name="$1/nom.$((i+1)).tar.gz"
            mv "$old_file" "$new_name"
            echo "Renommé nom.$i.tar.gz en nom.$((i+1)).tar.gz"
        fi
    done 
    echo "Rotation des logs terminée."
}

read -p "Entrez le chemin du répertoire : " user_dir
get_max_number "$user_dir"

read -p "Voulez-vous faire une rotation des logs ? (y/n) " answer
if [[ "$answer" == "y" ]]; then
    rotation_log "$user_dir"
else
    echo "Rotation des logs annulée."
fi