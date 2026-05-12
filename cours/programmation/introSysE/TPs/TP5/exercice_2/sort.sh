#!/bin/bash
infos_fichier() {
    if [ -d "$1" ] && [ "$(basename "$1")" = "*.mp3" ]; then
        echo "-- Infos sur la galerie de Musiques --"
        for file in "$1"/*.mp3; do
            if [ -f "$file" ]; then
                # Fichier au format titre Source/Year-Genre-Album-Titre.mp3
                echo "Fichier ID#$file"
                echo "Source: $(basename "$file" | cut -d'/' -f1)"
                $source = $(basename "$file" | cut -d'/' -f1)
                echo "Année: $(basename "$file" | cut -d'-' -f2)"
                $year = $(basename "$file" | cut -d'-' -f2)
                if [ ! -d "$(basename "$file" | cut -d'-' -f2)" ]; then
                    mkdir "$(basename "$file" | cut -d'-' -f2)"
                fi
                echo "Genre: $(basename "$file" | cut -d'-' -f3)"
                $genre = $(basename "$file" | cut -d'-' -f3)
                if [ ! -d "$(basename "$file" | cut -d'-' -f3)" ]; then
                    mkdir "$(basename "$file" | cut -d'-' -f3)"
                fi
                echo "Album: $(basename "$file" | cut -d'-' -f4)"
                $album = $(basename "$file" | cut -d'-' -f4)
                if [ ! -d "$(basename "$file" | cut -d'-' -f4)" ]; then
                    mkdir "$(basename "$file" | cut -d'-' -f4)"
                fi
                echo "Titre: $(basename "$file" | cut -d'-' -f5 | cut -d'.' -f1)"
                $title = $(basename "$file" | cut -d'-' -f5 | cut -d'.' -f1)
                echo "-----------------------------"
                mv "$file" "$(basename "$file" | cut -d'-' -f5 | cut -d'.' -f1).mp3"
                mv "$(basename "$file" | cut -d'-' -f5 | cut -d'.' -f1).mp3" "$(basename "$file" | cut -d'-' -f2)/"
                mv "$(basename "$file" | cut -d'-' -f2)/$(basename "$file" | cut -d'-' -f5 | cut -d'.' -f1).mp3" "$(basename "$file" | cut -d'-' -f3)/"
                mv "$(basename "$file" | cut -d'-' -f3)/$(basename "$file" | cut -d'-' -f5 | cut -d'.' -f1).mp3" "$(basename "$file" | cut -d'-' -f4)/"
            fi
        done
    else
        echo "Erreur: $1 n'est pas un répertoire valide ou ne contient pas de fichiers MP3."
    fi
}