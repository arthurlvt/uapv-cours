import random

# ---------- FONCTIONS COMMUNES ----------

def score(H, R):
    """Renvoie (bien placés, mal placés)"""
    bien_places = 0
    mal_places = 0
    H_copy = list(H)
    R_copy = list(R)

    # Compter bien placés
    for i in range(len(H)):
        if H[i] == R[i]:
            bien_places += 1
            H_copy[i] = R_copy[i] = None

    # Compter mal placés
    for i in range(len(H)):
        if R_copy[i] is not None and R_copy[i] in H_copy:
            mal_places += 1
            H_copy[H_copy.index(R_copy[i])] = None

    return bien_places, mal_places


def toutes_possibilites(n, longueur):
    possibilites = [[]]
    for _ in range(longueur):
        nouvelles = []
        for comb in possibilites:
            for val in range(1, n+1):
                L = list(comb)
                L.append(val)
                nouvelles.append(L)
        possibilites = nouvelles
    return possibilites


# ---------- MODE 1 : UTILISATEUR DEVINE ----------

def mode_utilisateur_devine():
    k = int(input("Valeur maximale autorisée (par ex. 9): "))
    longueur = int(input("Longueur de la combinaison: "))

    # Génération combinaison secrète
    secret = [random.randint(1, k) for _ in range(longueur)]

    print("\nJ'ai choisi une combinaison secrète. A toi de la deviner !\n")

    while True:
        # Proposition joueur
        prop = []
        for i in range(longueur):
            val = int(input(f"Entrez la valeur {i+1} : "))
            prop.append(val)

        bien, mal = score(secret, prop)
        print(f"Bien placés : {bien}, Mal placés : {mal}")

        if bien == longueur:
            print("🎉 Bravo, tu as trouvé !")
            break


# ---------- MODE 2 : ORDINATEUR DEVINE ----------

def mode_ordinateur_devine():
    longueur = 0
    while longueur <= 0 or longueur > 6:
        longueur = int(input("Merci d'entrer une longueur (1 à 6): "))

    n = int(input("Borne maximum des valeurs (ex: 9 → chiffres de 1 à 9): "))

    candidats = toutes_possibilites(n, longueur)
    Ens_H = []
    Scores_H = []

    print("\nPensez à une combinaison secrète (ne la tapez pas).")
    print("Je vais essayer de la deviner. À chaque fois que je propose,")
    print("vous devez indiquer le nombre de bien placés et de mal placés.\n")

    while True:
        if not candidats:
            print("Oups, plus de candidats possibles. Vérifiez vos réponses !")
            break
        
        H = candidats[0]
        print(f"Je propose : {H}")

        bien = int(input("Nombre de bien placés : "))
        mal = int(input("Nombre de mal placés : "))

        if bien == longueur:
            print("🎉 J'ai trouvé votre combinaison !")
            break

        Ens_H.append(H)
        Scores_H.append((bien, mal))

        nouveaux_candidats = []
        for cand in candidats:
            valide = True
            for i in range(len(Ens_H)):
                if score(cand, Ens_H[i]) != Scores_H[i]:
                    valide = False
                    break
            if valide:
                nouveaux_candidats.append(cand)

        candidats = nouveaux_candidats


# ---------- PROGRAMME PRINCIPAL ----------

def main():
    print("Bienvenue dans le Mastermind !")
    print("1. Tu devines la combinaison de l’ordinateur")
    print("2. L’ordinateur devine ta combinaison")

    choix = 0
    while choix not in (1, 2):
        choix = int(input("Choisis 1 ou 2 : "))

    if choix == 1:
        mode_utilisateur_devine()
    else:
        mode_ordinateur_devine()


# Lancement
main()
