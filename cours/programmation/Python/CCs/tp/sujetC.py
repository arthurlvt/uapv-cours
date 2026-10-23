from random import randint as rand

def exo1():
    a = int(input("Entrez une 1ère valeur: "))
    b = int(input("Entrez une 2ème valeur: "))
    c = int(input("Entrez une 3ème valeur: "))
    temp = 0

    if a == b == c: print("Les 3 valeurs sont égales")
    else:
        if a > b:
            temp = a
            a = b
            b = temp
        if a > c:
            temp = a
            a = c
            c = temp
        if b > c:
            temp = b
            b = c
            c = temp
        print(a, b, c)

def exo2():
    opperande = input("Entrez une opérande: (/), (%), (^) (*), (+), (-): ")
    while opperande != "/" or opperande != "//" or opperande != "*" or opperande != "+" or opperande != "-":
        opperande = input("Erreur! Oppérande inconnue \n Entrez une opérande va: (/), (*), (+), (-): ")
    a = int(input("Entrez un premier entier : "))
    b = int(input("Entrez un deuxieme entier: "))
    if opperande == "/" or "//" or "%":
        if b == 0: print("Erreur: La division par 0 est impossible")
        if opperande == "/" or opperande == "//": print(f"Le résultat de {a} / {b} = {a / b}")
        if opperande == "%": print(f"Le résultat de {a} % {b} = {a % b}")
    if opperande == "*": print(f"Le résultat de {a} * {b} = {a * b}")
    if opperande == "+": print(f"Le résultat de {a} + {b} = {a + b}")
    if opperande == "-": print(f"Le résultat de {a} - {b} = {a - b}")

def exo3():
    tab = []
    temp = 0
    val = 10
    palindrome = False
    nbr = int(input("Entrez un nombre à 3 digits: "))
    for i in range(3):
        temp = nbr % val
        nbr -= temp
        tab.append(temp)
        val = val * 10
    if nbr != 0: print("Erreur, votre nombre contenait + de 3 chiffres")
    if tab == tab[: -1]: palindrome = True
    print(palindrome)
        