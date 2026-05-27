<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="author" content="Arthur LOUVET">
    <title>RestoMood - Trouvez la meilleure table</title>
    <link rel="stylesheet" href="assets/style.css">
</head>
<body>
    <main class="main-content">
        <div class="slider">
            <!-- Slide 1 : Gastronomie -->
            <div class="slide active" style="background-image: url('https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?auto=format&fit=crop&q=80&w=1600');">
                <div class="hero-text-overlay">
                    <p class="chef-name">Chef Julien Dumas</p>
                    <h2 class="resto-name">Le Bellefeuille</h2>
                    <p class="description">Une expérience sensorielle unique au cœur de Paris, où la nature s'invite à votre table à travers une cuisine végétale et iodée.</p>
                    <div class="hero-buttons">
                        <a href="#" class="btn-book">Réserver une table</a>
                        <span class="price-range">€€€€</span>
                    </div>
                </div>
            </div>

            <!-- Slide 2 : Italien -->
            <div class="slide" style="background-image: url('https://images.unsplash.com/photo-1559339352-11d035aa65de?auto=format&fit=crop&q=80&w=1600');">
                <div class="hero-text-overlay">
                    <p class="chef-name">La Dolce Vita</p>
                    <h2 class="resto-name">Trattoria Gusto</h2>
                    <p class="description">Les saveurs authentiques de l'Italie. Pâtes fraîches maison et sélection de vins fins dans une ambiance chaleureuse et tamisée.</p>
                    <div class="hero-buttons">
                        <a href="#" class="btn-book">Découvrir la carte</a>
                        <span class="price-range">€€</span>
                    </div>
                </div>
            </div>

            <!-- Slide 3 : Japonais -->
            <div class="slide" style="background-image: url('https://images.unsplash.com/photo-1579027989536-b7b1f875659b?auto=format&fit=crop&q=80&w=1600');">
                <div class="hero-text-overlay">
                    <p class="chef-name">Art de la Découpe</p>
                    <h2 class="resto-name">Sakura Sushi Bar</h2>
                    <p class="description">L'excellence du Japon. Des produits d'une fraîcheur absolue préparés sous vos yeux par nos maîtres sushis renommés.</p>
                    <div class="hero-buttons">
                        <a href="#" class="btn-book">Réserver au comptoir</a>
                        <span class="price-range">€€€</span>
                    </div>
                </div>
            </div>
            <!-- Slide 5 : Méditerranéen / Bord de mer -->
            <div class="slide" style="background-image: url('https://images.unsplash.com/photo-1515276427842-f85802d514a2?auto=format&fit=crop&q=80&w=1600');">
                <div class="hero-text-overlay">
                    <p class="chef-name">Saveurs du Sud</p>
                    <h2 class="resto-name">La Villa Azur</h2>
                    <p class="description">Évadez-vous le temps d'un dîner avec une vue imprenable sur la mer et une cuisine inspirée des rivages de la French Riviera.</p>
                    <div class="hero-buttons">
                        <a href="#" class="btn-book">Voir la terrasse</a>
                        <span class="price-range">€€€€</span>
                    </div>
                </div>
            </div>

            <!-- Slide 6 : Steakhouse de Luxe -->
            <div class="slide" style="background-image: url('https://images.unsplash.com/photo-1544025162-d76694265947?auto=format&fit=crop&q=80&w=1600');">
                <div class="hero-text-overlay">
                    <p class="chef-name">Maître Grilleur</p>
                    <h2 class="resto-name">Black Angus Club</h2>
                    <p class="description">Pour les amateurs de viandes d'exception. Des découpes rares maturées 45 jours et grillées au charbon de bois japonais.</p>
                    <div class="hero-buttons">
                        <a href="#" class="btn-book">Réserver</a>
                        <span class="price-range">€€€</span>
                    </div>
                </div>
            </div>

            <!-- Dots -->
            <div class="slider-dots">
                <div class="dot active" onclick="setSlide(0)"></div>
                <div class="dot" onclick="setSlide(1)"></div>
                <div class="dot" onclick="setSlide(2)"></div>
                <div class="dot" onclick="setSlide(3)"></div>
                <div class="dot" onclick="setSlide(4)"></div>
            </div>
        </div>
    </main>
    <script>
        const slides = document.querySelectorAll('.slide');
        const dots = document.querySelectorAll('.dot');
        let currentIndex = 0;
        let autoPlay = setInterval(nextSlide, 6000);

        function showSlide(index) {
            slides.forEach(s => s.classList.remove('active'));
            dots.forEach(d => d.classList.remove('active'));

            slides[index].classList.add('active');
            dots[index].classList.add('active');
        }

        function nextSlide() {
            currentIndex = (currentIndex + 1) % slides.length;
            showSlide(currentIndex);
        }

        function setSlide(index) {
            clearInterval(autoPlay); 
            currentIndex = index;
            showSlide(currentIndex);
            autoPlay = setInterval(nextSlide, 6000); 

        }
    </script>
</body>
</html>