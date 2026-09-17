# EXERCICE 1

a = int(input("Entrez le premier entier : "))
b = int(input("Entrez le deuxième entier : "))

if a > b:
    print("valeur la plus grande: ", a)
elif a < b:
    print("valeur la plus petite: ", b)
else:
    print("Les 2 valeurs sont strictement égales")

# EXERCICE 2

L = int(input("Entrez la longueur : "))
l = int(input("Entrez la largeur : "))

if L > 0 and l > 0:
    if L >= l:
        print("Surface :", L * l)
    else:
        print("Données incohérentes")
else:
    print("Dimensions incorrectes")


# EXERCICE 3 (sans boucle)

a = int(input("Entrez a : "))
b = int(input("Entrez b : "))
c = int(input("Entrez c : "))
d = int(input("Entrez d : "))
e = int(input("Entrez e : "))
f = int(input("Entrez f : "))
count = 0

if a == 0: count += 1
if b == 0: count += 1
if c == 0: count += 1
if d == 0: count += 1
if e == 0: count += 1
if f == 0: count += 1

if count >= 3:
    print("La saisie est correcte!")
else:
    print("La saisie est incorrecte!")
    
    
# EXERCICE 4

a = int(input("Veuillez entrer le premier entier a: "))
b = int(input("Veuillez entrer un deuxième entier b: "))
c = int(input("Veuillez entrer le troisième entier c: "))

if a > b:
	a, b = b, a
if a > c:
	a, c = c, a
if b > c:
	b, c = c, b
if a == b == c:
	print("les 3 sont égaux")
else:
	print(f"Ordre: {a}, {b}, {c}")


# EXERCICE 4 (deuxieme méthode)
print("Sachant que a, b et c sont respectivement affichés dans l'ordre a <= b <= c : \n")
a = int(input("Entrez a : "))
b = int(input("Entrez b : "))
c = int(input("Entrez c : "))

temp = 0

if b < a:
    temp = a
    a = b
    b = temp
if c < b:
    temp = b
    b = c
    c = temp
if b < a:
    temp = a
    a = b
    b = temp

print(a, "<=", b, "<=", c)


# EXERCICE 5 (sans boucles ni fonctions natives)

somme = 0
max = -1000
min = 1000
mean = 0
count = 0

val = int(input("entrez une valeur: "))
mean += val
somme += val
if val < min: min = val
if val > max: max = val
count += 1
val = int(input("entrez une valeur: "))
mean += val
somme += val
if val < min: min = val
if val > max: max = val
count += 1
val = int(input("entrez une valeur: "))
mean += val
somme += val
if val < min: min = val
if val > max: max = val
count += 1
val = int(input("entrez une valeur: "))
mean += val
somme += val
if val < min: min = val
if val > max: max = val
count += 1
val = int(input("entrez une valeur: "))
mean += val
somme += val
if val < min: min = val
if val > max: max = val
count += 1
val = int(input("entrez une valeur: "))
mean += val
somme += val
if val < min: min = val
if val > max: max = val
count += 1
val = int(input("entrez une valeur: "))
mean += val
somme += val
if val < min: min = val
if val > max: max = val
count += 1
val = int(input("entrez une valeur: "))
mean += val
somme += val
if val < min: min = val
if val > max: max = val
count += 1
val = int(input("entrez une valeur: "))
mean += val
somme += val
if val < min: min = val
if val > max: max = val
count += 1
val = int(input("entrez une valeur: "))
mean += val
somme += val
if val < min: min = val
if val > max: max = val
count += 1
print(f"nombre de valeurs: {count} \n valeur maximum: {max} \n valeur minimum: {min}")


# EXERCICE 5 (méthode classique)

valeurs = []
for i in range(10):
    n = int(input(f"Entrez la valeur {i+1} : "))
    valeurs.append(n)

print("Plus petite valeur =", min(valeurs))
print("Plus grande valeur =", max(valeurs))
print("Moyenne =", sum(valeurs) / len(valeurs))


# EXERCICE 6

import math

ax = int(input("ax = "))
ay = int(input("ay = "))
bx = int(input("bx = "))
by = int(input("by = "))

d = math.sqrt((ax - bx)**2 + (ay - by)**2)
print("Distance: ", d, "u.a")


# EXERCICE 7 : méthode classique

import math

ax, ay = int(input("ax: ")), int(input("ay: "))
bx, by = int(input("bx: ")), int(input("by: "))
cx, cy = int(input("cx: ")), int(input("cy: "))

d1 = (bx - ax)**2 + (by - ay)**2
d2 = (cx - bx)**2 + (cy - by)**2
d3 = (ax - cx)**2 + (ay - cy)**2

a = d1
b = d2
c = d3

if a > b: 
    a, b = b, a
if a > c: 
    a, c = c, a
if b > c: 
    b, c = c, b
if a == b == c: 
    print("les 3 côtés sont égaux")
else:
    if a == b + c:
        print("ce triangle est rectangle")
    else:
        print("ce triangle n'est pas rectangle")  


# EXERCICE 7: méthode avec fonctions natives

import math

ax, ay = int(input("ax: ")), int(input("ay: "))
bx, by = int(input("bx: ")), int(input("by: "))
cx, cy = int(input("cx: ")), int(input("cy: "))

d1 = (bx - ax)**2 + (by - ay)**2
d2 = (cx - bx)**2 + (cy - by)**2
d3 = (ax - cx)**2 + (ay - cy)**2

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


# EXERCICE 10 : méthode classique

n = input("Entrez un nombre à 4 chiffres: ")
if n > 999 and n < 1000:
    print("premier chiffre: ", n // 1000)
    print("deuxième chiffre: ", (n // 100) % 10)
    print("troisième chiffre: ", (n // 10) % 10)
    print("quatrième chiffre: ", n % 10)
else: 
    print("Erreur: le nombre n'est pas à 4 chiffres")


# EXERCICE 10 : méthode native

n = input("Entrez un nombre à 4 chiffres : ")

if len(n) == 4 and n.isdigit():
    print(" - ".join(n))
else:
    print("Erreur : le nombre ne contient pas 4 chiffres")