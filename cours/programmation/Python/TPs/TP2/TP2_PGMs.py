import math
saut = "\n"


# EXERCICE 1 : calcul et résolution d'un polynome du second ordre de la forme ax^2 + bx + c = 0

def discriminant(a, b, c):
    return b**2 - 4*a*c
    
def resoudre():
    a = float(input("Entrez le coefficient a: "))
    b = float(input("Entrez le coefficient b: "))
    c = float(input("Entrez le coefficient c: "))
    delta = discriminant(a, b, c)
    if a == 0:
        if b == 0:
            if c == 0:
                return "L'équation est indéterminée (tous les réels sont solutions)."
            else:
                return "L'équation est impossible (aucune solution)."
        else:
            x = -c / b
            return f"L'équation est linéaire. La solution est x = {x:.2f}"
    else:
        if delta > 0:
            root1 = (-b + delta**0.5) / (2*a)
            root2 = (-b - delta**0.5) / (2*a)
            return f"Le discriminant est positif : {delta} \n /> Il y a deux racines réelles distinctes: {root1:.2f}, {root2:.2f}"
        elif delta == 0:
            root = -b / (2*a)
            return f"Le discriminant est nul : {delta} \n /> Il y a une seule racine réelle: {root:.2f}"
        else:
            return f"Le discriminant est négatif : {delta} \n /> Il n'y a donc pas de racines réelles.", ()
        
def affichage_resultat():
    resultat = resoudre()
    print("Résultat:", resultat)
    
def main():
    affichage_resultat()

"""
if __name__ == "__main__":
    main()
"""


# EXERCICE 2: Vérifier si un nombre est premier et afficher les nombres premiers entre eux SANS FONCTIONS

def est_premier(n):
    if n <= 1: return False
    for i in range(2, int(n**0.5) + 1): 
        if n % i == 0: return False
    return True


def plus_petit_diviseur_premier(n):
    if n <= 1: return None
    for i in range(2, n + 1):
        if n % i == 0 and est_premier(i): return i
    return None


def decomposition_en_facteurs_premiers(n):
    if n <= 1: return str(n)    
    temp_n = n  
    chaine = ""
    while temp_n > 1:
        d = plus_petit_diviseur_premier(temp_n) # trouver le plus petit diviseur premier de temp_n
        if chaine != "": chaine += " x " # ajouter un séparateur si ce n'est pas le premier facteur
        chaine += str(d) # ajouter le diviseur premier à la chaîne
        temp_n //= d # mettre à jour temp_n en le divisant par le diviseur premier trouvé
        
    return chaine


# EXERCICE 3 : Jeu avec nombre mystère

def generate_random_number():
    import random
    max = int(input("Entrez la valeur maximale pour le nombre mystère : "))
    min = int(input("Entrez la valeur minimale pour le nombre mystère : "))
    return random.randint(min, max)

def guess_number():
    number_to_guess = generate_random_number()
    guess = None
    attempts = 0
    max_attempts = int(input("Entrez la limite de tentatives : "))  # Limite de tentatives

    while guess != number_to_guess and attempts < max_attempts:
        guess = int(input("Devinez le nombre mystère : "))
        attempts += 1
        if guess < number_to_guess:
            print("Trop petit !")
        elif guess > number_to_guess:
            print("Trop grand !")
        else:
            print(f"Félicitations ! Vous avez trouvé le nombre mystère {number_to_guess} en {attempts} tentatives.")
    if attempts >= max_attempts:
        print(f"Vous avez atteint la limite de tentatives. Le nombre mystère était {number_to_guess}.")
        
        
# EXERCICE 4 : factorielle, coefficient binomial et triangle de pascal

def factorielle(n):
    if n < 0: raise ValueError("La factorielle n'est pas définie pour les nombres négatifs.")
    elif n == 0 or n == 1: return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
    
def coef_binomial(n, k):
    if k < 0 or k > n: raise ValueError("k doit être compris entre 0 et n.")
    return factorielle(n) // (factorielle(k) * factorielle(n - k))

def triangle_pascal(n): # afficher le triangle de pascal sous sa forme originelle que du côté droit (demi triangle)
    for i in range(n):
        for j in range(i + 1):
            print(coef_binomial(i, j), end=" ")
        print()
        
# application de la formule: (a+b)^4 = a^4 + 4a^3b + 6a^2b^2 + 4ab^3 + b^4:
