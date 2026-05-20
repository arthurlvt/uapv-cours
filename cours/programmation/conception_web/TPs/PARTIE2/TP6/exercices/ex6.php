<?php
  echo ("<h1>Exercice 6</h1>\n");
  $tab_prenom = array("Arthur", "Merlin", "Louise", "Guenièvre", 4);
  $tab_prenom1[1] = "A";
  $tab_prenom1[2] = "R";
  $tab_prenom1[3] = "T";
  $tab_prenom1[4] = "H";
  $tab_prenom1[5] = "U";
  $tab_prenom1[6] = "R";

  $tab_prenom2[0] = "M";
  $tab_prenom2[1] = "E";
  $tab_prenom2[2] = "R";
  $tab_prenom2[3] = "L";
  $tab_prenom2[4] = "I";
  $tab_prenom2[5] = "N";

  $tab_prenom3[0] = "L";
  $tab_prenom3[1] = "O";
  $tab_prenom3[2] = "U";
  $tab_prenom3[3] = "I";
  $tab_prenom3[4] = "S";
  $tab_prenom3[5] = "E";

  $tab_prenom4[0] = "G";
  $tab_prenom4[1] = "U";
  $tab_prenom4[2] = "E";
  $tab_prenom4[3] = "N";
  $tab_prenom4[4] = "I";
  $tab_prenom4[5] = "È";
  $tab_prenom4[6] = "V";
  $tab_prenom4[7] = "R";
  $tab_prenom4[8] = "E";

  echo "<p>Tableau Prenoms = ";
  for ($i = 0; $i < count($tab_prenom); $i++) {
    echo $tab_prenom[$i] . " ";
  }
  echo "</p>";
?>