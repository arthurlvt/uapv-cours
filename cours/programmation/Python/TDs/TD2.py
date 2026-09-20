# EXERCICE 1
a = int(input("Veuillez entrer un nombre entier entre 0 et 100 exclus : "))

while a <= 0 or a >= 100:
    a = int(input("Veuillez entrer un nombre entier entre 0 et 100 exclus : "))

print(f"Merci pour le nombre {a}")


# EXERCICE 2
a = int(input("Veuillez entrer un nombre entier entre 2 et 9 : "))

while a < 2 or a > 9:
    a = int(input("Veuillez entrer un nombre entier entre 2 et 9 : "))

for i in range(1, 11):
    print(f"{a} x {i} = {a * i}")


# EXERCICE 3
n = int(input("Entrez un entier non nul (0 pour arrêter) : "))

sum = 0
count = 0
val_max = n
val_min = n

while n != 0:
    sum += n
    count += 1

    if n > val_max:
        val_max = n
    if n < val_min:
        val_min = n

    n = int(input("Entrez un entier non nul (0 pour arrêter) : "))

if count > 0:
    moyenne = sum / count
    print("Moyenne :", moyenne)
    print("Max :", val_max)
    print("Min :", val_min)
else:
    print("Aucune valeur saisie.")


# EXERCICE 4

sum_even = 0
count_even = 0
sum_odd = 0
count_odd = 0

n = int(input("Entrez un entier (0 pour arrêter) : "))

while n != 0:
    if n % 2 == 0:
        sum_even += n
        count_even += 1
    else:
        sum_odd += n
        count_odd += 1

    n = int(input("Entrez un entier (0 pour arrêter) : "))

if count_even > 0:
    print("Moyenne des pairs :", sum_even / count_even)
else:
    print("Aucun nombre pair saisi.")

if count_odd > 0:
    print("Moyenne des impairs :", sum_odd / count_odd)
else:
    print("Aucun nombre impair saisi.")


# EXERCICE 5

import random

total_coups = 0
parties = 0

while True:
    juste_prix = random.randint(1, 100)
    coups = 0
    trouve = False

    while not trouve:
        nombre = int(input("Entrez un nombre : "))
        coups += 1
        if nombre > juste_prix:
            print("C'est inférieur !")
        elif nombre < juste_prix:
            print("C'est supérieur !")
        else:
            print(f"BRAVO ! Trouvé en {coups} coups.")
            trouve = True

    total_coups += coups
    parties += 1
    choix = input("Voulez-vous rejouer ? (o/n) : ").lower()
    if choix != "o":
        print(f"Moyenne de coups par partie : {total_coups / parties:.2f}")
        print("À bientôt !")
        break


# EXERCICE 6: Rectangle

largeur = int(input("Entrez la largeur : "))
hauteur = int(input("Entrez la hauteur : "))

for i in range(hauteur):
    if i == 0 or i == hauteur - 1:   # première ou dernière ligne
        print("*" * largeur)
    else:  # lignes du milieu
        print("*" + " " * (largeur - 2) + "*")


# Exercice 7 : Dessiner X avec des *

taille = 0
while taille < 15 or taille > 20 or taille % 2 == 0:
    taille = int(input("Entrez une taille impaire entre 15 et 20 : "))

for i in range(taille):
    ligne = ""
    for j in range(taille):
        if j == i or j == (taille - 1 - i):
            ligne += "*"
        else:
            ligne += " "
    print(ligne)


# Exercice 8 : Factorielle

n = int(input("Entrez un entier n >= 0 : "))

fact = 1
for i in range(1, n + 1): fact *= i

print(f"{n}! = {fact}")


# Exercice 9 : Vérifier si deux entiers sont premiers et afficher les nombres premiers entre eux SANS FONCTIONS

a = int(input("Entrez le premier entier : "))
b = int(input("Entrez le deuxième entier : "))

nb_diviseurs = 0
for d in range(1, a+1):
    if a % d == 0:
        nb_diviseurs += 1
if nb_diviseurs == 2:
    print(f"{a} est premier")
else:
    print(f"{a} n'est pas premier")

nb_diviseurs = 0
for d in range(1, b+1):
    if b % d == 0:
        nb_diviseurs += 1
if nb_diviseurs == 2:
    print(f"{b} est premier")
else:
    print(f"{b} n'est pas premier")
    
if a > b:
    temp = a
    a = b
    b = temp
for n in range(a, b + 1):
    nb_diviseurs = 0
    for i in range(1, n + 1): 
        if n % i == 0: 
            nb_diviseurs += 1
    if nb_diviseurs == 2: 
        print(n, end=" ")