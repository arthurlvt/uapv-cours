from random import randint as rand

def symbole(v):
    if v == 0: return "."
    if v == 1: return "X"
    if v == 2: return "O"
    
def grille_vide_amelioree(t):
    grille = []

    entete = [" "]
    for j in range(1, t + 1): 
        entete.append(j)
    grille.append(entete)

    for i in range(1, t + 1):
        ligne = [i]
        for j in range(t):
            ligne.append(".")
        grille.append(ligne)

    return grille

def afficher_grille(G, t):
    for i in range(t + 1):
        for j in range(t + 1):
            print(G[i][j], end=" ")
        print()
    
def grille_pleine(G, t):
    for i in range(1, t + 1):
        for j in range(1, t + 1):
            if G[i][j] == ".":
                return False
    return True
      
def joueur():
    return symbole(rand(1, 2))

def autreJoueur(joueur):
    if joueur == "O": return "X"
    if joueur == "X": return "O"

def coup_aleatoire(G, t):
    while True:
        x = rand(1, t)
        y = rand(1, t)
        if G[x][y] == ".":
            return x, y


def saisir_coup(G, t, joueur, adversaire):
    x, y = input("Entrez les coordonnées de votre case: ").split()
    x = int(x)
    y = int(y)

    if x < 1 or x > t or y < 1 or y > t:
        print("Coup Invalide! Cette case n'existe pas")
        return False
    if G[x][y] == adversaire:
        print("Coup Invalide! Il y a déjà le pion de votre adversaire")
        return False
    if G[x][y] == joueur:
        print("Coup Invalide! Vous avez déjà posé un pion sur cette case")
        return False

    print("Coup Valide")
    G[x][y] = joueur
    print("Nouvelle Grille :")
    afficher_grille(G, t)
    print(f"Au tour du joueur {adversaire}")
    return True
    
def coup_ordinateur(G, t, joueur):
    ordinateur = autreJoueur(joueur)
    for i in range(1, t+1):
        for j in range(1, t+1):
            if G[i][j] == ".":
                if joueur_gagnant(G, t, joueur): G.append(ordinateur)
                if joueur_gagnant(G, t, ordinateur): G.append(ordinateur)
            if G[i][j] == symbole(joueur): return
            if G[i][j] == symbole(ordinateur): return  
    
def ligne_gagnante(G, t, i, joueur):
    for j in range(1, t + 1):
        if G[i][j] != joueur: return False
    return True

def colonne_gagnante(G, t, j, joueur):
    for i in range(1, t + 1):
        if G[i][j] != joueur: return False
    return True
def diagonale_gagnante(G, t, joueur):
    diag1 = True
    diag2 = True
    for k in range(1, t + 1):
        if G[k][k] != joueur: diag1 = False
        if G[k][t + 1 - k] != joueur: diag2 = False
    return diag1 or diag2

def joueur_gagnant(G, t, joueur):
    for k in range(1, t + 1):
        if ligne_gagnante(G, t, k, joueur) or colonne_gagnante(G, t, k, joueur): return True
    return diagonale_gagnante(G, t, joueur)

def partie_classique(t):
    grille = grille_vide_amelioree(t)
    joueur1 = joueur()
    joueur2 = autreJoueur(joueur1)
    print("Voici la grille : \n")
    afficher_grille(grille, t)
    print()
    print(f"Joueur 1: {joueur1} \n Joueur 2: {joueur2}")
    print(f"{joueur()} commence :", end="")
    while True:
        while not saisir_coup(grille, t, joueur1, joueur2): pass
        if joueur_gagnant(grille, t, joueur1): return 1

        while not saisir_coup(grille, t, joueur2, joueur1): pass
        if joueur_gagnant(grille, t, joueur2): return 2
        
        if grille_pleine(grille, t): return 0   
    
def partie_ordinateur(t):   
    grille = grille_vide_amelioree(t)
    ordinateur = joueur()
    joueur1 = autreJoueur(ordinateur)
    print("Voici la grille : \n")
    afficher_grille(grille, t)
    print()
    print(f"Joueur 1 (vous): {joueur1} \n Joueur 2 (ordinateur): {ordinateur}")
    print(f"{joueur()} commence :", end="")
    while True:
        while not saisir_coup(grille, t, ordinateur, joueur1): pass
        if joueur_gagnant(grille, t, joueur1): return 1
    
        while not saisir_coup(grille, t, joueur1, ordinateur): pass
        if joueur_gagnant(grille, t, joueur1): return 2
            
        if grille_pleine(grille, t): return 0 
    
    
    
def main():

    score0 = 0
    score1 = 0
    score2 = 0

    while True:
        choix = input("Que souhaitez-vous faire? \n (y) Lancer une partie (1 vs 1) \n (b) Joueur contre l'ordinateur \n (n) Arrêter le Jeu \n")

        if choix == "n":
            break
        if choix != "y" and choix != "b":
            print("Une erreur de saisie est survenue! Veuillez réessayer")
            continue
        taille = int(input("Entrez une taille de grille entre 3 et 6 (inclus): "))
    while taille < 3 or taille > 6:
        taille = int(input("Taille invalide. Entrez une taille entre 3 et 6 : "))
        resultat = partie_classique(taille)
        if resultat == 1: score1 += 1
        elif resultat == 2: score2 += 1
        else: score0 += 1

    if score0 + score1 + score2 > 0:
        print(f"Scores du Match : \n Joueur 1: {score1} pts \n Joueur 2: {score2} pts \n {score0} matchs nuls")
        if score1 > score2: print("Victoire du joueur 1 !!")
        elif score2 > score1: print("Victoire du joueur 2 !!")
        else: print("Match Nul")

if __name__ == "__main__":
    main()