<?php
// lecture des données du fichier data/movies.txt avec des films au format titre|réalisateur|genre|annee|classement
$movies = [];
$file = fopen("./data/movies.txt", "r");
if ($file) {
    while (($line = fgets($file)) !== false) {
        $movie = explode("|", trim($line));
        $movies[] = [
            "title" => $movie[0],
            "director" => $movie[1],
            "genre" => $movie[2],
            // extraire l'année de la date de sortie du film
            "year" => substr($movie[3], 0, 4),
            "rating" => $movie[4]
        ];
        echo "</br>";
    }
    fclose($file);
} else {
    echo "Erreur lors de l'ouverture du fichier.";
    exit;
}

// tableau d'affichage des films
echo "<h1>Liste des films <strong>(Version 1)</strong></h1>";
echo "<table border='1'>";
echo "<tr><th>Titre</th><th>Réalisateur</th><th>Genre</th><th>Année</th><th>Classement</th></tr>";
foreach ($movies as $movie) {
    echo "<tr>";
    echo "<td>" . htmlspecialchars($movie["title"]) . "</td>";
    echo "<td>" . htmlspecialchars($movie["director"]) . "</td>";
    echo "<td>" . htmlspecialchars($movie["genre"]) . "</td>";
    echo "<td>" . htmlspecialchars($movie["year"]) . "</td>";
    echo "<td>" . htmlspecialchars($movie["rating"]) . "</td>";
    echo "</tr>";
}
echo "</table>";
// style du tableau + faire en sorte que le tableau soit en haut de la page
echo "<style>
    table {
        width: 100%;
        border-collapse: collapse;
        margin-top: 20px;
    }
    th, td {
        padding: 10px;
        text-align: left;
    }
    th {
        background-color: #f2f2f2;
    }
    tr:nth-child(even) {
        background-color: #f9f9f9;
    }
</style>";

// version 2 : version formulaire deroulant l'utilisateur selectionne le film et affiche les details du film selectionne
echo "<h1>Liste des films <strong>(Version 2)</strong></h1>";
echo "<form method='post'>";
echo "<label for='movie'>Sélectionnez un film :</label>";
echo "<select name='movie' id='movie'>";
foreach ($movies as $index => $movie) {
    echo "<option value='" . $index . "'>" . htmlspecialchars($movie["title"]) . "</option>";
}
echo "</select>";
echo "<input type='submit' value='Afficher les détails'>";
echo "</form>";
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $selectedMovieIndex = $_POST["movie"];
    if (isset($movies[$selectedMovieIndex])) {
        $selectedMovie = $movies[$selectedMovieIndex];
        echo "<h2>Détails du film sélectionné :</h2>";
        echo "<p><strong>Titre :</strong> " . htmlspecialchars($selectedMovie["title"]) . "</p>";
        echo "<p><strong>Réalisateur :</strong> " . htmlspecialchars($selectedMovie["director"]) . "</p>";
        echo "<p><strong>Genre :</strong> " . htmlspecialchars($selectedMovie["genre"]) . "</p>";
        echo "<p><strong>Année :</strong> " . htmlspecialchars($selectedMovie["year"]) . "</p>";
        echo "<p><strong>Classement :</strong> " . htmlspecialchars($selectedMovie["rating"]) . "</p>";
    } else {
        echo "<p>Film sélectionné invalide.</p>";
    }
}
?>