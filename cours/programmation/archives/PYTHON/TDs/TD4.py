import random

def Zeros(n, m):
    matrice = []
    # Création des n lignes
    for i in range(n):
        ligne = []
        # Remplissage des m colonnes avec 0
        for j in range(m):
            ligne.append(0)
        matrice.append(ligne)
    return matrice


def aleatoire(n, m, min_val, max_val):
    matrice = []
    for i in range(n):
        ligne = []
        for j in range(m):
            # Génère un entier aléatoire entre min_val et max_val inclus
            ligne.append(random.randint(min_val, max_val))
        matrice.append(ligne)
    return matrice


def afficher_matrice(matrice, n, m):

    # On n'utilise pas n et m directement dans le parcours mais ils sont requis par l'énoncé.
    print("-" * (m * 4))
    for ligne in matrice:
        # Affichage des éléments de la ligne séparés par une tabulation
        print(*ligne, sep='\t')
    print("-" * (m * 4))


def compter_occurrences(matrice, n, m, valeur):
    count = 0
    for ligne in matrice:
        for element in ligne:
            if element == valeur:
                count += 1
    return count


def sont_lignes_identiques(matrice, n, m, index1, index2):
    # Vérification des index valides
    if index1 < 0 or index1 >= n or index2 < 0 or index2 >= n:
        print("Erreur: Index de ligne invalide.")
        return False
    
    # En Python, la comparaison de listes (lignes) est directe
    return matrice[index1] == matrice[index2]


def existe_deux_lignes_identiques(matrice, n, m):
    # Comparaison de chaque ligne (i) avec toutes les lignes suivantes (j)
    for i in range(n):
        for j in range(i + 1, n): # j commence à i + 1 pour éviter de comparer une ligne avec elle-même et les doublons
            if sont_lignes_identiques(matrice, n, m, i, j):
                return True
    return False


def get_colonne(matrice, n, m, j):
    """
    Extrait la colonne d'index j de la matrice.
    """
    colonne = []
    for i in range(n):
        colonne.append(matrice[i][j])
    return colonne


def existe_deux_colonnes_identiques(matrice, n, m):
    # Si la matrice n'a qu'une seule colonne ou moins, c'est impossible
    if m < 2:
        return False
    
    # Comparaison de chaque colonne (j1) avec toutes les colonnes suivantes (j2)
    for j1 in range(m):
        colonne1 = get_colonne(matrice, n, m, j1)
        for j2 in range(j1 + 1, m):
            colonne2 = get_colonne(matrice, n, m, j2)
            
            # Comparaison des deux colonnes (listes)
            if colonne1 == colonne2:
                return True
    return False


def produit_matrices(A, n_A, m_A, B, n_B, m_B):
    # Condition de faisabilité : nombre de colonnes de A doit égaler le nombre de lignes de B
    if m_A != n_B:
        print("Erreur: Le produit matriciel n'est pas possible (mA != nB).")
        return None, 0, 0

    n_C = n_A
    m_C = m_B
    
    # Initialisation de la matrice résultat C avec des zéros
    C = Zeros(n_C, m_C)
    
    # Calcul du produit
    for i in range(n_C): # Lignes de C (et A)
        for j in range(m_C): # Colonnes de C (et B)
            somme = 0
            for k in range(m_A): # Colonnes de A et Lignes de B
                somme += A[i][k] * B[k][j]
            C[i][j] = somme
            
    return C, n_C, m_C


def est_symetrique(matrice, n, m):
    # 1. La matrice doit être carrée
    if n != m:
        return False
    
    # 2. Vérification de la symétrie A[i][j] == A[j][i]
    for i in range(n):
        for j in range(i + 1, m): # On parcourt seulement la partie au-dessus de la diagonale
            if matrice[i][j] != matrice[j][i]:
                return False
                
    return True


def est_liste_triee(L):
    n = len(L)
    # On parcourt jusqu'à l'avant-dernier élément
    for i in range(n - 1):
        if L[i] > L[i+1]:
            return False # Si un élément est plus grand que le suivant, ce n'est pas trié
    return True


def passer_echange(L, n):
    echange_fait = False
    
    # On parcourt les éléments jusqu'à l'indice n-2
    for i in range(n - 1):
        if L[i] > L[i+1]:
            # Échange des valeurs
            L[i], L[i+1] = L[i+1], L[i]
            echange_fait = True
            
    return not echange_fait # Renvoie True si AUCUN échange n'a été fait


def trier_liste_bulle(L):
    n = len(L)
    # L'algorithme de tri à bulles a besoin de n-1 passes au maximum
    for taille_sous_liste in range(n, 1, -1):
        # On passe et on vérifie si la liste est déjà triée
        est_trie = passer_echange(L, taille_sous_liste)
        if est_trie:
            break # Si c'est trié, on arrête
    return L

def trier_matrice(matrice, n, m):
    # La fonction modifie la matrice en place.
    for i in range(n):
        # trier_liste_bulle est appelée pour trier la sous-liste (ligne)
        trier_liste_bulle(matrice[i])
        
    # Vérification si la matrice est triée selon la définition (toutes les lignes triées)
    est_completement_triee = True
    for ligne in matrice:
        if not est_liste_triee(ligne):
            est_completement_triee = False
            break
            
    return est_completement_triee # Renvoie True si toutes les lignes sont triées