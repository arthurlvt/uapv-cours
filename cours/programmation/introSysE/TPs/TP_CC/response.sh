#!bin/bash

# <---------------------------------- EXERCICE 1 ---------------------------------->
1) cat students.txt | head -2
2) cat students.txt | head -n 2
3) cat students.txt | cut -f1 -d","
4) cat students.txt | grep -e"admin" | cut -f2-3 -d","
5) cat students.txt | cut -f3 -d"," | grep -e"i" # sort -u à mettre si on veut éviter 2x Claire
6) cat students.txt | cut -f2 -d"," | grep -e"^D"
7) cat students.txt | cut -f2 -d"," | grep -e"^D" -e"^M"
8) cat students.txt | cut -f2 -d"," | grep -e"^.f" -e"^.r"
9) cat students.txt | cut -f3 -d","
10) cat students.txt | grep -e"admin" | cut -f1-3,4 -d","
11) calcul de la moyenne :

average_salary() {
	$total = 0 
	$count= 0
	for salary in "$file" {
		
}
average_salary() "students.txt"

12)

conversion_csv() {
	echo "<utilisateurs>"
	for dir in "$dir"; do
		echo "	<utilisateur>"
		echo "		<id>$(cat $dir | head -1 | cut -f1 -d",")</id>"
		echo "		<nom>$(cat $dir | head - | cut -f2 -d",")</nom>"
		echo "		<prenom>$(cat $dir | head -1 | cut -f3 -d",")</prenom>"
		echo "		<role>$(cat $dir | head -1 | cut -f4 -d",")</role>"		
		echo "		<annee>$(cat $dir | head -1 | cut -f5 -d",")</annee>"
		echo "	</utilisateur>"
	done
	echo "</utilisateurs>"	
}
read -p "Entrez un répertoire de référence: " dir
conversion_csv "dir"

# <---------------------------------- EXERCICE 2 ---------------------------------->

get_client() {
	echo "Nom du client: $(basename $1 | cut -f3 -d"-")"
}
get_titre() {
	echo "Titre: $(basename $1 | cut -f5 -d"-")"
}
get_annee() {
	echo "Annee: $(basename $1 | cut -f2 -d"-")"
}
get_mission-type() {
	echo "Type de Mission: $(basename $1 | cut -f4 -d"-")"
}
get_extension() {
	echo "Type de fichier: $(basename $1 | cut -f5 -d".")"
}

read -p "Entrez une source" file
read -p "Entrez une destination" dest
$client = $(get_client "file")
$titre = $(get_titre "file")
$annee = $(get_annee "file")
$type = $(get_mission_type "file")
$ext = $(get_extension "file")


get_infos() {
	if [ "$#" -eq 2 ]; then
		for file in "$file"; do
			echo "----fichier $(file) -----"
			echo "Client: $(client)"
			echo "Titre: $(titre)"
			echo "Annee: $(annee)"
			echo "Type de Mission: $(type)"
			echo "Extension: $(ext)"
			echo "------------------------"
			if [ $(basename "$file") -eq "*.pdf") ] && [ $(basename "$file") -eq "*.txt" ] && [ $(basename "$file") -eq "*.docx" ]; then
				echo "fichier ignoré"
				$file = $file + 1
			fi
		done
	else
		echo "Erreur, vous n'avez pas passé 2 arguments en paramètres : <file> <destination>"
	fi
}

read -p "Quel fichier source ? " file
get_infos() "file"





























