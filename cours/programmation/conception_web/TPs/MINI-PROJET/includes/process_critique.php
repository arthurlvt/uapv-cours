<?php
include(__DIR__ . '/etablissements.php');

$file = __DIR__ . '/critiques.json';
if (!file_exists($file)) {
    file_put_contents($file, json_encode([]));
}

$json = file_get_contents($file);
$data = json_decode($json, true);
if (!is_array($data)) {
    $data = [];
}

if (isset($_POST['add_resto']) || isset($_POST['update_resto'])) {
    $nom = $_POST['nom_selection'];

    if (!isset($liste_etablissements[$nom])) {
        header("Location: /mon-projet/index.php?page=offers&error=invalid_place");
        exit();
    }
    
    $new_entry = [
        "id" => isset($_POST['id']) ? $_POST['id'] : time(),
        "nom" => $nom,
        "type" => $liste_etablissements[$nom]['type'],
        "annee" => intval($_POST['annee']),
        "note" => floatval($_POST['note']),
        "image" => $liste_etablissements[$nom]['image'],
        "critique" => $_POST['critique']
    ];

    if (isset($_POST['update_resto'])) {
        foreach ($data as $key => $item) {
            if ($item['id'] == $_POST['id']) {
                $data[$key] = $new_entry;
                break;
            }
        }
    } else {
        $data[] = $new_entry;
    }

    file_put_contents($file, json_encode(array_values($data), JSON_PRETTY_PRINT), LOCK_EX);
    header("Location: /mon-projet/index.php?page=offers");
    exit();
}

header("Location: /mon-projet/index.php?page=offers");
exit();