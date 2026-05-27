<?php
include('includes/header.php');

$file = 'includes/critiques.json';

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $current_data = json_decode(file_get_contents($file), true);
    
    $new_entry = [
        "id" => count($current_data) + 1,
        "nom" => $_POST['nom'],
        "type" => $_POST['type'],
        "annee" => intval($_POST['annee']),
        "note" => intval($_POST['note']),
        "image" => $_POST['image'],
        "critique" => $_POST['critique']
    ];

    $current_data[] = $new_entry;
    file_put_contents($file, json_encode($current_data, JSON_PRETTY_PRINT));
    echo "<p style='color:green; text-align:center;'>Critique ajoutée avec succès !</p>";
}
?>

<section class="admin-container" style="padding: 50px; color: white; max-width: 600px; margin: 0 auto;">
    <h2>Ajouter une nouvelle critique</h2>
    <form method="POST" style="display: flex; flex-direction: column; gap: 15px;">
        <input type="text" name="nom" placeholder="Nom du restaurant" required style="padding: 10px;">
        
        <select name="type" style="padding: 10px;">
            <option value="restaurant">Restaurant (Fourchettes)</option>
            <option value="bar">Bar (Verres)</option>
        </select>

        <input type="number" name="annee" placeholder="Année de visite" required style="padding: 10px;">
        
        <select name="note" style="padding: 10px;">
            <option value="1">1 (Bof)</option>
            <option value="2">2 (Pas mal)</option>
            <option value="3">3 (Très bien)</option>
            <option value="4">4 (Exceptionnel)</option>
        </select>

        <input type="text" name="image" placeholder="URL de l'image (Unsplash)" style="padding: 10px;">
        
        <textarea name="critique" placeholder="Ton avis..." rows="5" style="padding: 10px;"></textarea>
        
        <button type="submit" style="padding: 15px; background: #f49d26; border: none; cursor: pointer; font-weight: bold;">Enregistrer la critique</button>
    </form>
</section>

<?php include('includes/footer.php'); ?>