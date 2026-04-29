""" PROGRAMME TP3 - Mastermind simplifié """

import random

valeur1 = 0  # bien placés
valeur2 = 0  # mal placés


def Init(n, k):
    tab = []
    for i in range(n):
        tab.append(random.randint(0, k))
    return tab


def saisir_proposition(n):
    tab = []
    for i in range(n):
        valeur = int(input(f"Entrez la valeur {i} : "))
        tab.append(valeur)
    return tab


def Score(n, H, R):
    global valeur1, valeur2
    valeur1 = 0  # bien placés
    valeur2 = 0  # mal placés

    for i in range(n):
        if H[i] == R[i]:
            valeur1 += 1
        else:
            valeur2 += 1


def play():
    k = 9 
    n = int(input("Entrez la taille de la liste : "))

    while True:
        H = Init(n, k) 
        print("Liste H (aléatoire) :", H)

        R = saisir_proposition(n)
        Score(n, H, R)

        print(f"Nombre de valeurs bien placées : {valeur1}")
        print(f"Nombre de valeurs mal placées : {valeur2}")

        replay = input("Voulez-vous rejouer ? (o/n) : ")
        if replay.lower() != "o":
            print("Merci d'avoir joué, à bientôt !")
            break

play()
