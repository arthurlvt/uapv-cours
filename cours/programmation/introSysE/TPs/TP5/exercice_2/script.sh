#!/bin/bash

create_vignettes() {
    read -p "Entrez le chemin du répertoire de référence pour la galerie d'images: " dir
    if [ ! -d "$dir" ]; then
        echo "Erreur: le chemindoit être le repertoire de référence pour la galerie d'images."
        exit 1
    fi
    cd "$dir"
    mkdir -p vignettes
    for img in *.jpg; do
        convert "$img" -resize 128x128 "vignettes/vignette_$img"
    done
}

create_vignettes

create_page() {
    cat <<EOF > index.html
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Galerie d'images</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            margin: 0;
            padding: 20px;
        }
        .gallery {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
        }
        .gallery img {
            width: 128px;
            height: 128px;
            object-fit: cover;
            border: 2px solid #ccc;
            border-radius: 4px;
            transition: transform 0.2s;
        }
        .gallery img:hover {
            transform: scale(1.1);
            border-color: #777;
        }
    </style>
</head>
<body>
    <h1>Galerie d'images</h1>
    <div class="gallery">
EOF
    for vignette in vignettes/*.jpg; do
        original="${vignette#vignettes/}"
        cat <<EOF >> index.html
        <a href="$dir/vignettes/$original" target="_blank">
            <img src="$dir/$vignette" alt="$original">
        </a>
EOF
    done
    cat <<EOF >> index.html
    </div>
</body>
</html>
EOF

mv index.html ..
}

create_page