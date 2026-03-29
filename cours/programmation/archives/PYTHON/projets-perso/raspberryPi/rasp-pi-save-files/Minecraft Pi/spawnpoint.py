# Importation du/des module(s) nécéssaire(s): Minecraft, time
from mcpi.minecraft
    import Minecraft
    import time

# Début du programme : Dans ce programme nous allons créer une station de téléportation avec comme repère un bloc de fer !
mc = Minecraft.create() # Cette ligne de code permet de dire que "mc" est la partie crée sur Minecraft Pi.
diamant = 57 # Dans cette ligne de code, on dit que "diamant" correspond à la valeur "57".

mc.postToChat ("Teleportation en cour...")
time.sleep(5)

# Dans les prochaines ligne du programme, nous allons définir l'emplacement de notre première station de téléportation !
ts1 = mc.player.getTilePos() # Cette ligne définie "ts1" comme l'emplacement actuel du joueur.
mc.setBlock (ts1.x, ts1.y -1, ts1.z, diamant) # Cette définie que l'on va placer un bloc de diamant dans la position du joueur actuel mais que l'on va enlever 1° à la coordonnée y


# Dans les prochaines ligne du programme, nous allons afficher un message qui dira au joueur de trouver un nouvel emplacement pour notre base de téléportation !
mc.postToChat("Vous disposez de 30 secondes pour trouver un autre emplacement")
time.sleep(30)


# Dans les prochaines ligne du programme, nous allons définir l'emplacement de notre seconde station de téléportation !
ts2 = mc.player.getTilePos()
mc.setBlock(ts2.x, ts2.y -1, ts2.z, diamant)
mc.postToChat(Création du second emplacement)
time.sleep(2)


# Dans les prochaine ligne de code, nous allons créer une boucle infinie pour que notre joueur puisse se téléporter entre ces deux bases

while True:
    x, y, z = mc.player.getTilePos()
    if(x == ts1.x) and (y == ts1.y) and (z == ts1.z): # Dans cette ligne nous disons que x correspond à la coordonnée de la base de téléportation 1
        mc.player.setPos