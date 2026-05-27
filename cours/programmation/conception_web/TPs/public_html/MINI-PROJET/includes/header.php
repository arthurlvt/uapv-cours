<?php
    $currentPage = $_GET['page'] ?? 'main';
    if ($currentPage === 'presentation') {
        $btnText = "Accueil";
        $btnLink = "index.php?page=main";
        $btnStyle = "";
    } else {
        $btnText = "Présentation";
        $btnLink = "index.php?page=presentation";
        $btnStyle = "";
    }
?>
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>RestoMood</title>
    <link rel="stylesheet" href="assets/style.css">
    <link rel="icon" type="image/png" href="../assets/logo.png">
</head>
<body>

<header>
    <div class="header-left">
        <img src="assets/logo.png" alt="RestoMood" class="logo">
        <h1 class="title"><span class="cinema">Resto</span><span class="mood">Mood</span></h1>
    </div>

    <nav class="header-center">
        <ul class="nav-links">
            <li><a href="<?php echo $btnLink; ?>" class="nav-link"><?php echo $btnText; ?></a></li>
            <li><a href="index.php?page=offers" class="nav-link">Offres</a></li>
        </ul>
    </nav>
</header>
<?php 
    if ($currentPage === 'main') {
        include('includes/whos.php');
        
        echo '<section class="slider-container">';
        include('includes/main.php');
        echo '</section>';
    } 
?>