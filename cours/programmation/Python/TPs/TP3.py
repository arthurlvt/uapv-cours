import random
import time

def contented(L, val):
    for i in range(len(L)):
        if L[i] == val:
            return True
    return False

def init(n, k):
    computer_list = []
    for i in range(n):
        rand = random.randint(1, k)
        j = 0
        while j < len(computer_list):
            if rand == computer_list[j]:
                rand = random.randint(1, k)
                j = 0
            else:
                j += 1
        computer_list.append(rand)
    return computer_list


def user_choice(n, k):
    user_entry_list = input(f"Entrez {n} valeurs à la suite entre 1 et {k}: ").split()
    while len(user_entry_list) != n:
        print(f"Erreur de saisie ! Vous devez entrer {n} valeurs et non {len(user_entry_list)} valeurs !")
        user_entry_list = input(f"Entrez une liste de {n} valeurs entre 1 et {k}: ").split()
    user_list = []
    for i in range(n):
        user_list.append(int(user_entry_list[i]))
    return user_list


def evaluer(n, secret, essai):
    well_placed = 0
    for i in range(n):
        if essai[i] == secret[i]:
            well_placed += 1

    common = 0
    for i in range(n):
        found = False
        for j in range(n):
            if secret[i] == essai[j]:
                found = True
        if found:
            common += 1

    return (well_placed, common - well_placed)


def score(n, computer_list, user_list):
    well_placed, mal = evaluer(n, computer_list, user_list)
    print(f"> {well_placed} valeur(s) bonne(s) et bien placée(s)\n> {mal} valeur(s) bonne(s) mais mal placée(s)\n")
    return well_placed


def toutes_possibilites(max_val, nbr_val):
    print("Calcul de toutes les possibilités en cours...")
    start_time = time.perf_counter()
    possibilities = [[]]
    nbr_possibilities = max_val ** nbr_val
    for _ in range(nbr_val):
        new_possibility = []
        for comb in possibilities:
            for val in range(1, max_val + 1):
                already = False
                for j in range(len(comb)):
                    if comb[j] == val:
                        already = True
                if not already:
                    L = list(comb)
                    L.append(val)
                    new_possibility.append(L)
        possibilities = new_possibility
    end_time = time.perf_counter()
    print(f"Calcul terminé en {end_time - start_time:.2f} secondes pour {nbr_possibilities} combinaisons possibles.")
    return possibilities


def chiffres_differents(L):
    for i in range(len(L)):
        for j in range(i + 1, len(L)):
            if L[i] == L[j]:
                return False
    return True


def guess(longueur, n):
    candidats = toutes_possibilites(n, longueur)
    tries = 0

    while len(candidats) > 0:
        H = candidats[0]
        tries += 1
        print(f"Essai {tries} : je propose {H}")
        good_well_placed = int(input("Nombre de bien placés : "))
        good_wrong_placed    = int(input("Nombre de mal placés : "))

        if good_well_placed == longueur:
            return H, tries

        new_candidats = []
        for c in range(len(candidats)):
            if evaluer(longueur, candidats[c], H) == (good_well_placed, good_wrong_placed):
                new_candidats.append(candidats[c])
        candidats = new_candidats

    print("Plus aucun candidat possible : il y a une erreur dans les réponses.")
    return None, tries


def player_guess_mod():
    nbr_val = int(input("Combien de valeurs souhaitez-vous dans votre jeu ? "))
    while nbr_val > 10:
        print("Impossible : trop de valeurs demandées.")
        nbr_val = int(input("Combien de valeurs souhaitez-vous dans votre jeu ? "))
    max_val = random.randint(10, 20)
    computer_list = init(nbr_val, max_val)

    lose_counter = 0
    max_try = 10
    while lose_counter < max_try:
        user_list = user_choice(nbr_val, max_val)
        if score(nbr_val, computer_list, user_list) == nbr_val:
            print(f"Bravo, vous avez gagné en {lose_counter + 1} essai(s) !")
            return
        lose_counter += 1
        print(f"Il vous reste {max_try - lose_counter} essai(s).")

    print(f"Perdu ! La combinaison était {computer_list}")


def computer_guess_mod():
    nbr_val = int(input("Combien de valeurs souhaitez-vous dans votre jeu ? "))
    while nbr_val > 10:
        print("Impossible : trop de valeurs demandées (10 maximum).")
        nbr_val = int(input("Combien de valeurs souhaitez-vous dans votre jeu ? "))

    max_val = int(input("Borne maximum des valeurs (ex: 9 → chiffres de 1 à 9): "))
    while max_val < nbr_val:
        print(f"La borne doit être au moins {nbr_val} (valeurs toutes différentes).")
        max_val = int(input("Borne maximum des valeurs : "))

    candidats = toutes_possibilites(max_val, nbr_val)
    Ens_H = []
    Scores_H = []

    print("\nPensez à une combinaison secrète de valeurs toutes différentes (ne la tapez pas).")
    print("Je vais essayer de la deviner. À chaque fois que je propose,")
    print("vous devez indiquer le nombre de bien placés et de mal placés.\n")

    while True:
        if len(candidats) == 0:
            print("Oups, plus de candidats possibles. Vérifiez vos réponses !")
            break

        H = candidats[0]
        print(f"Je propose : {H}")

        bien = int(input("Nombre de bien placés : "))
        mal = int(input("Nombre de mal placés : "))

        if bien == nbr_val:
            print("J'ai trouvé votre combinaison !")
            break

        Ens_H.append(H)
        Scores_H.append((bien, mal))

        nouveaux_candidats = []
        for c in range(len(candidats)):
            cand = candidats[c]
            valide = True
            for i in range(len(Ens_H)):
                if evaluer(nbr_val, cand, Ens_H[i]) != Scores_H[i]:
                    valide = False
            if valide:
                nouveaux_candidats.append(cand)

        candidats = nouveaux_candidats


def main():
    menu = "MASTERMINDDDD \n > (1): jouer \n > (2): faire deviner une combinaison \n > (0): quitter \nVotre choix: "
    while True:
        choice = int(input(menu))
        if choice == 1:
            player_guess_mod()
        elif choice == 2:
            computer_guess_mod()
        elif choice == 0:
            print("Au revoir !")
            break
        else:
            print("Choix invalide : entrez 0, 1 ou 2.")


if __name__ == "__main__":
    main()