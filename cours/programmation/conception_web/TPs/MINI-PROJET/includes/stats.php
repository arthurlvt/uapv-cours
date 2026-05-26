<section class="statistics-section" style="padding: 80px 20px; background: #000; border-top: 1px solid #111;">
    <div class="stats-container" style="display: flex; justify-content: space-around; max-items: center; max-width: 1100px; margin: 0 auto; flex-wrap: wrap; gap: 20px;">
        
        <!-- Stat 1 -->
        <div class="stat-item" style="flex: 1; min-width: 200px; text-align: center; padding: 20px; border-right: 1px solid #222;">
            <span style="display: block; color: #f49d26; font-size: 3rem; font-weight: bold; font-family: 'Arial', sans-serif; margin-bottom: 10px;">15+</span>
            <p style="color: #fff; text-transform: uppercase; font-size: 0.85rem; letter-spacing: 2px; margin: 0;">Établissements</p>
        </div>

        <!-- Stat 2 -->
        <div class="stat-item" style="flex: 1; min-width: 200px; text-align: center; padding: 20px; border-right: 1px solid #222;">
            <span style="display: block; color: #f49d26; font-size: 3rem; font-weight: bold; font-family: 'Arial', sans-serif; margin-bottom: 10px;">4.8</span>
            <p style="color: #fff; text-transform: uppercase; font-size: 0.85rem; letter-spacing: 2px; margin: 0;">Note Moyenne</p>
        </div>

        <!-- Stat 3 -->
        <div class="stat-item" style="flex: 1; min-width: 200px; text-align: center; padding: 20px; border-right: 1px solid #222;">
            <span style="display: block; color: #f49d26; font-size: 3rem; font-weight: bold; font-family: 'Arial', sans-serif; margin-bottom: 10px;">24/7</span>
            <p style="color: #fff; text-transform: uppercase; font-size: 0.85rem; letter-spacing: 2px; margin: 0;">Réservations</p>
        </div>
    </div>
</section>

<style>
    /* Pour que les bordures disparaissent sur mobile et ne cassent pas le design */
    @media (max-width: 768px) {
        .stat-item {
            border-right: none !important;
            border-bottom: 1px solid #222;
        }
        .stat-item:last-child {
            border-bottom: none !important;
        }
    }
</style>