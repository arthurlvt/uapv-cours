import numpy as np

EPSILON = 1e-10

# Q1-A : Renvoie le numéro de colonne du premier élément non nul de la ligne i ou -1 si la ligne est entièrement nulle.
def trouver_pivot_sur_ligne(A, i):
    for j in range(A.shape[1]):
        if abs(A[i, j]) >= EPSILON:
            return j
    return -1

# Q1-B : Renvoie True si la ligne i de A est entièrement nulle.
def est_ligne_nulle(A, i):
    return np.all(np.abs(A[i]) < EPSILON)

# Q1-C : Renvoie True si toutes les lignes nulles sont situées en bas de la matrice.
def lignes_nulles_en_bas(A):
    m = A.shape[0]
    for i in range(m):
        if est_ligne_nulle(A, i):
            for j in range(i + 1, m):
                if not est_ligne_nulle(A, j):
                    return False
    return True

# Q1-D : Renvoie True si tous les éléments SOUS chaque pivot sont nuls.
def verifier_pivots(A):
    m = A.shape[0]
    for i in range(m):
        pivot_col = trouver_pivot_sur_ligne(A, i)
        if pivot_col != -1 and i + 1 < m:          # ← garde i+1 < m avant le slicing
            if np.any(np.abs(A[i + 1:, pivot_col]) >= EPSILON):
                return False
    return True

# Q1-E : Renvoie True si la matrice est sous forme échelonnée.
#   Conditions vérifiées :
#   1. Les lignes nulles sont en bas.
#   2. Les éléments sous chaque pivot sont nuls.
#   3. Les pivots se déplacent strictement vers la droite ligne après ligne.
def est_echelonnee(A):
    if not lignes_nulles_en_bas(A):
        return False
    if not verifier_pivots(A):
        return False
    pivots = [trouver_pivot_sur_ligne(A, i)
              for i in range(A.shape[0])
              if not est_ligne_nulle(A, i)]
    return all(pivots[k] < pivots[k + 1] for k in range(len(pivots) - 1))


def Echelonner(M):
    A = M.astype(float).copy()
    m, n = A.shape
    i, j = 0, 0

    while i < m and j < n:
        k = i
        while k < m and abs(A[k, j]) < EPSILON:
            k += 1
        if k >= m:
            j += 1
        else:
            A[[i, k]] = A[[k, i]]

            for r in range(i + 1, m):
                if abs(A[r, j]) >= EPSILON:
                    facteur = A[r, j] / A[i, j]
                    for c in range(j, n):
                        A[r, c] = A[r, c] - facteur * A[i, c]

            i += 1
            j += 1

    A[np.abs(A) < EPSILON] = 0.0
    return A


print("=" * 55)
print("Q3 — Test de la fonction Echelonner")
print("=" * 55)

# Matrice dont on connaît le résultat à la main :
#   L2 ← L2 - 2*L1  →  [0, -3, -3]
#   L3 ← L3 - 3*L1  →  [0, -6, -6]
#   L3 ← L3 - 2*L2  →  [0,  0,  0]
# Résultat attendu : [[1,2,3],[0,-3,-3],[0,0,0]]
M_test = np.array([
    [1,  2,  3],
    [2,  1,  3],
    [3,  0,  3]
], dtype=float)

print("Matrice de départ :\n", M_test)
M_ech = Echelonner(M_test)
print("Forme échelonnée :\n", M_ech)
print("Est échelonnée ?", est_echelonnee(M_ech))


# ============================================================
# PARTIE 4 — Sous-famille libre de cardinal maximal
# ============================================================

print("\n" + "=" * 55)
print("Q4 — Sous-famille libre extraite de {e1,...,e6}")
print("=" * 55)

e1 = np.array([3, 0, 0, 0, 1], dtype=float)
e2 = np.array([1, 0, 1, 0, 0], dtype=float)
e3 = np.array([2, 1, 0, 0, 5], dtype=float)
e4 = np.array([3, 2, 1, 1, 0], dtype=float)
e5 = np.array([1, 1, 1, 1, 1], dtype=float)
e6 = np.array([1, 0, 1, 1, 2], dtype=float)

# On forme la matrice dont les COLONNES sont les vecteurs, puis on l'échelonne.
# Les colonnes-pivots correspondent aux vecteurs librement indépendants.
vecteurs = [e1, e2, e3, e4, e5, e6]
noms     = ["e1", "e2", "e3", "e4", "e5", "e6"]

A = np.column_stack(vecteurs)   # matrice 5×6
print("Matrice A (vecteurs en colonnes) :\n", A)

A_ech = Echelonner(A)
print("\nForme échelonnée :\n", A_ech)

# Identifier les colonnes-pivots (colonnes portant un pivot)
pivots_cols = []
pivot_row = 0
for j in range(A_ech.shape[1]):
    if pivot_row < A_ech.shape[0]:
        if abs(A_ech[pivot_row, j]) >= EPSILON:
            pivots_cols.append(j)
            pivot_row += 1

rang = len(pivots_cols)
sous_famille = [noms[j] for j in pivots_cols]
print(f"\nRang de la matrice : {rang}")
print(f"Colonnes-pivots (indices 0-based) : {pivots_cols}")
print(f"Sous-famille libre de cardinal maximal : {{{', '.join(sous_famille)}}}")

# Vecteurs dépendants (non-pivots)
non_pivots = [noms[j] for j in range(len(noms)) if j not in pivots_cols]
print(f"Vecteurs dépendants des autres : {non_pivots}")

# La famille est-elle une base de Vect(e1,...,e6) ?
print(f"\nLa sous-famille libre trouvée est-elle une base de Vect(e1,...,e6) ?")
print(f"  → Oui : elle est libre ET génératrice (cardinal = rang = {rang}).")



def Echelonner_vectorise(M):
    A = M.astype(float).copy()
    m, n = A.shape
    i, j = 0, 0

    while i < m and j < n:
        # Remplacement de la boucle 1 : np.where sur la colonne j à partir de i
        pivot_candidats = np.where(np.abs(A[i:, j]) >= EPSILON)[0]

        if len(pivot_candidats) == 0:
            j += 1
        else:
            k = i + pivot_candidats[0]          # première ligne non nulle

            A[[i, k]] = A[[k, i]]               # échange de lignes

            if i + 1 < m:
                f = A[i + 1:, j] / A[i, j]     # vecteur des facteurs (shape : m-i-1,)
                A[i + 1:, j:] -= f[:, None] * A[i, j:]   # soustraction matricielle

            i += 1
            j += 1

    A[np.abs(A) < EPSILON] = 0.0
    return A

print("\n" + "=" * 55)
print("Q5 — Test de la version vectorisée")
print("=" * 55)
M_ech_v = Echelonner_vectorise(M_test.copy())
print("Résultat version vectorisée :\n", M_ech_v)
print("Identique à la version naïve ?", np.allclose(Echelonner(M_test), M_ech_v))