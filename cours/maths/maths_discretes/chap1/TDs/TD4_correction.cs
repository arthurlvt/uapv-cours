[ OUTIL DE COPIE-COLLE DES SYMBOLES LOGIQUES : ∀ ¬ ∧ ∨ ∃ => <=> ]


EXO 1: Procédure simple
x <- 2
z <- x + y
x <- y * z

1. soit assertion initiale (p): x = 5 et assertion finale (q) : x = 14 ; On a alors la correction partielle suivante:
- z <- 5 + 2 = 7
- x <- y * z = 2 * 7 = 14
-> conclusion : q est vérifiée
2. soit assertion initiale (p): x = -5 et assertion finale (q) : x = -6 ;
- z <- -5 + 2 = -3
- x <- y * z = 2 * -3 = -6
-> conclusion : q est vérifiée
3. soit assertion initiale (p): x = -2 et assertion finale (q) : x = 0 ;
- z <- -2 + 2 = 0
- x <- y * z = 2 * 0 = 0
-> conclusion : q est vérifiée


EXO 2: Procédure avec blocs conditionnels
1. soit assertion initiale (p): T et assertion finale (q) : x => 0; On a alors la correction partielle suivante:
Si x < 0 alors
x <- 0
Fin Si

(T ∧ (x < 0)){x <- 0}(x >= 0) <=> P{S}q 
- (x < 0){x <- 0}(x >= 0) Vrai <=> 
- (T ∧ ¬(x < 0)) => (x >= 0) Vrai <=>
- T{Si x < 0 alors x <- 0 Fin Si}(x >= 0) est partiellement correcte


2. soit assertion initiale (p): T et assertion finale (q) : (x =< ∧ min = x)∨(x > y ∧ min = y); On a alors la correction partielle suivante:
Si x < y alors
min <- x
Sinon
min <- y
Fin Si


EXO 3: Procédure avec des boucles
1. soit assertion initiale (p): x appartient à R, n appartient à N^* et assertion finale (q) : puissance(x, n) = x^n; 
On a alors la correction partielle suivante:
ib : (puissance = x^i) ∧ (i =< n)
Ainsi, puissance = I, i = 0, x^0 = 1
puissance = puissance * x = x^i * x = x^(i + 1) = x^i2
Donc puissance = x^i reste vraie à lissue de la boucle et comme i < n alors i2 < n + 1 
alors i2 < n donc linvariant de boucle est vérifiée à litération suivante (fin de la boucles)

2. Avant dentrer dans la boucle, puissance = 1 et i = 0, alors puissance = 1 = x^0 = x^i ..i = 1 =< n
à lissue de la procédure i < n est FAUX
(puissance = x^i) ∧ (i =< n) est vrai donc i = n et puissance = x^n

3. Il faut montrer q2, la procédure termine:
Au début c = 0 et il est incrémenté de 1 à chaque itération, alors c = n après n 
itérations, et la condition de la boucle devient fausse, alors la procédure termine.


EXO 4: Procédures Récursives
Soit la procédure somme(n) donnée par Σn k = 0 k
Procedure somme(n : entier positif)
    Si n = 0 alors
        Retourner 0
    Sinon
        Retourner n + somme(n - 1)
    Fin Si

1. Montrer que la procédure est correcte pour le cas de base
Ici, on montre que somme(n) = Σn k = 0 k est vérifiée pour n = 0 :
Si n = 0, somme(n) renvoie 0, et Σ0 k = 0 k = 0
Donc la procédure est correcte pour le cas de base.

Montrer que la procédure est correcte pour le cas récursif
Supposons que la procédure est correcte pour n - 1 cest à dire que somme(n - 1) = Σn-1 k = 0 k
Alors, pour n > 0, somme(n) renvoie n + somme(n - 1) = n + Σn-1 k = 0 k = Σn k = 0 k
Donc la procédure est correcte pour le cas récursif.

2. Montrer que la procédure est correcte pour le cas de base
Ici, on montre que factorielle(n : entier positif) = n! est vérifiée pour n = 0 :
Si n = 0, factorielle(n) renvoie 1, et 0! = 1
Donc la procédure est correcte pour le cas de base.

Montrer que la procédure est correcte pour le cas récursif
Supposons que la procédure est correcte pour n - 1 cest à dire que factorielle(n - 1) = (n - 1)!
Alors, pour n > 0, factorielle(n) renvoie n * factorielle(n - 1) = n * (n - 1)! = n!
Donc la procédure est correcte pour le cas récursif.

-> La procédure est donc correcte ∀ n >= 0.


EXO 5: Analyser des Procédures
Procédure p5.1 (n : entiers strictement positif, m : entier)
    Si n = 1 alors
        Retourner m
    Sinon
        Retourner m + p5.1(n - 1, m)
    Fin Si

1. Quel est le résultat renvoyé par p5.1 si n = 2 et m = 2?
Si n = 2 et m = 2, alors :
- p5.1(2, 2) renvoie 2 + p5.1(1, 2)
- p5.1(1, 2) renvoie 2
Donc, p5.1(2, 2) renvoie 2 + 2 = 4.

2. Quel est le résultat renvoyé par p5.1 si n = 3 et m = 0?
Si n = 3 et m = 0, alors :
- p5.1(3, 0) renvoie 0 + p5.1(2, 0)
- p5.1(2, 0) renvoie 0 + p5.1(1, 0)
- p5.1(1, 0) renvoie 0
Donc, p5.1(3, 0) renvoie 0 + 0 + 0 = 0.

3. quel est le résultat renvoyé par p5.1 si n = 3 et m = 4?
Si n = 3 et m = 4, alors :
- p5.1(3, 4) renvoie 4 + p5.1(2, 4)
- p5.1(2, 4) renvoie 4 + p5.1(1, 4)
- p5.1(1, 4) renvoie 4
Donc, p5.1(3, 4) renvoie 4 + 4 + 4 = 12.

4. Déduire d'après les questions précédentes le rôle de la procédure p5.1
La procédure p5.1 calcule la somme de m répété n fois, ce qui équivaut à n * m. 
En d'autres termes, p5.1(n, m) = n * m.

5. Montrer que p5.1 est correcte
Pour montrer que p5.1 est correcte, nous allons utiliser l'induction sur n.
- Cas de base : n = 1
Si n = 1, alors p5.1(1, m) renvoie m, et 1 * m = m, donc p5.1(1, m) = 1 * m est vérifié.
- Cas récursif : Supposons que p5.1(k, m) = k * m pour un certain k >= 1. 
Nous devons montrer que p5.1(k + 1, m) = (k + 1) * m.
p5.1(k + 1, m) renvoie m + p5.1(k, m). 
Par hypothèse de récurrence, p5.1(k, m) = k * m, donc p5.1(k + 1, m) = m + k * m = (k + 1) * m.
Ainsi, p5.1 est correcte pour tous les n >= 1.

5.2
Procédure p5.2 (x : réel)
    y <- 2
    z <- x + y
    Si z > 0 alors
        x <- z * 3
    Sinon
        x <- 0
    Fin Si
    Retourner z
Fin procédure

1. Quel est le résultat renvoyé par p5.2 si x = 3?
Si x = 3, alors :
- y <- 2
- z <- 3 + 2 = 5
- Comme x > 0, x <- 5 * 3 = 15
- La procédure retourne z, donc p5.2(3) renvoie 5.

2. Quel est le résultat renvoyé par p5.2 si x = -2?
Si x = -2, alors :
- y <- 2
- z <- -2 + 2 = 0
- Comme x <= 0, x <- 0
- La procédure retourne z, donc p5.2(-2) renvoie 0.

3. Quel est le résultat renvoyé par p5.2 si x = -4?
Si x = -4, alors :
- y <- 2
- z <- -4 + 2 = -2
- Comme x <= 0, x <- 0
- La procédure retourne z, donc p5.2(-4) renvoie -2.

4. Déduire d'après les questions précédentes le rôle de la procédure p5.2
La procédure p5.2 renvoie la valeur max(0, 3x + 6)

5. Montrer que p5.2 est correcte
Pour montrer que p5.2 est correcte, nous allons vérifier que les assertions initiales et finales sont respectées.
Rappel: pour une procédure de la forme:
Si c, alors S1
Sinon si S1 c2 alors S2
Sinon S3
Fin Si
On a les hypothèses suivantes:
- (c ∧ p){S1}q
- (¬c ∧ c2 ∧ p){S2}q
- (¬c ∧ ¬c2 ∧ p){S3}q
Conclusion : (p){Si c alors S1 Sinon si S1 c2 alors S2 Sinon S3 Fin Si}q

Dans notre cas, nous avons:
- c : z > 0
- S1 : z <- z * 3
- S2 : z <- 0
- p : T (toujours vrai)
- q : z = x + 2
Vérifions les hypothèses:
- (z > 0 ∧ T){z <- z * 3}(z = x + 2) est vérifié car après exécution de S1, z reste égal à x + 2.
- (¬(z > 0) ∧ T){z <- 0}(z = x + 2) est vérifié car après exécution de S2, z reste égal à x + 2.
Ainsi, toutes les hypothèses sont vérifiées, et nous pouvons conclure que p5.2 est correcte.