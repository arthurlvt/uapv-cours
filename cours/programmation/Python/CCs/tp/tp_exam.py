def moyenne(L, x, y):
    somme = 0
    compteur = 0
    for i in range(len(L)):
        if L[i] >= x and L[i] <= y:
            somme += L[i]
            compteur += 1
    if compteur == 0:
        return None
    else:
        return somme / compteur

#---------------------------------------#

def min_max(L):
    if len(L) == 0:
        return None, None
    else:
        minimum = L[0]
        maximum = L[0]
        for i in range(1, len(L)):
            if L[i] < minimum:
                minimum = L[i]
            if L[i] > maximum:
                maximum = L[i]
        return minimum, maximum

#---------------------------------------#

def sans_doublons(L):
    new_list = []
    for i in range(len(L)):
        deja_vu = False
        for j in range(len(new_list)):
            if L[i] == new_list[j]:
                deja_vu = True
        if deja_vu == False:
            new_list.append(L[i])
    return new_list

#---------------------------------------#

def present(L, x):
    for i in range(len(L)):
        if x == L[i]: return True
        else: return False
def repetitions(L):
    resultat = []
    for i in range(len(L)):
        if i == 0 or L[i] != L[i - 1]:
            effectif = 0
            for j in range(i, len(L)):
                if L[j] == L[i]:
                    effectif += 1
                else:
                    break
            resultat.append([L[i], effectif])
    return resultat
        
#---------------------------------------#        
        
def test_moyenne(L, x, y, attendu):
    obtenu = moyenne(L, x, y)
    if obtenu == attendu:
        verdict = "OK"
    else:
        verdict = "ÉCHEC"
    print(L, "->", obtenu, "| attendu :", attendu, "|", verdict)       
def test_min_max(L, attendu_min, attendu_max):
    obtenu_min, obtenu_max = min_max(L)
    if obtenu_min == attendu_min and obtenu_max == attendu_max:
        verdict = "OK"
    else:
        verdict = "ÉCHEC"
    print(L, "->", (obtenu_min, obtenu_max), "| attendu :", (attendu_min, attendu_max), "|", verdict)  
def test_sans_doublons(L, attendu):
    obtenu = sans_doublons(L)
    if obtenu == attendu:
        verdict = "OK"
    else:
        verdict = "ÉCHEC"
    print(L, "->", obtenu, "| attendu :", attendu, "|", verdict)  
def test_repetitions(L, attendu):
    obtenu = repetitions(L)
    if obtenu == attendu:
        verdict = "OK"
    else:
        verdict = "ÉCHEC"
    print(L, "->", obtenu, "| attendu :", attendu, "|", verdict)
    