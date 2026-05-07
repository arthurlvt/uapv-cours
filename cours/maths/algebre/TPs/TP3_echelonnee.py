import numpy as np

# -- Q1-A : Vérifier si une matrice est sous forme échelonnée -- #
def trouver_pivot_sur_ligne(A, i):
    for j in range(A.shape[1]):
        if abs(A[i, j]) >= 1e-10:
            return j
    return -1

# -- Q1-B : Trouver un pivot sur une ligne -- #
def est_ligne_nulle(A, i):
    return np.all(np.abs(A[i]) < 1e-10)

# -- Q1-C : Vérifier que toute les lignes nulles sont en bas de la matrice -- #
def check_echelonnee(A):
    for i in range(A.shape[0]):
        if est_ligne_nulle(A, i):
            for j in range(i + 1, A.shape[0]):
                if not est_ligne_nulle(A, j):
                    return False
    return True
    
# -- Q1-D : Vérifier que tous les éléments sous le pivot sont nuls -- #
def verifier_pivots(A):
    for i in range(A.shape[0]):
        pivot_col = trouver_pivot_sur_ligne(A, i)
        if pivot_col != -1:
            if np.any(np.abs(A[i+1:, pivot_col]) >= 1e-10):
                return False
    return True

# -- Q1-E : Vérifier que la matrice est échelonnée -- #
# Vérifier 4 conditions pour une matrice échelonnée :
# 1. Chaque ligne non nulle a un pivot à gauche de la ligne précédente.
# 2. Les éléments sous le pivot sont nuls.
# 3. Les lignes nulles sont en bas de la matrice.
# 4. La matrice est de forme échelonnée.
def est_echelonnee(A):
    if not check_echelonnee(A):
        return False
    if not verifier_pivots(A):
        return False
    pivots = []
    for i in range(A.shape[0]):
        pivot_col = trouver_pivot_sur_ligne(A, i)
        if pivot_col != -1:
            pivots.append(pivot_col)
    if not all(pivots[i] < pivots[i + 1] for i in range(len(pivots) - 1)):
        return False
    return True