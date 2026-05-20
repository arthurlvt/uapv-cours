<?php
  // Exercice 7 : tableaux associatifs
  $tab_site["instagram"] = "https://www.instagram.com/";
  $tab_site["github"] = "https://github.com/";
  $tab_site["netflix"] = "https://www.netflix.com/";
  $tab_site["spotify"] = "https://www.spotify.com/";
  // Sites Fetiches
  $tab_sites_fetiches = array(
    "Instagram" => $tab_site["instagram"],
    "GitHub" => $tab_site["github"],
    "Netflix" => $tab_site["netflix"],
    "Spotify" => $tab_site["spotify"]
  );
  // création d'une page HTML avec les liens
  echo "<h2>Mes sites préférés</h2>";
  echo "<ul>";
  foreach ($tab_sites_fetiches as $site => $url) {
    echo "<li><a href='$url' target='_blank'>$site</a></li>";
  }
  echo "</ul>";
?>