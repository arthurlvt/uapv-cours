import numpy as np
import time

# ------------------- FONCTIONS ------------------- #

# -- Q1:  Résolution d'un système linéaire -- #
def solving_system(A, B):
    return np.linalg.solve(A, B)

# -- Q2:  Produit scalaire de deux vecteurs ligne -- #
def produit_scalaire(ligne1, ligne2):
    resultat = 0
    for i in range(len(ligne1)):
        resultat += ligne1[i] * ligne2[i]
    return resultat

# -- Q3:  Produit matriciel en utilisant produit_scalaire -- #
def produit_matrices(A, B):
    n = len(A)
    B_T = [[B[j][i] for j in range(n)] for i in range(n)]
    C = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = produit_scalaire(A[i], B_T[j])
    return C

# -- Q4:  Comparaison des temps sur grandes matrices -- #
def compare_temps():
    n = 500
    A = np.random.rand(n, n)
    B = np.random.rand(n, n)

    start = time.time()
    produit_matrices(A.tolist(), B.tolist())
    print(f"Temps avec produit_matrices : {time.time() - start:.4f}s")

    start = time.time()
    np.dot(A, B)
    print(f"Temps avec np.dot          : {time.time() - start:.4f}s")

# -- Q5:  Moyenne et écart-type des notes par étudiant -- #
def moyenne_et_ecart_type(A):
    moyennes     = np.mean(A, axis=1).round(0)
    ecarts_types = np.std(A, axis=1).round(2)
    return moyennes, ecarts_types

# -- Q6:  Indice de l'étudiant avec la meilleure moyenne -- #
def indice_meilleure_moyenne(A):
    return np.argmax(np.mean(A, axis=1))

# -- Q7:  Calcul de l'inverse d'une matrice -- #
def calcul_inverse():
    G = np.random.rand(5, 5)
    print(f"Inverse de G :\n{np.linalg.inv(G)}")
    print(f"G x G^-1 :\n{np.dot(G, np.linalg.inv(G))}")

# -- Q8: Chercher un pivot + échange de deux lignes d'une matrice + Transvection + Échelonner une matrice -- #
def chercher_pivot(M, l, c):
    pivot = l
    for k in range(l, M.shape[0]):
        if abs(M[k, c]) > abs(M[pivot, c]):
            pivot = k
    return pivot

def echanger_lignes(M, i, j):
    M[i], M[j] = M[j].copy(), M[i].copy()

def transvection(M, i, j, c):
    M[j]= M[i,c]*M[j] - M[j,c]*M[i]
    
def echelonner(A_original):
    A = A_original.copy()
    n1 = A.shape[0]
    n2 = A.shape[1]
    l = 0
    colonnes_pivot = []
    for c in range(n2):
        if l == n1: break
        pivot = chercher_pivot(A, l, c)
        if A[pivot][c] == 0: continue
        if pivot > l:
            echanger_lignes(A, l, pivot)
        for k in range(l + 1, n1):
            transvection(A, l, k, c)
        colonnes_pivot.append(c)
        l = l + 1
    
    rang = l
    famille_libre = A_original[:, colonnes_pivot]
    return A, rang, famille_libre
        

# ------------------- MAIN ------------------- #
if __name__ == "__main__":

    A = np.array([
        [14, 12,  8],  # étudiant 0
        [ 9, 17, 11],  # étudiant 1
        [16, 10, 13]   # étudiant 2
    ])

    A_systeme = np.array([
        [ 0,  1, -1],
        [-2,  4, -1],
        [-2,  5, -4]
    ])
    B_systeme = np.array([3, 1, -2])

    def q1():
        print("===== Q1 : Résolution d'un système linéaire =====")
        solution = solving_system(A_systeme, B_systeme)
        print("Solution du système AX = B :\n", solution)

    def q2():
        print("===== Q2 : Produit scalaire de deux vecteurs ligne =====")
        ligne1, ligne2 = A[0], A[1]
        print(f"Produit scalaire de {ligne1} et {ligne2} : {produit_scalaire(ligne1, ligne2)}")

    def q3():
        print("===== Q3 : Produit matriciel =====")
        B = np.array([[1, 2, 3], [0, 1, 4], [5, 6, 0]])
        print("Produit matriciel A @ B :\n", produit_matrices(A.tolist(), B.tolist()))

    def q4():
        print("===== Q4 : Comparaison des temps sur grandes matrices =====")
        compare_temps()

    def q5():
        print("===== Q5 : Moyenne et écart-type des notes =====")
        print("\nMatrice des notes :")
        print("  Étudiant | Maths | Algo | Réseau")
        print("  " + "-" * 34)
        for i, ligne in enumerate(A):
            print(f"  Étudiant {i} |  {ligne[0]:4} | {ligne[1]:4} | {ligne[2]:6}")
        print()
        moyennes, ecarts_types = moyenne_et_ecart_type(A)
        for i in range(len(A)):
            print(f"  Étudiant {i} → moyenne : {moyennes[i]:.0f} | écart-type : {ecarts_types[i]:.2f}")

    def q6():
        print("===== Q6 : Meilleure moyenne =====")
        print(f"Indice de l'étudiant avec la meilleure moyenne : {indice_meilleure_moyenne(A)}")

    def q7():
        print("===== Q7 : Calcul de l'inverse d'une matrice =====")
        calcul_inverse() 
    
    def q8():
        print("===== Q8 : Pivot, échange, transvection et échelonnement =====")
        
        A = np.array([[1,2,1,1],[2,4,2,2],[3,6,3,4]], dtype=float)
        B = np.array([[1,2,1,3,3],[2,4,0,4,4],[1,2,3,5,5],[2,4,0,4,7]], dtype=float)
        A_orig = np.array([[1,2,1,1],[2,4,2,2],[3,6,3,4]], dtype=float)
        A_ech, rang, famille = echelonner(A_orig)
        print(f"Matrice A de départ :\n{A_orig}")
        print(f"Matrice A échelonnée :\n{A_ech}")
        print(f"Rang : {rang}")
        print(f"Famille libre :\n{famille}")
        
    questions = {
        1: ("Résolution d'un système linéaire", q1),
        2: ("Produit scalaire de deux vecteurs", q2),
        3: ("Produit matriciel", q3),
        4: ("Comparaison des temps (custom vs numpy)", q4),
        5: ("Moyenne et écart-type des notes", q5),
        6: ("Indice de la meilleure moyenne", q6),
        7: ("Calcul de l'inverse d'une matrice", q7),
        8: ("Pivot, échange, transvection et échelonnement", q8)
    }

    while True:
        print("\n" + "=" * 40)
        print("  TP4 - numpy")
        print("=" * 40)
        print(f"\n  Matrice A :\n{A}\n")
        for num, (desc, _) in questions.items():
            print(f"  {num}. {desc}")
        print(f"  0. Quitter")
        print()

        choix = input("Choix : ").strip()
        if choix == "0":
            break
        try:
            num = int(choix)
            if num in questions:
                print()
                questions[num][1]()
            else:
                print("Choix invalide.")
        except ValueError:
            print("Choix invalide.")