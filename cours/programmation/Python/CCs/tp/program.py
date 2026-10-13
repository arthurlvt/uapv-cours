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
            ligne.append(0)
        grille.append(ligne)

    return grille

def afficher_grille(G, t):
    for i in range(t + 1):
        for j in range(t + 1):
            print(G[i][j], end=" ")
        print()
                
def joueur():
    return symbole(rand(0, 2))

def autreJoueur(joueur):
    if joueur == "O": return "X"
    if joueur == "X": return "O"

def saisir_coup(G, t, joueur):
    print(f"Votre jeu: {joueur}")
    print(grille_vide_amelioree(4))
    x, y = int(input("Entrez les coordonnées de votre case: "))
    adversaire = autreJoueur(joueur)
    for i in range(1, t+1):
        for j in range(1, t+1):
            if x == i and y == j:
                if G[i][j] == adversaire: return "Coup Invalide! Il y a déjà le pion de votre adversaire"
                if G[i][j] == joueur: return "Coup Invalide! Vous avez déjà posé un pion sur cette case"
                else: 
                    print("Coup Valide")
                    G.append(joueur)
    print(f"Nouvelle Grille: \n {grille_vide_amelioree(G)}")

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

def partie(t):
    grille = grille_vide_amelioree(t)
    print("Voici la grille : \n")
    print(afficher_grille(grille))
    
    