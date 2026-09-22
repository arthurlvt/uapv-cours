import math


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

if __name__ == "__main__":
    main()
    
    
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