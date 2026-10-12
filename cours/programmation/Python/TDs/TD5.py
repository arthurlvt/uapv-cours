 # EXERCICE 1
"""
Cette boucle donne la parité d'un nombre x :
    |-> si x vaut 2, 4, 6, 8 : le programme renvoie pair
    |-> si x vaut 3 ou 9 : le programme renvoie triple
    |-> sinon (1, 5, 7) : le programme renvoie impair
Si x = 6, le programme renvoie donc pair
"""

# EXERCICE 2
def abondant(n):
    somme = 0
    diviseur = n - 1
    while diviseur >= 1:
        if n % diviseur == 0:
            somme += diviseur
        diviseur -= 1
    return somme > n
print(abondant(12), abondant(28))


# EXERCICE 3
def abondant_liste(L):
    L_fini = []
    for i in range(len(L)):
        if abondant(L[i]):
            somme = 0
            diviseur = L[i] - 1
            while diviseur >= 1:
                if L[i] % diviseur == 0: somme += diviseur
                diviseur -= 1
            L_fini.append(somme)
    return L_fini
print(abondant_liste([10, 12, 18, 20]))
    

# EXERCICE 4
def position_min(L):
    if len(L) == 0: return None
    index = 0
    i = 1
    while i < len(L):
        if L[i] < L[index]:
            index = i
        i += 1
    return index

print(position_min([4, 2, 7, 1, 3]), position_min([10, 5, 5, 8]), position_min([42]))

# EXERCICE 5
def sort(L):
    for i in range(len(L) - 1):
        index = i
        for j in range(i+1, len(L)):
            if L[j] < L[index]: index = j
            if L[i] > L[index]:
                temp = L[i]
                L[i] = L[index]
                L[index] = temp
    return L
print(sort([5, 2, 9, 1]), sort([3, 3, 2]))


# EXERCICE 6
def doublons(L):
    if len(L) == 0: return False
    for i in L:
        for j in L:
            if L[i] == L[j]: return False
        return True
print(doublons([1, 2, 3, 4, 5]), doublons([]))

# EXERCICE 7
def frequency(L, x):
    frequence = 0
    for i in L: 
        if i == x: frequence += 1
    return frequence
print(frequency([5, 5, 5], 5))

# EXERICCE 8
def incluse(L1, L2):
    counter = 0
    for val1 in L1:
        for val2 in L2:
            if val1 == val2: counter += 1
    if counter == len(L1): return True
    else: return False
print(incluse([], [1, 2, 3]))


# EXERCICE 9
def equals(L1, L2):
    if len(L1) != len(L2): return False
    else: return incluse(L1, L2)
print(equals([1, 2, 3], [3, 2, 1]))


# EXERCICE 10
def croissante(L):
    counter = 0
    for i in L:
        for j in L:
            if i <= j: counter += 1
    if counter == len(L): return True
    else: return False
print(croissante([1, 2, 4, 3]))