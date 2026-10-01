import random
from time import sleep

def init(n, k):
    computer_list = []
    for i in range(n): 
        rand = random.randint(1, k)
        while rand in computer_list:
            rand = random.randint(1, k)
        computer_list.append(rand)
    return computer_list


def user_choice(n, k):
    user_entry_list = input(f"Entrez une liste de {n} valeurs entre 1 et {k}: ").split()
    while len(user_entry_list) != n: 
        print(f"Erreur de saisie ! Vous devez entrer {n} valeurs et non {len(user_entry_list)} valeurs !")
        user_entry_list = input(f"Entrez une liste de {n} valeurs entre 1 et {k}: ").split()
    user_list = []
    for i in user_entry_list:
        user_list.append(int(i))
    return user_list


def score(n, computer_list, user_list):
    good_answer_well_placed_counter = 0
    for i in range(n):
        if user_list[i] == computer_list[i]:
            good_answer_well_placed_counter += 1

    common = 0
    for i in range(n):
        found = False
        for j in range(n):
            if computer_list[i] == user_list[j]:
                found = True
        if found:
            common += 1
    good_answer_wrong_placed_counter = common - good_answer_well_placed_counter

    print(f"> {good_answer_well_placed_counter} valeur(s) bonne(s) et bien placée(s)\n> {good_answer_wrong_placed_counter} valeur(s) bonne(s) mais mal placée(s)\n")
    return good_answer_well_placed_counter


def toutes_possibilites(n, k):
    possibilites = [[]]
    for _ in range(k):
        nouvelles = []
        for comb in possibilites:
            for val in range(1, n+1):
                L = list(comb)
                L.append(val)
                nouvelles.append(L)
        possibilites = nouvelles
    return possibilites


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
    nbr_val = 0
    nbr_val = int(input("Combien de valeurs souhaitez-vous dans votre jeu ? "))
    while nbr_val > 5:
        print("Impossible : trop de valeurs demandées (5 maximum).")
        nbr_val = int(input("Combien de valeurs souhaitez-vous dans votre jeu ? "))

    max_val = int(input("Borne maximum des valeurs (ex: 9 → chiffres de 1 à 9): "))

    candidats = toutes_possibilites(max_val, nbr_val)
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

        if bien == nbr_val:
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
 
def main():
    choice = int(input("MASTERMINDDDD \n > (1): jouer \n > (2): faire deviner une combinaison \n > (0): quitter \nVotre choix: "))
    while choice == 0 or choice == 1 or choice == 2:
        if choice == 1: player_guess_mod()
        elif choice == 2: computer_guess_mod()
        else: 
            print("Au revoir !") 
            break
        choice = int(input("MASTERMINDDDD \n > (1): jouer \n > (2): faire deviner une combinaison \n > (0): quitter \nVotre choix: "))
        print("Erreur : veuillez entrer un nombre entier.")
        choice = int(input("MASTERMINDDDD \n > (1): jouer \n > (2): faire deviner une combinaison \n > (0): quitter \nVotre choix: "))
if __name__ == "__main__":
    main()