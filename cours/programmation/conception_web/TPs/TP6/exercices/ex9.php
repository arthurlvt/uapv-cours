<?php
$tab = array("C", "E", "R", "I", 4);
// boucle qui met un tiret entre chaque lettre du tableau mais qui affiche pas "4"
for ($i = 0; $i < count($tab); $i++) {
    if ($tab[$i] !== 4) {
        echo $tab[$i];
        if ($i < count($tab) - 1) {
            echo "-";
        }
    }
}
?>