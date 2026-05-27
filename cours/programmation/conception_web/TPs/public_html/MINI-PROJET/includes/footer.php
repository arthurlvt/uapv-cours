<footer style="margin-top: 50px; padding: 40px 0; border-top: 1px solid #222; text-align: center; color: #666;">
    <p>&copy; <?php echo date('Y'); ?> RestoMood - Design par Arthur LOUVET</p>
</footer>

<script>
    // 1. Force l'affichage de la page au chargement
    window.addEventListener('load', () => {
        document.body.classList.add('page-loaded');
    });

    // Sécurité : au cas où le chargement reste bloqué
    setTimeout(() => {
        if (!document.body.classList.contains('page-loaded')) {
            document.body.classList.add('page-loaded');
            document.body.style.opacity = "1";
        }
    }, 1500);

    // 2. Animation de sortie
    document.querySelectorAll('nav a, .nav-link').forEach(link => {
        link.addEventListener('click', function(e) {
            const href = this.getAttribute('href');

            // On déclenche la transition si c'est un lien interne et pas une ancre (#)
            if (href && !href.startsWith('#') && (href.includes('index.php') || href.includes('page='))) {
                
                // On vérifie qu'il n'y a pas de confirmation de suppression (pour ne pas bloquer le bouton supprimer)
                if (!this.onclick || !this.onclick.toString().includes('confirm')) {
                    
                    e.preventDefault();
                    
                    document.body.classList.remove('page-loaded');
                    document.body.style.opacity = "0";
                    document.body.style.transform = "translateY(-10px)";

                    setTimeout(() => {
                        window.location.href = href;
                    }, 400);
                }
            }
        });
    });
</script>