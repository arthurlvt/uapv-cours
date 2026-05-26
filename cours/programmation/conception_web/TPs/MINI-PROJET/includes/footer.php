<footer style="margin-top: 50px; padding: 40px 0; border-top: 1px solid #222; text-align: center; color: #666;">
    <p>&copy; <?php echo date('Y'); ?> RestoMood - Design par Arthur LOUVET</p>
</footer>

<script>
    window.addEventListener('load', () => {
        document.body.classList.add('page-loaded');
    });

    setTimeout(() => {
        if (!document.body.classList.contains('page-loaded')) {
            document.body.classList.add('page-loaded');
            document.body.style.opacity = "1";
        }
    }, 1500);

    document.querySelectorAll('nav a, .nav-link').forEach(link => {
        link.addEventListener('click', function(e) {
            const href = this.getAttribute('href');

            if (href && !href.startsWith('#') && (href.includes('index.php') || href.includes('page='))) {
                
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