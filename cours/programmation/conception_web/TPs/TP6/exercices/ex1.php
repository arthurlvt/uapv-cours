<?php
  $saut = "<br>";
  echo "<h1>Exercice 1</h1>" . $saut;
  $i = 58;
  $j = 4;
  echo "Le produit de $i et $j est égal à " . ($i * $j) . $saut;
  $k = $i;
  $i = $j;
  $j = $k;
  echo "Après échange, i = $i et j = $j" . $saut;
  echo "Le nouveau produit de $i et $j est égal à " . ($i * $j) . $saut;
  echo "Le quotient de $i et $j est égal à " . ($i / $j) . $saut;
  echo "Le reste de la division de $i par $j est égal à " . ($i % $j);
?>