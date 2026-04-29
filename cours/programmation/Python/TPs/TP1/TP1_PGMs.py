# EXERCICE 1
a = int(input("Veuillez entrer un entier a: "))
b = int(input("Veuillez entrer un entier b: "))

if a > b:
	print(f"{a} > {b}")
elif a < b:
	print(f"{a} < {b}")
else:
	print(f"{a} = {b}")

----------------------------------------------------------------------

# EXERCICE 2
longueurL = int(input("Veuillez entrer une longueur L: "))
largeurl = int(input("Veuillez entrer une largeur l: "))

if longueurL >= largeurl:
	print(f"Surface du rectangle : {longueurL * largeurl}m2")
else:
	print("La longueur doit être supérieure ou égale à la largeur !")

----------------------------------------------------------------------

# EXERCICE 3

entier1 = int(input("Veuillez entrer le premier entier: "))
entier2 = int(input("Veuillez entrer un deuxième entier: "))
entier3 = int(input("Veuillez entrer le troisième entier: "))
entier4 = int(input("Veuillez entrer un quatrième entier: "))
entier5 = int(input("Veuillez entrer le cinquième entier: "))
entier6 = int(input("Veuillez entrer un sixième entier: "))
somme = 0 

if entier1 <= 0:
	somme=+ 1
if entier2 <= 0:
	somme =+ 1
if entier3 <= 0:
	somme =+ 1
if entier4 <= 0:
	somme =+ 1
if entier5 <= 0:
	somme =+ 1
if entier6 <= 0:
	somme =+ 1

if sum <= 3:
	print("La saisie est incorrecte !")
else:
	print("La saisie est correcte")

----------------------------------------------------------------------

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

----------------------------------------------------------------------

# EXERCICE 5

val = int(input("Entrez une valeur et -1 pour arreter: "))
minimum = val
maximum = val
somme = val
compteur = 0

while True:
	val = int(input("Entrez une valeur et -1 pour arreter: "))
	if val == -1:
		break
	if val < minimum:
		minimum = val
	if val > maximum:
		maximum = val

somme = somme + val
compteur = compteur + 1
moyenne = somme / compteur

print(f"min: {minimum}, max: {maximum}, moyenne: {moyenne}")

----------------------------------------------------------------------

# EXERCICE 6

x1 = int(input("Entrez x1: "))
y1 = int(input("Entrez y1 :"))
x2 = int(input("Entrez x2: "))
y2 = int(input("Entrez y2 :"))

dist_x = (x1 - x2)
dist_y = (y1 - y2)


distance = ((dist_x**2 + dist_y**2)**0,5)*2

print(distance)

----------------------------------------------------------------------

# EXERCICE 7

x1 = int(input("Entrez x1: "))
y1 = int(input("Entrez y1: "))
x2 = int(input("Entrez x2: "))
y2 = int(input("Entrez y2: "))
x3 = int(input("Entrez x3: "))
y3 = int(input("Entrez y3: "))

cote1 = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
cote2 = ((x2 - x3)**2 + (y2 - y3)**2)**0.5
cote3 = ((x1 - x3)**2 + (y1 - y3)**2)**0.5

if cote1**2 + cote2**2 == cote3**2:
	print("Le triangle est rectangle")
else:
	print("Le triangle n'est pas rectangle")

----------------------------------------------------------------------

# EXERCICE 8

operande_choice = input("Entrez un mode d'opération: ")
operateur1 = int(input("Entrez l'opérateur 1: "))
operateur2 = int(input("Entrez l'opérateur 2: "))

if operande_choice == "/":
	print(f"Opération: {operateur1 / operateur2}")
elif operande_choice == "*":
	print(f"Opération: {operateur1 * operateur2}")
elif operande_choice == "+":
	print(f"Opération: {operateur1 - operateur2}")
elif operande_choice == "-":
	print(f"Opération: {operateur1 - operateur2}")
else:
	print("erreur")

----------------------------------------------------------------------

# EXERCICE 9

a = int(input("Entrez a: "))
b = int(input("Entrez b: "))
c = int(input("Entrez c: "))
delta = 0
delta_nul = -b /(2 * a)
delta_positif_1 = (-b - delta**0.5)/(2 * a)
delta_positif_2 = (-b + delta**0.5)/(2 * a)

if a != 0:
	delta = (b**2) - (4 * a * c)
	if delta == 0:
		print(f"Une solution: {delta_nul}")
	if delta > 0:
		print(f"Deux solutions: {delta_positif_1} et {delta_positif_2}")
	else:
		print("Aucune solutions pour cette équation car delta < 0")

----------------------------------------------------------------------

# EXERCICE 10

ombre = int(input("Entrez un nombre à 4 chiffres: "))

while nombre < 1000 or nombre > 9999:
	print("Le nombre ne contient pas 4 chiffres")
	
print("Ok!")

nb1 = nombre // 1000
nb2 = nombre % 1000
nb3 = nombre % 100
nb4 = nombre % 10

print(nb1, nb2, nb3, nb4)
