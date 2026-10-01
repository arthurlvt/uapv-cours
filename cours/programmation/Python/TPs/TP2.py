import math
saut = "\n"

def surfCercle(rayon):
    return math.pi * rayon ** 2


def maxNumberOf(first, second, third, fourth):
    temp = 0
    if first > second:
        temp = first
        first = second
        second = temp
    if first > third:
        temp = first
        first = third
        third = temp
    if first > fourth:
        temp = first
        first = fourth
        fourth = temp
    if second > third:
        temp = second
        second = third
        third = temp
    if second > fourth:
        temp = second
        second = fourth
        fourth = temp
    if third > fourth:
        temp = third
        third = fourth
        fourth = temp
    first, second, third, fourth = fourth, third, second, first
    return first


def discriminant(a, b, c):
    delta = b**2 - 4*a*c
    if delta > 0:
        root1 = (-b + delta**0.5) / (2*a)
        root2 = (-b - delta**0.5) / (2*a)
        return f"Le discriminant est positif : {delta} \n /> Il y a deux racines réelles distinctes: {root1:.2f}, {root2:.2f}"
    elif delta == 0:
        root = -b / (2*a)
        return f"Le discriminant est nul : {delta} \n /> Il y a une seule racine réelle: {root:.2f}"
    else:
        return f"Le discriminant est négatif : {delta} \n /> Il n'y a donc pas de racines réelles.", ()
    
def resoudre():
    a = float(input("Entrez le coefficient a: "))
    b = float(input("Entrez le coefficient b: "))
    c = float(input("Entrez le coefficient c: "))
    resultat = discriminant(a, b, c)
    print(resultat)

def affichage_resultat():
    resultat = resoudre()
    print("Résultat:", resultat)
    
def main():
    affichage_resultat()

"""
if __name__ == "__main__":
    main()
"""  
    
def months_to_reach_value():
    valeur_initiale = 57.0 
    taux_croissance = 0.03 # 3%
    valeur_ciblee = 200.0
    
    valeur_actuelle = valeur_initiale
    nombre_mois = 0
    
    while valeur_actuelle < valeur_ciblee:
        valeur_actuelle *= (1 + taux_croissance) # 3% increase
        nombre_mois += 1
        
    return nombre_mois


def months_to_reach_value_general(prix_initial, taux_mensuel, valeur_cible):
    if prix_initial <= 0 or taux_mensuel <= 0 or valeur_cible <= prix_initial: return 0 
        
    valeur_actuelle = prix_initial
    nombre_mois = 0
    
    while valeur_actuelle < valeur_cible:
        valeur_actuelle *= (1 + taux_mensuel)
        nombre_mois += 1
        
    return nombre_mois


def is_leap_year(annee):
    # Règle 3: divisible par 400
    if annee % 400 == 0: return True
    
    # Règle 2: divisible par 100 (mais pas par 400)
    if annee % 100 == 0: return False
        
    # Règle 1: divisible par 4 (et pas par 100)
    if annee % 4 == 0: return True
        
    return False


def identiques_à_epsilon(a, b, epsilon):
    return abs(a - b) < epsilon


def carrés_triangle_rectangle(c1, c2, c3):
    # Vérifie si le plus grand côté est identique à la somme des carrés des deux autres côtés
    if c1 <= 0 or c2 <= 0 or c3 <= 0: return False  # Les côtés doivent être positifs
    
    if(identiques_à_epsilon(c1**2, c2**2 + c3**2, 1e-6) or
       identiques_à_epsilon(c2**2, c1**2 + c3**2, 1e-6) or
       identiques_à_epsilon(c3**2, c1**2 + c2**2, 1e-6)): return True
    return False


def carrés_triangle_rectangle_general(c1, c2, c3, c4):
        # Vérifie 3 des longueur peuvent former un triangle rectangle
        return (carrés_triangle_rectangle(c1, c2, c3) or
                carrés_triangle_rectangle(c1, c2, c4) or
                carrés_triangle_rectangle(c1, c3, c4) or
                carrés_triangle_rectangle(c2, c3, c4))


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

choice = 0

while choice != -1:
    print("--- Test des fonctions ---")
    print("Calculer la surface d'un cercle (1)")
    print("Trouver le plus grand nombre parmi quatre (2)")
    print("Résoudre une équation quadratique (3)")
    print("Calculer le nombre de mois pour atteindre une valeur (4)")
    print("Vérifier si une année est bissextile (5)")
    print("Vérifier si trois côtés forment un triangle rectangle (6)")
    print("Vérifier si quatre côtés forment un triangle rectangle (7)")
    print("Vérifier si un nombre est premier (8)")
    print("Trouver le plus petit diviseur premier d'un nombre (9)")
    print("Décomposer un nombre en facteurs premiers (10)")
    print("Quitter (-1)")
    choice = int(input("Entrez votre choix: "))
    if choice == 1:
        rayon = float(input("Entrez le rayon d'un cercle C: "))
        print(f"La surface du cercle est: {surfCercle(rayon):.2f}")
    elif choice == 2:
        first = float(input("Entrez le premier nombre: "))
        second = float(input("Entrez le deuxième nombre: "))
        third = float(input("Entrez le troisième nombre: "))
        fourth = float(input("Entrez le quatrième nombre: "))
        print(f"Le plus grand nombre est: {maxNumberOf(first, second, third, fourth)}")
    elif choice == 3: resoudre()
    elif choice == 4:
        prix_initial = float(input("Entrez le prix initial: "))
        taux_mensuel = float(input("Entrez le taux de croissance mensuel (en décimal, ex: 0.03 pour 3%): "))
        valeur_cible = float(input("Entrez la valeur cible: "))
        mois = months_to_reach_value_general(prix_initial, taux_mensuel, valeur_cible)
        print(f"Nombre de mois pour atteindre la valeur cible: {mois}")
    elif choice == 5:
        annee = int(input("Entrez une année: "))
        if is_leap_year(annee):
            print(f"{annee} est une année bissextile.")
        else:
            print(f"{annee} n'est pas une année bissextile.")
    elif choice == 6:
        c1 = float(input("Entrez le premier côté: "))
        c2 = float(input("Entrez le deuxième côté: "))
        c3 = float(input("Entrez le troisième côté: "))
        if carrés_triangle_rectangle(c1, c2, c3):
            print("Ces côtés peuvent former un triangle rectangle.")
        else:
            print("Ces côtés ne peuvent pas former un triangle rectangle.")
    elif choice == 7:
        c1 = float(input("Entrez le premier côté: "))
        c2 = float(input("Entrez le deuxième côté: "))
        c3 = float(input("Entrez le troisième côté: "))
        c4 = float(input("Entrez le quatrième côté: "))
        if carrés_triangle_rectangle_general(c1, c2, c3, c4):
            print("Ces côtés peuvent former un triangle rectangle.")
        else:
            print("Ces côtés ne peuvent pas former un triangle rectangle.")
    elif choice == 8:
        n = int(input("Entrez un nombre: "))
        if est_premier(n):
            print(f"{n} est un nombre premier.")
        else:
            print(f"{n} n'est pas un nombre premier.")
    elif choice == 9:
        n = int(input("Entrez un nombre: "))
        diviseur = plus_petit_diviseur_premier(n)
        if diviseur is not None: # si n > 1
            print(f"Le plus petit diviseur premier de {n} est: {diviseur}")
        else:
            print(f"{n} n'a pas de diviseur premier (il est <= 1).")
    elif choice == 10:
        n = int(input("Entrez un nombre: "))
        decomposition = decomposition_en_facteurs_premiers(n)
        print(f"La décomposition en facteurs premiers de {n} est: {decomposition}")
    elif choice == -1:
        print("Au revoir!")