# Importation du/des module(s) nécéssaire(s): Minecraft, time
from mcpi.minecraft
    import Minecraft
    import time

# Début du premier programme : Le but de ce programme est de connaître la position du joueur avec 3 coordonnées (x | y | z) !
mc = Minecraft.create() # Cette ligne de code permet de dire que "mc" est la partie crée sur Minecraft Pi

time.sleep(1) # Le module time sert dans ce cas à donner une latence entre chaques actions.
pos = mc.player.getPos() # Cette commande sert à dire que "pos" est définie comme la position du joueur dans Minecraft Pi.
mc.postToChat ("Votre position est : x = " + str (pos.x) +", y = " + str (pos.y) +", z = " + str (pos.z)) # Grâce à cette ligne de code, on va pouvoir poster un message dans le chat de Minecraft Pi



# Début du second programme : Le but de ce programme est de pouvoir téléporter notre joueur en changeant sa position grâce à ses coordonnées !
mc = M# Grâce à cette commande, on va pouvoir poster dans le chat du jeu un message !inecraft.create() # Cette ligne de code permet de dire que "mc" est la partie crée sur Minecraft Pi.

time.sleep(2)
mc.postToChat ("Pret pour la teleportation !")

time.sleep(5)
mc.player.setPos (pos.x, pos.y + 60 pos.z) # Cette commande permet d'ajouter 60° à notre coordonnée x actuelle.



# Début du troisième programme : Le but de ce programme est de pouvoir faire apparaître un bloc grâce aux coordonnée définies dans notre code !
mc = Minecraft.create()

x, y, z = mc.player.getPos() # Ici, on définie que l'on va définir la position de notre bloc grâce aux coordonnées x, y et z.
mc.setBlock (x + 1, y, z, 1) # Grâce à cette ligne, on définie que l'on va placer le bloc en ajoutant 1° à la coordonnée x et le 1 correspond à un bloc (la pierre).