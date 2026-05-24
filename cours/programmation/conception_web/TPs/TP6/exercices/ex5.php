<?php
  echo ("<h1>Exercice 5</h1>\n");
  for ($i = 1; $i <= 33; $i++) {
    if ($i % 11 == 1) {
      $r = rand(0, 255);
      $g = rand(0, 255);
      $b = rand(0, 255);
      $color = "rgb($r, $g, $b)";
    }
    echo ("<p style='color: $color;'>Ligne numéro $i</p>");
  }
?>