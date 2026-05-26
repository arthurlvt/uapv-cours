<?php
// On récupère les données si on est en mode édition
$is_editing = isset($edit_data);
$action_name = $is_editing ? 'update_resto' : 'add_resto';
?>

<form method="POST" action="includes/process_critique.php" style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px;">
    <!-- Champ caché pour l'ID si on modifie -->
    <?php if($is_editing): ?>
        <input type="hidden" name="id" value="<?php echo $edit_data['id']; ?>">
    <?php endif; ?>

    <select name="nom_selection" required style="grid-column: span 2; padding: 10px;">
        <?php foreach ($liste_etablissements as $nom => $infos): ?>
            <option value="<?php echo $nom; ?>" <?php if($is_editing && $edit_data['nom'] == $nom) echo 'selected'; ?>>
                <?php echo $nom; ?>
            </option>
        <?php endforeach; ?>
    </select>

    <input type="number" name="annee" value="<?php echo $is_editing ? $edit_data['annee'] : ''; ?>" placeholder="Année" required style="padding: 10px;">
    <input type="number" name="note" value="<?php echo $is_editing ? $edit_data['note'] : ''; ?>" step="0.5" min="1" max="5" placeholder="Note (1-5)" required style="padding: 10px;">

    <textarea name="critique" placeholder="Votre critique..." style="grid-column: span 2; padding: 10px;" rows="3"><?php echo $is_editing ? $edit_data['critique'] : ''; ?></textarea>
    
    <button type="submit" name="<?php echo $action_name; ?>" style="grid-column: span 2; background: #f49d26; padding: 15px; font-weight: bold; cursor: pointer;">
        <?php echo $is_editing ? 'Mettre à jour la critique' : 'Publier la critique'; ?>
    </button>
    
    <?php if($is_editing): ?>
        <a href="index.php?page=offers" style="grid-column: span 2; text-align: center; color: #ccc;">Annuler la modification</a>
    <?php endif; ?>
</form>