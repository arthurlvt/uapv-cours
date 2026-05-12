#!/bin/bash
#shebang

infos_etudiants() {
    for lines in $(cat $1); do
        echo "Numéro UAPV: $(cut -f1 -d"," <<< $lines)"
        echo "Nom: $(cut -f2 -d"," <<< $lines)"
        echo "Prénom: $(cut -f3 -d"," <<< $lines)"
        echo "Matière Prime: $(cut -f4 -d"," <<< $lines)"
        echo "Moyenne: $(cut -f5 -d"," <<< $lines)"
        echo "-----------------------------"
    done
}
infos_etudiants "notes.txt"


moyenne_generale() {
    total=0
    count=0
    for lines in $(cat $1); do
        total=$(echo "$total + $(cut -f5 -d"," <<< $lines)" | bc)
        count=$((count + 1))
    done
    echo "Moyenne générale: $(echo "scale=2; $total / $count" | bc)"
}
moyenne_generale "notes.txt"


convertir_xml() {
    echo "<students>"
    for lines in $(cat $1); do
        echo "  <student>"
        echo "    <num_uapv>$(cut -f1 -d"," <<< $lines)</num_uapv>"
        echo "    <name>$(cut -f2 -d"," <<< $lines)</name>"
        echo "    <surname>$(cut -f3 -d"," <<< $lines)</surname>"
        echo "    <course>$(cut -f4 -d"," <<< $lines)</course>"
        echo "    <note>$(cut -f5 -d"," <<< $lines)</note>"
        echo "  </student>"
    done
    echo "</students>"
}
convertir_xml "notes.txt" > notes.xml