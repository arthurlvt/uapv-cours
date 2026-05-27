<?php
// On s'assure que la liste est disponible pour le CTA en bas de page
include('includes/etablissements.php');
?>

<section class="presentation-section" style="color: white; padding: 40px 20px; max-width: 1000px; margin: 0 auto; line-height: 1.6;">
    
    <!-- Header de la page -->
    <div style="text-align: center; margin-bottom: 60px;">
        <h2 style="font-size: 3rem; margin-bottom: 20px; font-weight: bold;">
            L'Art de Bien <span style="color: #f49d26;">Choisir</span>
        </h2>
        <p style="color: #888; font-size: 1.2rem; max-width: 800px; margin: 0 auto;">
            RestoMood n'est pas qu'un simple annuaire. C'est votre boussole gastronomique pour transformer chaque repas en une expérience mémorable[cite: 10].
        </p>
    </div>

    <!-- Section Concept : Image + Texte -->
    <div style="display: flex; align-items: center; gap: 40px; margin-bottom: 80px; flex-wrap: wrap;">
        <div style="flex: 1; min-width: 300px;">
            <img src="https://images.unsplash.com/photo-1559339352-11d035aa65de?auto=format&fit=crop&q=80&w=800" 
                 alt="Ambiance RestoMood" 
                 style="width: 100%; border-radius: 15px; border: 1px solid #333; box-shadow: 0 10px 30px rgba(0,0,0,0.5);">
        </div>
        <div style="flex: 1; min-width: 300px;">
            <h3 style="color: #f49d26; font-size: 1.8rem; margin-bottom: 15px;">Notre Vision</h3>
            <p style="margin-bottom: 15px;">
                Dans un monde saturé d'options, nous croyons en la qualité plutôt qu'en la quantité. Chaque établissement listé sur RestoMood a été rigoureusement sélectionné pour son atmosphère, son service et, bien sûr, sa cuisine[cite: 3, 10].
            </p>
            <p>
                Que vous cherchiez le raffinement du <strong>Le Bellefeuille</strong> ou l'authenticité d'une <strong>Trattoria Gusto</strong>, nous vous aidons à trouver la table qui correspond à votre "Mood" du moment[cite: 3, 10].
            </p>
        </div>
    </div>

    <!-- Section "Comment ça marche" -->
    <div style="background: #111; padding: 40px; border-radius: 20px; border: 1px solid #222; margin-bottom: 60px;">
        <h3 style="text-align: center; margin-bottom: 40px; font-size: 1.8rem;">Votre Guide Culinaire</h3>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 30px;">
            
            <div style="text-align: center;">
                <div style="font-size: 2.5rem; margin-bottom: 10px;">🔍</div>
                <h4 style="color: #f49d26; margin-bottom: 10px;">Explorez</h4>
                <p style="font-size: 0.9rem; color: #aaa;">Naviguez parmi nos sélections exclusives de restaurants et bars[cite: 3, 7].</p>
            </div>

            <div style="text-align: center;">
                <div style="font-size: 2.5rem; margin-bottom: 10px;">✍️</div>
                <h4 style="color: #f49d26; margin-bottom: 10px;">Critiquez</h4>
                <p style="font-size: 0.9rem; color: #aaa;">Partagez vos impressions et notez vos expériences en quelques clics[cite: 9, 10].</p>
            </div>

            <div style="text-align: center;">
                <div style="font-size: 2.5rem; margin-bottom: 10px;">🌟</div>
                <h4 style="color: #f49d26; margin-bottom: 10px;">Partagez</h4>
                <p style="font-size: 0.9rem; color: #aaa;">Aidez la communauté à découvrir les pépites de la gastronomie locale[cite: 10].</p>
            </div>

        </div>
    </div>

    <!-- Call to Action -->
    <div style="text-align: center; padding: 40px; border-top: 1px solid #222;">
        <h3 style="margin-bottom: 20px;">Prêt à découvrir votre prochaine table ?</h3>
        <a href="index.php?page=offers" class="btn-book" 
           style="background: #f49d26; color: black; padding: 15px 40px; border-radius: 50px; text-decoration: none; font-weight: bold; display: inline-block; transition: 0.3s;">
           Voir les Critiques
        </a>
    </div>

</section>