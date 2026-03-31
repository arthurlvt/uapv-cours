import numpy as np


# -- Q1-1 : Décomposition LU (méthode de Crout, avec boucles) -- #
def LU_decomposition(A):
    N = A.shape[0]
    L = np.zeros((N, N))
    U = np.eye(N)

    for h in range(N):
        for i in range(h, N):
            L[i, h] = A[i, h] - sum(L[i, k] * U[k, h] for k in range(h))
        for j in range(h + 1, N):
            U[h, j] = (A[h, j] - sum(L[h, k] * U[k, j] for k in range(h))) / L[h, h]

    return L, U


# -- Q1-2 : Vérification détaillée L × U -- #
def afficher_verification(L, U, A):
    N = A.shape[0]
    print("\nVérification détaillée L × U :")
    for i in range(N):
        row = []
        for j in range(N):
            terms = [f"{L[i,k]:.0f}×{U[k,j]:.4g}" for k in range(N)]
            row.append("+".join(terms))
        print("| " + "   ".join(row) + " |")
    print("=")
    print(L @ U)


# -- Q1-3 : Décomposition LU forme matricielle (sans boucles internes) -- #
def LU_decomposition_mat(A):
    N = A.shape[0]
    L = np.zeros((N, N))
    U = np.eye(N)

    for h in range(N):
        L[h:, h] = A[h:, h] - L[h:, :h] @ U[:h, h]
        U[h, h+1:] = (A[h, h+1:] - L[h, :h] @ U[:h, h+1:]) / L[h, h]

    return L, U


# -- Q1-3 (suite) : Décomposition LU avec pivot partiel -- #
def LU_decomposition_pivot(A):
    N = A.shape[0]
    A = A.copy()
    L = np.zeros((N, N))
    U = np.eye(N)
    P = np.eye(N)

    for h in range(N):
        L[h:, h] = A[h:, h] - L[h:, :h] @ U[:h, h]

        m = h + np.argmax(np.abs(L[h:, h]))
        if m != h:
            A[[h, m]] = A[[m, h]]
            L[[h, m], :h] = L[[m, h], :h]
            P[[h, m]] = P[[m, h]]
            L[h:, h] = A[h:, h] - L[h:, :h] @ U[:h, h]

        U[h, h+1:] = (A[h, h+1:] - L[h, :h] @ U[:h, h+1:]) / L[h, h]

    return P, L, U


# ------------------- MAIN -------------------- #
if __name__ == "__main__":
    A = np.array([[2, 1, 1],
                  [4, 3, 3],
                  [8, 7, 9]], dtype=float)

    def q1():
        print("===== Q1-1 : LU avec boucles =====")
        L, U = LU_decomposition(A)
        print("L:\n", L)
        print("U:\n", U)
        print("L @ U:\n", L @ U)
        print(saut)
        print("===== Q1-2 : Vérification détaillée =====")
        L, U = LU_decomposition(A)
        afficher_verification(L, U, A)

    def q3():
        print("===== Q1-3a : LU matricielle =====")
        L, U = LU_decomposition_mat(A)
        print("L:\n", L)
        print("U:\n", U)
        print("L @ U:\n", L @ U)

    def q4():
        print("===== Q1-3b : LU avec pivot =====")
        P, L, U = LU_decomposition_pivot(A)
        print("P:\n", P)
        print("L:\n", L)
        print("U:\n", U)
        print("P @ A:\n", P @ A)
        print("L @ U:\n", L @ U)

    questions = {
        1: ("LU avec boucles (Crout)", q1),
        2: ("LU matricielle (sans boucles internes)", q3),
        3: ("LU avec pivot partiel", q4),
    }

    while True:
        print("\n" + "=" * 40)
        print("  TP2 - Décomposition LU")
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