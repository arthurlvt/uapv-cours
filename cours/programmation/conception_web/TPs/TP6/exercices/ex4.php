<?php
  echo ("<h1>Exercice 4</h1>\n");
  $couleurs = ["red", "green", "blue", "orange", "purple", "pink"];
  $index = (time() / 40) % count($couleurs);
  $couleur = $couleurs[$index];
  echo ("<p style='color: $couleur;'>Ce texte change de couleur toutes les 40 secondes.</p>");
?>