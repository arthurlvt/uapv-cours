<?php

include(__DIR__ . '/etablissements.php');
$file = __DIR__ . '/critiques.json';

if (!file_exists($file)) {
    file_put_contents($file, json_encode([]));
}

if (isset($_GET['delete'])) {
    $id_to_delete = $_GET['delete'];
    $data = json_decode(file_get_contents($file), true);
    
    $filteredData = array_filter($data, function($item) use ($id_to_delete) {
        return $item['id'] != $id_to_delete;
    });

    file_put_contents($file, json_encode(array_values($filteredData), JSON_PRETTY_PRINT));
    header("Location: index.php?page=offers");
    exit();
}

$edit_data = null;
if (isset($_GET['edit'])) {
    $id_to_edit = $_GET['edit'];
    $data = json_decode(file_get_contents($file), true);
    foreach ($data as $item) {
        if ($item['id'] == $id_to_edit) {
            $edit_data = $item;
            break;
        }
    }
}


$restaurants = json_decode(file_get_contents($file), true);
?>

<section class="offers-container">
    <h2 class="section-title">Nos Critiques Gastronomiques</h2>
    
    <div style="text-align: center; margin-bottom: 40px;">
        <a href="#add-form" class="btn-book" style="background: #f49d26; color: black; padding: 12px 25px; border-radius: 5px; text-decoration: none; font-weight: bold;">
            <?php echo isset($_GET['edit']) ? '✎ Modifier la sélection' : '+ Rédiger une critique'; ?>
        </a>
    </div>

    <div class="reviews-grid">
        <?php if (empty($restaurants)): ?>
            <p style="color: #666; text-align: center; grid-column: span 3;">Aucun avis pour le moment.</p>
        <?php else: ?>
            <?php foreach (array_reverse($restaurants) as $resto): ?>
                <div class="review-card" style="position: relative;">
                    
                    <!-- ACTIONS ADMIN (Modifier / Supprimer) -->
                    <div style="position: absolute; top: 10px; right: 10px; z-index: 20; display: flex; gap: 8px;">
                        <a href="index.php?page=offers&edit=<?php echo $resto['id']; ?>#add-form" 
                           title="Modifier"
                           style="background: #f49d26; color: black; width: 30px; height: 30px; border-radius: 50%; text-align: center; line-height: 30px; text-decoration: none; font-size: 14px;">
                           ✎
                        </a>
                        <a href="index.php?page=offers&delete=<?php echo $resto['id']; ?>" 
                           onclick="return confirm('Supprimer définitivement cet avis ?')"
                           title="Supprimer"
                           style="background: #ff4444; color: white; width: 30px; height: 30px; border-radius: 50%; text-align: center; line-height: 30px; text-decoration: none; font-size: 14px; font-weight: bold;">
                           ×
                        </a>
                    </div>

                    <div class="review-image" style="background-image: url('<?php echo $resto['image']; ?>'); height: 200px; background-size: cover; position: relative;">
                        <span class="review-year" style="position: absolute; bottom: 10px; left: 10px; background: rgba(0,0,0,0.7); padding: 3px 8px; border-radius: 4px; font-size: 0.8rem; color: #f49d26;">
                            <?php echo $resto['annee']; ?>
                        </span>
                    </div>
                    
                    <div class="review-details" style="padding: 20px; color: white;">
                        <h3 style="margin: 0; color: #fff;"><?php echo htmlspecialchars($resto['nom']); ?></h3>
                        
                        <div class="review-rating" style="display: flex; align-items: center; gap: 8px; margin: 10px 0;">
                            <span style="color: #f49d26; font-size: 1.2rem;">⭐</span>
                            <span style="font-size: 1.1rem; color: #f49d26; font-weight: bold;">
                                <?php echo number_format($resto['note'], 1); ?> / 5
                            </span>
                        </div>
                        
                        <p class="review-text" style="font-style: italic; color: #bbb; font-size: 0.95rem; line-height: 1.4;">
                            "<?php echo htmlspecialchars($resto['critique']); ?>"
                        </p>
                    </div>
                </div>
            <?php endforeach; ?>
        <?php endif; ?>
    </div>

    <div id="add-form" style="margin-top: 80px; background: #111; padding: 40px; border-radius: 15px; border: 1px solid #333; max-width: 700px; margin-left: auto; margin-right: auto;">
        <h3 style="color: white; margin-bottom: 25px; text-align: center;">
            <?php echo $edit_data ? 'Modifier la critique de ' . $edit_data['nom'] : 'Partager une nouvelle expérience'; ?>
        </h3>
        
        <?php include(__DIR__ . '/form_add.php'); ?>
    </div>
</section>