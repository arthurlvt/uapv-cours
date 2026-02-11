# EXERCICE 1

a = int(input("Entrez le premier entier : "))
b = int(input("Entrez le deuxième entier : "))

if a > b:
    print("plus grand =", a)
elif a < b:
    print("plus petit =", a)
else:
    print("égal")


# EXERCICE 2

L = int(input("Entrez la longueur : "))
l = int(input("Entrez la largeur : "))

if L > 0 and l > 0:
    if L >= l:
        print("Surface =", L * l)
    else:
        print("Données incohérentes")
else:
    print("Dimensions incorrectes")


# EXERCICE 3

a = int(input("Entrez a : "))
b = int(input("Entrez b : "))
c = int(input("Entrez c : "))
d = int(input("Entrez d : "))
e = int(input("Entrez e : "))
f = int(input("Entrez f : "))

nuls = 0
for x in [a, b, c, d, e, f]:
    if x == 0:
        nuls += 1

if nuls < 3:
    print("Saisie correcte")
else:
    print("Saisie incorrecte")
    

# EXERCICE 4

a = int(input("Entrez a : "))
b = int(input("Entrez b : "))
c = int(input("Entrez c : "))

x, y, z = sorted([a, b, c])
print("Ordre croissant :", x, y, z)


# EXERCICE 5

valeurs = []
for i in range(10):
    n = int(input(f"Entrez la valeur {i+1} : "))
    valeurs.append(n)

print("Plus petite valeur =", min(valeurs))
print("Plus grande valeur =", max(valeurs))
print("Moyenne =", sum(valeurs) / len(valeurs))


# EXERCICE 6

import math

x1 = int(input("x1 = "))
y1 = int(input("y1 = "))
x2 = int(input("x2 = "))
y2 = int(input("y2 = "))

d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print("Distance =", d)


# EXERCICE 7

import math

x1, y1 = int(input("x1 = ")), int(input("y1 = "))
x2, y2 = int(input("x2 = ")), int(input("y2 = "))
x3, y3 = int(input("x3 = ")), int(input("y3 = "))

d1 = (x2 - x1)**2 + (y2 - y1)**2
d2 = (x3 - x2)**2 + (y3 - y2)**2
d3 = (x1 - x3)**2 + (y1 - y3)**2

cotes = sorted([d1, d2, d3])

if cotes[0] + cotes[1] == cotes[2]:
    print("Triangle rectangle")
else:
    print("Pas un triangle rectangle")
    

# EXERCICE 8

op = input("Entrez une opération (+, -, *, /) : ")
a = int(input("Entrez la première opérande : "))
b = int(input("Entrez la deuxième opérande : "))

if op == "+":
    print("Résultat =", a + b)
elif op == "-":
    print("Résultat =", a - b)
elif op == "*":
    print("Résultat =", a * b)
elif op == "/":
    if b != 0:
        print("Résultat =", a // b)  # division entière
    else:
        print("Erreur : division par zéro")
else:
    print("Opération invalide")


# EXERCICE 9

import math

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

if a != 0:
    delta = b**2 - 4*a*c
    if delta > 0:
        x1 = (-b - math.sqrt(delta)) / (2*a)
        x2 = (-b + math.sqrt(delta)) / (2*a)
        print("Deux solutions réelles :", x1, x2)
    elif delta == 0:
        x = -b / (2*a)
        print("Solution unique :", x)
    else:
        print("Pas de solution réelle")
else:
    print("a doit être différent de 0")


# EXERCICE 10

n = input("Entrez un nombre à 4 chiffres : ")

if len(n) == 4 and n.isdigit():
    print(" - ".join(n))
else:
    print("Erreur : le nombre ne contient pas 4 chiffres")





