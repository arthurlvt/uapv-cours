<?php
    // Affichage des erreurs pour le débug
    ini_set('display_errors', 1);
    error_reporting(E_ALL);

    // 1. Inclure le header
    include('includes/header.php');

    $page = $_GET['page'] ?? 'main';

    echo '<main class="content-area">';

    // 2. Logique d'affichage
    if ($page === 'main') {
        include('includes/features.php');
        include('includes/stats.php');
    } 
    elseif ($page === 'presentation') {
        include('includes/presentation.php');
    } 
    elseif ($page === 'offers' || $page === 'offres') {
        include('includes/offers.php');
    }

    echo '</main>';
    
    include('includes/footer.php');
?>