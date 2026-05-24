<?php
  echo ("<h1>Exercice 3</h1>\n");
  setlocale(LC_TIME, "fr_FR_utf8","fra");
  echo (strftime ("<h4>Ici, nous sommes le %A %d %B, "));
  echo (strftime ("il est %H h %M min %S sec.</h4>\n"));
  $timestamp = time() - (2 * 24 * 60 * 60);
  echo (strftime ("<h4>Il y a deux jours, nous étions le %A %d %B, "));
?>