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

somme = 0
compte = 0
val_max = n
val_min = n

while n != 0:
    somme += n
    compte += 1

    if n > val_max:
        val_max = n
    if n < val_min:
        val_min = n

    n = int(input("Entrez un entier non nul (0 pour arrêter) : "))

if compte > 0:
    moyenne = somme / compte
    print("Moyenne :", moyenne)
    print("Max :", val_max)
    print("Min :", val_min)
else:
    print("Aucune valeur saisie.")


# EXERCICE 4

somme_pairs = 0
nb_pairs = 0
somme_impairs = 0
nb_impairs = 0

n = int(input("Entrez un entier (0 pour arrêter) : "))

while n != 0:
    if n % 2 == 0:
        somme_pairs += n
        nb_pairs += 1
    else:
        somme_impairs += n
        nb_impairs += 1

    n = int(input("Entrez un entier (0 pour arrêter) : "))

if nb_pairs > 0:
    print("Moyenne des pairs :", somme_pairs / nb_pairs)
else:
    print("Aucun nombre pair saisi.")

if nb_impairs > 0:
    print("Moyenne des impairs :", somme_impairs / nb_impairs)
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
for i in range(1, n + 1):
    fact *= i

print(f"{n}! = {fact}")


# Exercice 9 : Vérifier si deux entiers sont premiers et afficher les nombres premiers entre eux

def nb_premier(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

# Saisie des deux entiers
a = int(input("Entrez un premier entier positif : "))
b = int(input("Entrez un deuxième entier positif : "))

# Vérification premier/pas premier pour chaque nombre
if nb_premier(a):
    print(f"{a} est PREMIER")
else:
    print(f"{a} n'est PAS PREMIER")

if nb_premier(b):
    print(f"{b} est PREMIER")
else:
    print(f"{b} n'est PAS PREMIER")

# Inversion si nécessaire
if a > b:
    a, b = b, a

# Affichage des nombres premiers dans l'intervalle
print(f"Nombres premiers entre {a} et {b} :")
for i in range(a, b + 1):
    if est_premier(i):
        print(i, end=" ")
print()