import numpy as np
import time
saut = "\n"

# --------------- EXERCICE 1 --------------- #
def exercice1():
    print("------ EXERCICE 1 ------", saut)
    # VERSION 1 DE LA MATRICE A
    A = np.array([[5, 3, 3],
                  [3, 5, 3],
                  [3, 3, 5]])
    # VERSION 2 DE LA MATRICE A
    Abis = 3 * np.ones((3, 3)) + 2 * np.eye(3)
    
    # VERSION 1 DE LA MATRICE B
    B = np.array([[1, 0, 0],
                  [1, 1, 0],
                  [1, 0, 1]])
    # VERSION 2 DE LA MATRICE B
    Bbis = np.eye(3)
    Bbis[:, 0] = 1

    # VERSION 1 DE LA MATRICE C
    C = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12],
                  [13, 14, 15, 16]])
    # VERSION 2 DE LA MATRICE C
    Csize = 4
    Cbis = np.eye(Csize)
    j = 1
    for i in range(Csize):
        for k in range(Csize):
            C[i, k] = j
            j += 1

    # VERSION 1 DE LA MATRICE D
    D = np.array([[1, 2, 3, 4],
                  [1, 2, 3, 4],
                  [1, 2, 3, 4],
                  [1, 2, 3, 4]])
    # VERSION 2 DE LA MATRICE D
    Dsize = 4
    Dbis = np.eye(Dsize)
    for i in range(Dsize):
        Dbis[:, i] = i + 1
    print("Matrice A:", saut, Abis, saut)
    print("Matrice B:", saut, Bbis, saut)
    print("Matrice C:", saut, Cbis, saut)
    print("Matrice D:", saut, Dbis, saut)


# --------------- EXERCICE 2 --------------- #
def exercice2():
    print("------ EXERCICE 2 ------", saut)
    B2 = np.array([[1, 1, 0],
                    [1, -1, 1],
                    [1, 0, 1]])
    # a- Vérifier que B est inversible
    print("Rang de B :", np.linalg.matrix_rank(B2))
    # b- Calculer son inverse
    B_inv = np.linalg.inv(B2)
    print("Inverse de B :", saut, B_inv, saut)
    # c- Résoudre le système
    b = np.array([1, 3, -2])
    x = np.linalg.solve(B2, b)
    print("Solutions (x, y, z) :", x, saut)
    # Vérification
    print("Vérification B @ B_inv :", saut, B2 @ B_inv, saut)


# --------------- EXERCICE 3 --------------- #
def exercice3():
    print("------ EXERCICE 3 ------", saut)
    # 1- Système direct
    A3 = np.array([[1, 1, 1],
                    [1, -2, 1],
                    [2, -1, 1]])
    b3 = np.array([1, 0, 2])
    x1 = np.linalg.solve(A3, b3)
    print("1- Solution (x, y, z) :", x1, saut)
    # 2- D'abord résoudre a, b, c
    A3bis = np.array([[3, 1, -1],
                       [1, 1, 1],
                       [1, -2, 2]])
    b3bis = np.array([3, 3, 1])
    abc = np.linalg.solve(A3bis, b3bis)
    print("2- a, b, c :", abc)
    # Puis résoudre x, y, z avec a, b, c comme second membre
    x2 = np.linalg.solve(A3, abc)
    print("2- Solution (x, y, z) :", x2, saut)


# --------------- EXERCICE 4 --------------- #
def exercice4():
    print("------ EXERCICE 4 ------", saut)
    col = np.arange(1, 11).reshape(10, 1)
    ligne = np.ones((1, 10))
    M = col @ ligne
    print(M.astype(int), saut)


# --------------- EXERCICE 5 --------------- #
def exercice5():
    print("------ EXERCICE 5 ------", saut)
    n = int(input("Entrez n : "))
    # VERSION AVEC BOUCLE
    t0 = time.perf_counter()
    s1 = 0
    for i in range(n + 1):
        s1 += i
    t1 = time.perf_counter()
    # VERSION AVEC NUMPY
    t2 = time.perf_counter()
    s2 = np.sum(np.arange(n + 1))
    t3 = time.perf_counter()
    print("Somme (boucle) :", s1, "| Temps :", t1 - t0, "s")
    print("Somme (numpy)  :", s2, "| Temps :", t3 - t2, "s", saut)


# --------------- EXERCICE 6 --------------- #
def exercice6():
    print("------ EXERCICE 6 ------", saut)
    n = int(input("Entrez n (lignes) : "))
    m = int(input("Entrez m (colonnes) : "))
    A = np.ones((n, m))
    B = np.ones((n, m)) * 2
    C = np.ones((n, m)) * 3
    # Vérifier la cohérence des tailles
    if A.shape != B.shape or B.shape != C.shape:
        print("Erreur : les matrices n'ont pas la même taille")
        return
    nb_lignes = A.shape[0]
    resultat = np.empty((3 * nb_lignes, A.shape[1]))
    for i in range(nb_lignes):
        resultat[3*i] = A[i]
        resultat[3*i + 1] = B[i]
        resultat[3*i + 2] = C[i]
    print("Matrice générée", 3*n, "*", m, ":", saut, resultat.astype(int), saut)
    
  
# --------------- EXERCICE 7 --------------- #
def exercice7():
    print("------ EXERCICE 7 ------", saut)
    A = np.random.uniform(-5, 5, (10000, 10000))
    B = A.copy()
    # VERSION AVEC BOUCLE
    t0 = time.perf_counter()
    for i in range(B.shape[0]):
        for j in range(B.shape[1]):
            if B[i, j] < 0:
                B[i, j] = 0
            elif B[i, j] > 1:
                B[i, j] = 1
    t1 = time.perf_counter()
    # VERSION AVEC NUMPY
    t2 = time.perf_counter()
    Bbis = A.copy()
    Bbis[Bbis < 0] = 0
    Bbis[Bbis > 1] = 1
    t3 = time.perf_counter()
    print("Matrice d'origine:", A, saut)
    print("Matrice transformée (avec boucle):", B, saut)
    print("Temps (boucle) :", t1 - t0, "s")
    print("Matrice transformée (avec numpy):", Bbis, saut)
    print("Temps (numpy)  :", t3 - t2, "s")


# --------------- EXERCICE 8 --------------- #
def exercice8():
    print("------ EXERCICE 8 ------", saut)
    n = int(input("Entrez n: "))
    m = int(input("Entrez m: "))
    A = np.random.randint(-5, 5, (n, m))
    B = A.copy()
    # VERSION AVEC BOUCLE
    for i in range(B.shape[0]):
        for j in range(B.shape[1]):
            B[i, j] = abs(B[i, j])
    # VERSION AVEC NUMPY
    Bbis = np.abs(A)
    print("Matrice d'origine:", saut, A)
    print("Matrice valeur absolue (boucle):", saut, B)
    print("Matrice valeur absolue (numpy):", saut, Bbis)
    
    
# --------------- EXERCICE 9 --------------- #
def exercice9():
    print("------ EXERCICE 9 ------", saut)
    n = int(input("Entrez n: "))
    m = int(input("Entrez m: "))
    A = np.random.randint(-5, 5, (n, m))
    # VERSION AVEC BOUCLE
    compteur = 0
    for i in range(A.shape[0] - 1): # -1 pour éviter le dépassement
        for j in range(A.shape[1] - 1): # -1 aussi
            if A[i, j] == A[i+1, j+1]:
                compteur += 1
    total = (n - 1) * (m - 1)
    pOccurences = compteur / total
    # VERSION AVEC NUMPY
    compteur_np = np.sum(A[:-1, :-1] == A[1:, 1:])
    pOccurences_np = compteur_np / ((n - 1) * (m - 1))
    print("Pourcentage d'occurences (avec boucle) :", pOccurences * 100, "%")   
    print("Pourcentage d'occurences (avec numpy):", pOccurences_np * 100, "%")
  

# --------------- EXERCICE 10 --------------- #
def exercice10():
    print("------ EXERCICE 10 ------", saut)
    A = np.random.uniform(-5, 5, (5, 3))
    print("Matrice d'origine:", saut, A, saut)
    
    # VERSION AVEC BOUCLE
    B = A.copy()
    n = B.shape[0]
    for j in range(B.shape[1]):
        # Calcul de la moyenne
        m = 0
        for i in range(n):
            m += B[i, j]
        m = m / n
        # Calcul de l'écart-type et
        et = 0
        for i in range(n):
            et += (B[i, j] - m) ** 2
        et = (et / n) ** 0.5
        # Normalisation
        for i in range(n):
            B[i, j] = (B[i, j] - m) / et
    print("Normalisée (boucle):", saut, B, saut)
    # VERSION AVEC NUMPY
    m = np.mean(A, axis=0) # moyenne de chaque colonne
    et = np.std(A, axis=0) # écart-type de chaque colonne
    C = (A - m) / et
    print("Normalisée (numpy):", saut, C, saut)
    
    
# --------------- EXERCICE 11 --------------- #
def exercice11():
    print("------ EXERCICE 11 ------", saut)
    n = int(input("Entrez n: "))
    m = int(input("Entrez m: "))
    A = np.random.randint(-5, 5, (n, m))
    B = np.abs(A)
    compteurValeursPaires = 0
    compteurValeursImpaires = 0
    for i in range(B.shape[0]):
        for j in range(B.shape[1]):
            if B[i, j] % 2 == 0:
                compteurValeursPaires += 1
            else:
                compteurValeursImpaires += 1
    compteurValeursPairesNumpy = np.sum(B % 2 == 0)
    compteurValeursImpairesNumpy = np.sum(B % 2 != 0)
    print(B, saut)
    print("Nombre de valeurs paires:", compteurValeursPairesNumpy, saut, "Nombre de valeurs impaires:", compteurValeursImpairesNumpy)
    # idem avec la boucle

    
# ------------------------------------------ #
# ------------- MENU --- CHOIX ------------- #
# ------------------------------------------ #
print("# ------ ALGEBRE ET PROGRAMME - TP1 ------ #")

exercices = {
    1: ("Création de matrices", exercice1),
    2: ("Inversibilité et résolution", exercice2),
    3: ("Systèmes d'équations", exercice3),
    4: ("Produit vecteur colonne/ligne", exercice4),
    5: ("Somme chronométrée", exercice5),
    6: ("Concaténation alternée", exercice6),
    7: ("Manipulation de matrices", exercice7),
    8: ("Transformation de matrices", exercice8),
    9: ("Compteur d'occurences dans une matrice", exercice9),
    10: ("Caractéristique et normalisation de matrices", exercice10),
    11: ("Compteur de valeurs paires et impaires dans une matrice", exercice11),
}

def menu():
    print("\nQue souhaitez-vous faire ?")
    for num, (nom, _) in exercices.items():
        print(f"  ({num}) : {nom}")
    print("  (0) : Quitter")
    
menu()
choice = int(input("CHOIX : "))

while choice != 0:
    if choice in exercices:
        exercices[choice][1]()
    else:
        print("Choix invalide")
    menu()
    choice = int(input("CHOIX : "))

print("Programme stopé, fin des itérations")
    

