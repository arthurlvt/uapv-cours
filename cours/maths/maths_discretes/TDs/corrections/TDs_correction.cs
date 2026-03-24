[ OUTIL DE COPIE-COLLE DES SYMBOLES LOGIQUES : ∀ ¬ ∧ ∨ ∃ => <=> ]
[ OUTIL DE COPIE-COLLE DES SYMBOLES LOGIQUES : ∅, ℕ, ℤ, ℚ, ℝ, ℂ, ∈, ∉, ⊆, ⊈, ⊇, ⊉, ∪, ∩, \, |->, infini ]

TD3: Logique de premier Ordre - Correction
EXO 1: De la logique de premier ordre au français
1. ∀x(P(x) ∧ C(x))  : "Tous le monde a visité Paris et ont un chat ;
2. ∃x(C(x) ∧ ¬F(x)) : "Il existe quelqu'un qui a un chat et qui n'a pas de furet" ;
3. ∀x(E(x) ∧ P(x) => C(x)) : "Tout le monde qui a visité Paris et qui est étudiant a un chat" ;
4. ∀x(P(x) => F(x)) : "Tout le monde qui a visité Paris a un furet" ;
5. ¬∃x(E(x) ∧ C(x) ∧ F(x)) : "Il n'existe personne qui à la fois, est étudiant, a un chat et a un furet" ; 


EXO 2: Du français à la logique de premier ordre -> Soit D(x, y) : "La personne x peut duper la personne y" 
1. "Tout le monde peut duper Alban" : ∀x D(x, Alban) ; 
2. "Brigitte peut duper tout le monde": ∀y D(Brigitte, y) ;
3. "Tout le monde peut duper quelqu'un": ∀x, ∃y D(x, y) ;
4. "Il n'y a personne qui puisse duper tout le monde": ¬∃x, ∀y D(x, y) ; 
5. "Tout le monde peut être dupé par quelqu'un": ∀y, ∃x D(x, y) ; ¬∃y, ∀x D(x, y) ;
6. "Personne ne peut duper à la fois Alban et Brigitte": ¬∃x D(x, Alban) ∧ D(x, Brigitte) ; 
7. "Personne ne peut se duper lui même": ¬∃x D(x, x) ;
8. "Il y a des gens qui peuvent duper aucune personne appart eux même": ∃x, y ¬D(x, y) ∧ D(x, x) ou on peut écrire : ∃x, ∀y (D(x, y) <=> (x = y));


EXO 2 (version négation) 
1. "Personne ne peut duper Alban": ¬∃x D(x, Alban) ; 
2. "Il existe au moins une personne que Brigitte ne peut pas duper": ∃x ¬D(Brigitte, x) ; 
3. "Il existe au moins une personne qui ne peut duper personne": ∃x, ∀y ¬D(x, y) ; 
4. "Tout le monde peut duper tout le monde": ∃x, ∀y D(x, y) ;
5. "Il existe au moins une personne qui peut être dupé par tout le monde": ∃y, ∀x D(x, y) ; 
6. "Il y a des gens qui peuvent duper à la fois Alban et Brigitte": ∃x D(x, Alban) ∧ D(x, Brigitte) ; 
7. "Il y a des gens qui peuvent se duper eux même": ∃x D(x, x) ; 
8. "Tout le monde peut duper au moins une personne autre que lui même": ∀x, ∃y (D(x, y) ∧ ¬(x = y)) ;


EXO 3: Identifier les inférences
1. "Tous les hommes sont mortels. Or Socrate est un homme. Donc Socrate est mortel"
Prédicats: H(x) : "x est un homme" ; M(x) : "x est mortel"
- Prémisse 1: ∀x (H(x) => M(x)) (Hypothèse 1)
- Prémisse 2: H(Socrate) (Hypothèse 2)
- Conclusion: M(Socrate) et Type inférence: Modus Ponens Universel


EXO 4: Modéliser et déduire
1. "Tous les colibris ont des couleurs vives. Aucun gros oiseau ne se nourrit de miel et ont des couleurs ternes."
-> En déduire "Les colibris sont petits"
Domaine : les oiseaux
Prédicats: C(x) : "x est un colibri" ; V(x) : "x a des couleurs vives" ; G(x) : "x est un gros oiseau" ; M(x) : "x se nourrit de miel" ;
- Prémisse 1: ∀x (C(x) => V(x)) (Hypothèse 1) ;
- Prémisse 2: ¬∃x (G(x) ∧ M(x)) ;
              <=> ∀x ¬(G(x) ∧ M(x)) ;
              <=> ∀x (¬G(x) ∨ ¬M(x)) ;
              <=> ∀x (G(x) => ¬M(x)) (Hypothèse 2) ;
- Prémisse 3: ∀x (¬M(x) => ¬V(x)) (Hypothèse 3) ;
- Conclusion: ∀x (C(x) => ¬G(x))
Application des règles inference:
1. ∀x (G(x) => ¬M(x)) (Hypothèse 2) ;
2. ∀x (¬M(x) => ¬V(x)) (Hypothèse 3) ;
3. ∀x (G(x) => ¬V(x)) (Règle de syllogisme hypothétique / Transitivité universelle 1, 2) ;
4. ∀x (C(x) => V(x)) (Hypothèse 3) ;
5. ∀x (¬V(x) => ¬C(x)) (Contraposée de 4) ;
6. ∀x (G(x) => ¬C(x)) (Règle de syllogisme hypothétique / Transitivité universelle 3, 5) ;
7. ∀x (C(x) => ¬G(x)) (Contraposée de 6) ;

2. "Tous les gens qui font du sport mangent sainement et boivent beaucoup d’eau. Tous les étudiants de l’université font du sport et dorment bien la nuit et boivent beaucoup d’eau."
-> En déduire "Tous les étudiants de l’université dorment bien la nuit et boivent beaucoup d’eau."
Domaine : les gens
Prédicats: S(x) : "x fait du sport" ; M(x) : "x mange sainement" ; B(x) : "x boit beaucoup d’eau" ; E(x) : "x est étudiant de l’université" ; D(x) : "x dort bien la nuit" ;
- Prémisse 1: ∀x (S(x) => (M(x) ∧ B(x))) (Hypothèse 1) ;
- Prémisse 2: ∀x (E(x) => (S(x) ∧ D(x) ∧ B(x))) (Hypothèse 2) ;
- Conclusion: ∀x (E(x) => (D(x) ∧ B(x)))
Application des règles inference:
1. ∀x (S(x) => (M(x) ∧ B(x))) (Hypothèse 1) ;
2. ∀x (E(x) => (S(x) ∧ D(x) ∧ B(x))) (Hypothèse 2) ;
3. ∀x (E(x) => S(x)) (Règle de simplification 2) ;
4. ∀x (E(x) => D(x)) (Règle de simplification 2) ;
5. ∀x (E(x) => B(x)) (Règle de simplification 2) ;
6. ∀x (E(x) => (M(x) ∧ B(x))) (Règle de syllogisme hypothétique / Transitivité universelle 3, 1) ;
7. ∀x (E(x) => (D(x) ∧ B(x))) (Règle de conjonction 4, 5) ;

2. bis (version autre) : "Tous les gens (étudiants) qui font du sport mangent sainement et boivent beaucoup d’eau. Tous les étudiants de l’université font du sport et dorment bien la nuit"
-> En déduire "Tous les étudiants de l’université dorment bien la nuit et boivent beaucoup d’eau."
Domaine : les gens
Prédicats: S(x) : "x fait du sport" ; M(x) : "x mange sainement" ; B(x) : "x boit beaucoup d’eau" ; D(x) : "x dort bien la nuit"
- Prémisse 1: ∀x (S(x) => (M(x) ∧ B(x))) (Hypothèse 1) ;
- Prémisse 2: ∀x (S(x) ∧ D(x)) (Hypothèse 2) ;
- Conclusion: ∀x (S(x) => (D(x) ∧ B(x)))
Application des règles inference:
1. ∀x (S(x) ∧ D(x)) (Hypothèse 2) ;
2. S(a) ∧ D(a) (avec a arbitraire dans le domaine -> Règle instanciation universelle 1) ;
3. S(a) (Règle de simplification 2) ;
4. ∀x (S(x) => (M(x) ∧ B(x))) (Hypothèse 1) ;
5. S(a) => (M(a) ∧ B(a)) (Règle d’instanciation universelle 5) ;
6. M(a) ∧ B(a) (Règle de modus ponens universel 3, 6) ;
7. B(a) (Règle de simplification 7) ;
8. D(a) (Règle de simplification 2) ;
9. D(a) ∧ B(a) (Règle de conjonction 4, 9) ;
10. ∀x (S(x) => (D(x) ∧ B(x))) (Règle de généralisation universelle 2, 9) ;

...(faire 3 et 4 dans la correction)

EXO 5: Analyser des raisonnements
1. "Tous les étudiants de première année suivent un cours de programmation. Alice est étudiante de première année."
Peut-on en déduire qu’Alice suit des cours de programmation ?
Domaine : les gens
Prédicats: E(x) : "x est étudiant de première année" ; P(x) : "x suit un cours de programmation"
- Prémisse 1: ∀x (E(x) => P(x)) (Hypothèse 1) ;
- Prémisse 2: E(Alice) (Hypothèse 2) ;
- Conclusion: P(Alice) ?
Application des règles inference:
1. ∀x (E(x) => P(x)) (Hypothèse 1) ;
2. E(Alice) => P(Alice) (Règle d’instanciation universelle 1) ;
3. E(Alice) (Hypothèse 2) ;
4. P(Alice) (Règle de modus ponens universel 2, 3) ;
5. Conclusion: Oui, on peut en déduire qu’Alice suit des cours de programmation, car tous les étudiants de première année suivent un cours de programmation et Alice est étudiante de première année ;

2. "Tous les étudiants d’informatique suivent un cours de programmation. Bob suit des cours de programmation."
Peut-on en déduire que Bob est étudiant d’informatique ?
Domaine : les gens
Prédicats: I(x) : "x est étudiant d’informatique" ; P(x) : "x suit un cours de programmation"
- Prémisse 1: ∀x (I(x) => P(x)) (Hypothèse 1) ;
- Prémisse 2: P(Bob) (Hypothèse 2) ;
- Conclusion: I(Bob) ?
Application des règles inference:
1. ∀x (I(x) => P(x)) (Hypothèse 1) ;
2. I(Bob) => P(Bob) (Règle d’instanciation universelle 1) ;
3. P(Bob) (Hypothèse 2) ;
4. I(Bob) (Règle de modus ponens universel 2, 3) -> Faux ;
5. Conclusion: Non, on ne peut pas en déduire que Bob est étudiant d’informatique, car il peut suivre des cours de programmation sans être étudiant d’informatique ;

3. "Tous les perroquets aiment les fruits. Tui n’est pas un perroquet."
Peut-on en déduire que Tu n’aime pas les fruits ?
Domaine : les animaux
Prédicats: P(x) : "x est un perroquet" ; F(x) : "x aime les fruits"
- Prémisse 1: ∀x (P(x) => F(x)) (Hypothèse 1) ;
- Prémisse 2: ¬P(Tu) (Hypothèse 2) ;
- Conclusion: ¬F(Tu) ?
Application des règles inference:
1. ∀x (P(x) => F(x)) (Hypothèse 1) ;
2. P(Tu) => F(Tu) (Règle d’instanciation universelle 1) ;
3. ¬P(Tu) (Hypothèse 2) ;
4. ¬F(Tu) (Règle de modus tollens universel 2, 3) -> Faux ;
5. Conclusion: Non, on ne peut pas en déduire que Tu n’aime pas les fruits, car Tu peut aimer les fruits sans être un perroquet ;

...(faire 4 et 5 dans la correction)

EXO 6: Montrer que les règles d’inférence sont valides
1. Règle de modus ponens universel : ∀x (P(x) => Q(x)) , P(a) => Q(a) (avec a arbitraire dans le domaine) ;
2. Règle de modus tollens universel : ∀x (P(x) => Q(x)) , ¬Q(a) => ¬P(a) (avec a arbitraire dans le domaine) ;
3. Règle de syllogisme hypothétique / Transitivité universelle : ∀x (P(x) => Q(x)) , ∀x (Q(x) => R(x)) , ∀x (P(x) => R(x)) ;

EXO 7: Algorithme et Quantificateurs
A: domaine de x ;
B: domaine de y ;
-> ∀(x, y), P(x, y)

----------------------------------------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------------------------------------

TD4: Procédures et Preuves de correction - Correction
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

----------------------------------------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------------------------------------

TD5: Manipulation d'ensembles - Correction

EXO 3: Manipulation de base des ensembles
A = D = O = F = L 
|-> {-3, 3} ⊆ J 
|-> {-3, 3} = 2
B = G = N 
|-> ∅ ⊆ de tous les ensembles, par définition
|-> ∅ = 0
C = {{∅}} = 1
E = H 
|-> ℕ
|-> ℕ = infini
I = M 
|-> {0} ⊆ ℕ = E = H
|-> {0} = 1
J = {-3, 3, {3}, {-3}}
|-> |J| = 4
K = {3} ⊆ J, E, H, A, D, O, F, L
|-> |K| = 1

EXO 4: Opérations dans les ensembles
1. A = "Ensemble des étudiants habitants à moins de 3km du CERI"
   B = "Ensemble des étudiants qui viennent au CERI à pied"
   -> A et B sont ensemble des étudiants du CERI
A ∪ B = "Ensemble des étudiants qui habitent à moins de 3km du CERI ou qui viennent au CERI à pied"
A ∩ B = "Ensemble des étudiants qui habitent à moins de 3km du CERI et qui viennent au CERI à pied"
A \ B = "Ensemble des étudiants qui habitent à moins de 3km du CERI mais qui ne viennent pas au CERI à pied"
B \ A = "Ensemble des étudiants qui viennent au CERI à pied mais qui n'habitent pas à moins de 3km du CERI"
A^c = "Ensemble des étudiants qui n'habitent pas à moins de 3km du CERI"
B^c = "Ensemble des étudiants qui ne viennent pas au CERI à pied"

2. A = {1, 2, 3, 4, 5}
   B = {0, 3, 6}
   -> A et B sont dans {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
A ∪ B = {0, 1, 2, 3, 4, 5, 6}
A ∩ B = {3}
A \ B = {1, 2, 4, 5}
B \ A = {0, 6}
A^c = {0, 6, 7, 8, 9, 10}
B^c = {1, 2, 4, 5, 7, 8, 9, 10}

3. A = {a, b, c, d, e}
   B = {c, d, e, f, g, h}
   -> A et B sont dans {a, b, c, d, e, f, g, h}
A ∪ B = {a, b, c, d, e, f, g, h}
A ∩ B = {c, d, e}
A \ B = {a, b}
B \ A = {f, g, h}
A^c = {f, g, h}
B^c = {a, b}

4. A = {x ∈ ℕ | x = 2 * k, k ∈ ℕ} (Ensemble des nombres pairs)
   B = {x ∈ ℕ | x ≤ 100} (Ensemble des nombres naturels inférieurs ou égaux à 100)
   -> A et B sont dans ℕ
A ∪ B = {x ∈ ℕ | x ≤ 100 ∨ x = 2 * k, k ∈ ℕ} (Tous les nombres naturels jusqu'à 100 et tous les nombres pairs)
A ∩ B = {x ∈ ℕ | x ≤ 100 ∧ x = 2 * k, k ∈ ℕ} (Tous les nombres naturels jusqu'à 100 qui sont pairs)
A \ B = {x ∈ ℕ | x > 100 ∧ x = 2 * k, k ∈ ℕ} (Tous les nombres pairs supérieurs à 100)
B \ A =  {x ∈ ℕ | x ≤ 100 ∧ x = 2k + 1, k ∈ ℕ} (Tous les nombres naturels jusqu'à 100 qui sont impairs)
A^c = {x ∈ ℕ | x = 2k + 1, k ∈ ℕ} (Tous les nombres naturels supérieurs à 100 qui sont impairs)
B^c = {x ∈ ℕ | x > 100} (Tous les nombres naturels supérieurs à 100)

5. A = "Ensemble des étudiants de licence informatique"
   B = "Ensemble des étudiants qui suivent des cours d'Algèbre ou des cours d'Analyse"
   -> A et B sont dans ensemble des étudiants de Avignon Université
A ∪ B = "Ensemble des étudiants de licence informatique ou qui suivent des cours d'Algèbre ou des cours d'Analyse"
A ∩ B = "Ensemble des étudiants de licence informatique qui suivent des cours d'Algèbre ou des cours d'Analyse"
A \ B = "Ensemble des étudiants de licence informatique qui ne suivent pas de cours d'Algèbre et ne suivent pas de cours d'Analyse"
B \ A = "Ensemble des étudiants qui suivent des cours d'Algèbre ou des cours d'Analyse mais qui ne sont pas en licence informatique"
A^c = "Ensemble des étudiants de Avignon Université qui ne sont pas en licence informatique"
B^c = "Ensemble des étudiants de Avignon Université qui ne suivent pas de cours d'Algèbre et ne suivent pas de cours d'Analyse"

EXO 5: Application des principes de base des ensembles
1. un groupe contient 325 étudiants Informatique et 18 étudiants de Mathématiques
-> Principe de Multiplication : 325 * 18 = 5850
Il y a 5850 façons différentes de choisir un étudiant en Informatique et un étudiant de Mathématiques.
-> Principe de Addition : 325 + 18 = 343
Il y a 343 façons différentes de choisir un étudiant en Informatique ou un étudiant de Mathématiques.

2. un QCM contient 10 questions. Chaque question a 4 réponses possibles.
-> Principe de Multiplication : 4^10 = 1 048 576
Il y a 1 048 576 façons différentes de répondre à ce QCM.
-> Principe de Multiplication : 5^10 = 9 765 625
Il y a 9 765 625 façons différentes de répondre à ce QCM si on peut choisir de ne pas répondre à une question.

3. 
Un groupe de étudiants contient des étudiants de licence informatique, des étudiants licence mathématiques 
et des étudiants en double-licence informatique et mathématique. On sait que il y a 38 étudiants qui font 
une licence informatique (licence seule ou double-licence), 23 étudiants qui font une licence de 
mathématiques (licence seule ou double-licence) et 7 étudiants qui font une double-licence. 
-> Combien de étudiants y a-t-il dans le groupe ?

-> On peut utiliser la formule de l'union de deux ensembles : |A ∪ B| = |A| + |B| - |A ∩ B|
Ici, A est l'ensemble des étudiants en licence informatique (38), B est l'ensemble des étudiants en licence de mathématiques (23) et A ∩ B est l'ensemble des étudiants en double-licence (7).
Donc, le nombre total d'étudiants dans le groupe est : |A ∪ B| = 38 + 23 - 7 = 54
Il y a 54 étudiants dans le groupe.

EXO 6: Photos de mariage
Alix et Camille se marient et veulent faire des photos avec leur 4 plus proches invités. La photographe
propose de aligner ces personnes sur les photos. Combien y  -t-il de façons différentes de arranger les 6
personnes selon les règles suivantes :
1. Aucune contrainte
2. Alix et Camille doivent être côte à côte
3. Alix et Camille ne doivent pas être côte à côte
4. Alix doit se situer quelque part à gauche de Camille (mais pas nécessairement à côté)
5. Alix doit se situer quelque part à droite de Camille (mais pas nécessairement à côté)

-> Il y a 6 personnes à arranger, donc il y a 6! façons différentes de les arranger.
6! = 720 |-> il y a 720 façons différentes de arranger les 6 personnes sans aucune contrainte.


EXO 7: Boutique de vêtements
Une boutique de vêtements lance une nouvelle collection de tee-shirts. Un tee-shirt est défini par sa coupe,
sa taille, sa couleur et son motif. On donne les options suivantes pour chaque caractéristique :
- Ensemble des coupes possibles: coupe homme, coupe femme, coupe neutre (3 options)
- Ensemble des tailles possibles: XS, S, M, L, XL, XXL (6 options)
- Ensemble des couleurs possibles: noir, bleu, rouge, vert, jaune, violet, marron (7 options)
- Ensemble des motifs possibles: unis, pois, rayures, dessins (4 options)

1. Définissez le ensemble des tee-shirts. Quelle est la cardinalité de cet ensemble ?
Ensemble des tee-shirts peut être défini comme le produit cartésien des ensembles de caractéristiques :
Tee-shirts = Coupes × Tailles × Couleurs × Motifs
Où :
- Coupes = {coupe homme, coupe femme, coupe neutre}
- Tailles = {XS, S, M, L, XL, XXL}
- Couleurs = {noir, bleu, rouge, vert, jaune, violet, marron}
- Motifs = {unis, pois, rayures, dessins}
La cardinalité de de ensemble des tee-shirts est le produit des cardinalités de chaque ensemble de caractéristiques :
|Tee-shirts| = |Coupes| × |Tailles| × |Couleurs| × |Motifs|
|Tee-shirts| = 3 × 6 × 7 × 4 = 504
Il y a 504 tee-shirts différents dans la nouvelle collection.

Supposons à présent que toutes les combinaisons ne sont pas possibles. Les tailles XL et XXL ne sont 
disponibles uniquement avec la coupe homme. Les tailles XS et S ne sont disponibles uniquementavec la 
coupe femme. Les couleurs noir, bleu et rouge ne sont disponibles que pour les tailles M et L. 
Les couleurs vert et jaunes ne sont disponibles que pour les tailles XL et XXL. Les couleurs violet et 
marron ne sont disponibles que pour les tailles XS et S. Le motif à dessin est disponible uniquement pour 
les tailles XS, S et M. Le motif uni est disponible uniquement pour les tailles L et XXL. Le motif à pois 
est disponible uniquement pour les tailles L et XL. Le motif à rayures est disponible uniquement pour les 
tailles XS et S.
2. Définissez le nouvel ensemble des tee-shirts en tenant compte de ces contraintes. Quelle est la cardinalité de ce nouvel ensemble ?
Ensemble des tee-shirts avec contraintes peut être défini comme suit :
Tee-shirts = {(c, t, co, m) | c ∈ Coupes, t ∈ Tailles, co ∈ Couleurs, m ∈ Motifs,
et les contraintes suivantes sont respectées :
- (t = XL ∨ t = XXL) => c = coupe homme
- (t = XS ∨ t = S) => c = coupe femme
- (t = M ∨ t = L) => (co = noir ∨ co = bleu ∨ co = rouge)
- (t = XL ∨ t = XXL) => (co = vert ∨ co = jaune)
- (t = XS ∨ t = S) => (co = violet ∨ co = marron)
- (t = XS ∨ t = S ∨ t = M) => m = dessin
- (t = L ∨ t = XXL) => m = uni
- (t = L ∨ t = XL) => m = pois
- (t = XS ∨ t = S) => m = rayures}
Calculons la cardinalité de ce nouvel ensemble en tenant compte des contraintes :
- Pour la coupe homme (c = coupe homme), les tailles possibles sont M, L, XL, XXL. 
  - Pour M et L, les couleurs possibles sont noir, bleu, rouge, et les motifs possibles sont dessin, uni, pois. 
    - M : 3 couleurs × 3 motifs = 9 tee-shirts
    - L : 3 couleurs × 3 motifs = 9 tee-shirts
  - Pour XL et XXL, les couleurs possibles sont vert, jaune, et les motifs possibles sont uni, pois. 
    - XL : 2 couleurs × 2 motifs = 4 tee-shirts
    - XXL : 2 couleurs × 2 motifs = 4 tee-shirts
- Pour la coupe femme (c = coupe femme), les tailles possibles sont XS, S. 
  - Pour XS et S, les couleurs possibles sont violet, marron, et les motifs possibles sont dessin, rayures. 
    - XS : 2 couleurs × 2 motifs = 4 tee-shirts
    - S : 2 couleurs × 2 motifs = 4 tee-shirts
- Pour la coupe neutre (c = coupe neutre), les tailles possibles sont M, L. 
  - Pour M et L, les couleurs possibles sont noir, bleu, rouge, et les motifs possibles sont dessin, uni, pois. 
    - M : 3 couleurs × 3 motifs = 9 tee-shirts
    - L : 3 couleurs × 3 motifs = 9 tee-shirts
En total, le nombre de tee-shirts différents dans la nouvelle collection avec les contraintes est :
9 (coupe homme M) + 9 (coupe homme L) + 4 (coupe homme XL) + 4 (coupe homme XXL) + 4 (coupe femme XS) + 4 (coupe femme S) + 9 (coupe neutre M) + 9 (coupe neutre L) = 52
Il y a 52 tee-shirts différents dans la nouvelle collection en tenant compte des contraintes.

----------------------------------------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------------------------------------

TD7: Permutations et Combinaisons - Correction

EXO 1: Quelques calculs
1. Combien de façons existe-il de sélectionner 5 élements dans ordre dans un ensemble de 3 élements
si les répétitions des éléments sont autorisées ?
-> Ensemble de n = 3 éléments, 5 élements à sélectionner (ordonnés) : n^k = 3^5 = 243
2. Combien de façons existe-il de sélectionner 5 élements dans ordre dans un ensemble de 5 élements
si les répétitions des éléments sont autorisées ?
-> Ensemble de n = 5 éléments, 5 élements à sélectionner (ordonnés) : n^k = 5^5 = 3125
3. Combien de chaines de caractères peut-on former si ;
 a) seule les lettres en minuscules sont autorisées ?
 b) les lettres en minuscules et les lettres en majuscules sont autorisés ?
 c) les lettres en minuscules les lettres en majuscules et les chiffres sont autorisés ?
-> a) 26 lettres en minuscules longueur de la chaine k : 26^k
-> b) 26 lettres en minuscules + 26 lettres en majuscules = 52 caractères, longueur de la chaine k : 52^k
-> c) 26 lettres en minuscules + 26 lettres en majuscules + 10 chiffres = 62 caractères, longueur de la chaine k : 62^k
4. Combien de façons existe-il de distribuer 3 tâches à réaliser à 5 employés, si chaque employé peut effectuer 0, 1, 2 ou 3 tâches ?
-> Ensemble de n = 5 employés, 3 tâches à distribuer (ordonnées) : n^k = 5^3 = 125
5. Chaque jours, je prends un sandwich au hasard dans une pile contenant de nombreux exemplaires de 6 sandwichs différents.
Si le ordre de sélection des sandwichs compte combien de façons existe-il de choisir les sandwichs pendant une semaine (7 jours) ?;
-> Ensemble de n = 6 sandwichs, 7 jours à sélectionner (ordonnés) : n^k = 6^7 = 279 936

EXO 2: A la boulangerie :
[RAPPEL: (n, k) = n! / (k! * (n - k)!)]
1. Le nombre de assortissements de 6 petits pains est de 8^6 = 262 144
/-> (k + n - 1)! / (k! * (n - 1)!) = 13! / (6! * 7!) = 1716
2. Le nombre de assortissements de 12 petits pains est de 8^12 = 68 719 476 736
/-> (19, 12) = 19! / (12! * 7!) = 50388
3. Le nombre de assortissements de 24 petits pains est de 8^24 = 18 446 744 073 709 551 616
/-> (31, 24) = 31! / (24! * 7!) = 2629575
4. Le nombre de assortissements de 12 petits pains contenant au moins un de chaque variétés est de 8! * 8^4 = 1 290 240
/-> Si on veut au moins un pain de chaque variété ;
C, N, M, B, R, S, G, F x x x x <=> On calcul le nombre de 4-combinaisons parmi 11 avec répétitions ;
(11, 4) = 11! / (4! * 7!) = 330
Ensuite, on multiplie par 8! pour les différentes façons de choisir les 8 pains différents ;
330 * 8! = 1 290 240


EXO 3: A la pizzeria :
-> Un traiteur propose de réaliser des livraisons de pizzas pour des fêtes. Ils ont à la carte les pizzas suivantes :
- Margherita
- Jambon Fromage
- 3 Fromages
- Poulet Crème
- Saumon Pommes de terre
- Aubergines
1. Combien existe-il de commandes possibles de 12 pizzas ?
-> Ensemble de n = 6 pizzas, 12 pizzas à sélectionner (ordonnées) : n^k = 6^12 = 2 176 782 336
2. Combien existe-il de commandes possibles de 36 pizzas ?
-> Ensemble de n = 6 pizzas, 36 pizzas à sélectionner (ordonnées) : n^k = 6^36 = 2 176 782 336^3 = 1 031 442 606 796 976 000 000
3. Combien existe-il de commandes possibles de 24 pizzas avec au moins 2 de chaque variété ?
-> Si on veut au moins 2 pizzas de chaque variété ;
M, J, F, P, S, A x x x x x x <=> On calcul le nombre de 12-combinaisons parmi 17 avec répétitions ;
(17, 12) = 17! / (12! * 5!) = 6188
Ensuite, on multiplie par 6! pour les différentes façons de choisir les 6 pizzas différentes ;
6188 * 6! = 4 461 120
4. Combien existe-il de commandes possibles de 24 pizzas ne contenant pas plus de 2 margherita ?
-> Si on veut au plus 2 pizzas de Margherita ;
M x x <=> On calcul le nombre de 22-combinaisons parmi 6 avec répétitions ;
(27, 22) = 27! / (22! * 5!) = 80730
Ensuite, on multiplie par 6! pour les différentes façons de choisir les 6 pizzas différentes ;
80730 * 6! = 5 647 200


----------------------------------------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------------------------------------


TD8: Principe inclusion-exclusion et dérangements - Correction
EXO 1: Appliquer les bases du principe de inclusion-exclusion
-> Soit 2 ensembles E1 et E2 tels que |E1| = 12 et |E2| = 18.
1. Quelle est la cardinalité de E1 ∪ E2 si E1 ∩ E2 = ∅ ?
Si E1 et E2 sont disjoints, alors |E1 ∪ E2| = |E1| + |E2| = 12 + 18 = 30
2. Quelle est la cardinalité de E1 ∪ E2 si |E1 ∩ E2| = 1 ?
Si E1 et E2 sont disjoints, alors |E1 ∪ E2| = |E1| + |E2| - |E1 ∩ E2| = 12 + 18 - 1 = 29
3. Quelle est la cardinalité de E1 ∪ E2 si |E1 ∩ E2| = 5 ?
Si E1 et E2 ont une intersection de cardinalité 5, alors |E1 ∪ E2| = |E1| + |E2| - |E1 ∩ E2| = 12 + 18 - 5 = 25
4. Quelle est la cardinalité de E1 ∪ E2 si |E1 ∩ E2| = 10 ?
Si E1 et E2 ont une intersection de cardinalité 10, alors |E1 ∪ E2| = |E1| + |E2| - |E1 ∩ E2| = 12 + 18 - 10 = 20
5. Quelle est la cardinalité de E1 ∪ E2 si E1 ⊆ E2 ?
Si E1 est un sous-ensemble de E2, alors |E1 ∪ E2| = |E2| = 18

EXO 2: Comprendre la formule du principe général de inclusion-exclusion
1. Soit 3 ensembles A, B, C, contenant chacun 100 éléments.
(a). Développer la formule donnant la cardinalité de A ∪ B ∪ C.
|A ∪ B ∪ C| = |A| + |B| + |C| - |A ∩ B| - |A ∩ C| - |B ∩ C| + |A ∩ B ∩ C|
(b). Quelle est la cardinalité de A ∪ B ∪ C si les 3 ensembles sont disjoints ?
Si A, B et C sont disjoints, alors |A ∪ B ∪ C| = |A| + |B| + |C| = 100 + 100 + 100 = 300
(c). Quelle est la cardinalité de A ∪ B ∪ C si chaque paire de ensembles contient 50 élements mais que aucun élement est présent dans les 3 ensembles ?
Si chaque paire de ensembles contient 50 éléments, alors |A ∩ B| = |A ∩ C| = |B ∩ C| = 50 et |A ∩ B ∩ C| = 0
Donc, |A ∪ B ∪ C| = |A| + |B| + |C| - |A ∩ B| - |A ∩ C| - |B ∩ C| + |A ∩ B ∩ C| = 100 + 100 + 100 - 50 - 50 - 50 + 0 = 150
(d). Quelle est la cardinalité de A ∪ B ∪ C si chaque paire de ensembles contient 50 élements mais que 25 élement sont présent dans les 3 ensembles ?
Si chaque paire de ensembles contient 50 éléments, alors |A ∩ B| = |A ∩ C| = |B ∩ C| = 50 et |A ∩ B ∩ C| = 25
Donc, |A ∪ B ∪ C| = |A| + |B| + |C| - |A ∩ B| - |A ∩ C| - |B ∩ C| + |A ∩ B ∩ C| = 100 + 100 + 100 - 50 - 50 - 50 + 25 = 175
(e). Quelle est la cardinalité de A ∪ B ∪ C si ces 3 ensembles sont égaux ?
Si A, B et C sont égaux, alors |A ∩ B| = |A ∩ C| = |B ∩ C| = |A ∩ B ∩ C| = 100
Donc, |A ∪ B ∪ C| = |A| + |B| + |C| - |A ∩ B| - |A ∩ C| - |B ∩ C| + |A ∩ B ∩ C| = 100 + 100 + 100 - 100 - 100 - 100 + 100 = 100

2. Soit 4 ensembles A, B, C, D avec |A| = 10, |B| = 100, |C| = 1000, |D| = 10 000
(a). Développer la formule donnant la cardinalité de A ∪ B ∪ C ∪ D.
|A ∪ B ∪ C ∪ D| = |A| + |B| + |C| + |D| - |A ∩ B| - |A ∩ C| - |A ∩ D| - |B ∩ C| - |B ∩ D| - |C ∩ D| + |A ∩ B ∩ C| + |A ∩ B ∩ D| + |A ∩ C ∩ D| + |B ∩ C ∩ D| - |A ∩ B ∩ C ∩ D|
(b). Quelle est la cardinalité de A ∪ B ∪ C ∪ D si A ⊆ B, B ⊆ C, C ⊆ D ?
Si A ⊆ B, B ⊆ C, C ⊆ D, alors |A ∪ B ∪ C ∪ D| = |D| = 10 000
(c). Quelle est la cardinalité de A ∪ B ∪ C ∪ D si les 4 ensembles sont disjoints ?
Si A, B, C et D sont disjoints, alors |A ∪ B ∪ C ∪ D| = |A| + |B| + |C| + |D| = 10 + 100 + 1000 + 10 000 = 11 110
(d). Quelle est la cardinalité de A ∪ B ∪ C ∪ D si chaque paire de ensembles contient 2 élements et chaque triplet de ensembles contient 1 élement et que aucun élement est présent dans les 4 ensembles ?
Si chaque paire de ensembles contient 2 éléments, alors |A ∩ B| = |A ∩ C| = |A ∩ D| = |B ∩ C| = |B ∩ D| = |C ∩ D| = 2 (6 manieres donc 12 éléments au total)
Si chaque triplet de ensembles contient 1 élément, alors |A ∩ B ∩ C| = |A ∩ B ∩ D| = |A ∩ C ∩ D| = |B ∩ C ∩ D| = 1 (4 manieres donc 4 éléments au total)
Si aucun élément est présent dans les 4 ensembles, alors |A ∩ B ∩ C ∩ D| = 0
Donc, |A ∪ B ∪ C ∪ D| = |A| + |B| + |C| + |D| - |A ∩ B| - |A ∩ C| - |A ∩ D| - |B ∩ C| - |B ∩ D| - |C ∩ D| + |A ∩ B ∩ C| + |A ∩ B ∩ D| + |A ∩ C ∩ D| + |B ∩ C ∩ D| - |A ∩ B ∩ C ∩ D| = 10 + 100 + 1000 + 10 000 - 12 + 4 - 0 = 11 102
(e). Quellle est la cardinalité de A ∪ B ∪ C ∪ D si chaque paire de ensembles contient 3 élements et chaque triplet de ensembles contient 3 élement et que 3 élement sont présents dans les 4 ensembles ?
Si chaque paire de ensembles contient 3 éléments, alors |A ∩ B| = |A ∩ C| = |A ∩ D| = |B ∩ C| = |B ∩ D| = |C ∩ D| = 3 (6 manieres donc 18 éléments au total)
Si chaque triplet de ensembles contient 3 éléments, alors |A ∩ B ∩ C| = |A ∩ B ∩ D| = |A ∩ C ∩ D| = |B ∩ C ∩ D| = 3 (4 manieres donc 12 éléments au total)
Si 3 éléments sont présents dans les 4 ensembles, alors |A ∩ B ∩ C ∩ D| = 3
Donc, |A ∪ B ∪ C ∪ D| = |A| + |B| + |C| + |D| - |A ∩ B| - |A ∩ C| - |A ∩ D| - |B ∩ C| - |B ∩ D| - |C ∩ D| + |A ∩ B ∩ C| + |A ∩ B ∩ D| + |A ∩ C ∩ D| + |B ∩ C ∩ D| - |A ∩ B ∩ C ∩ D| = 10 + 100 + 1000 + 10 000 - 18 + 12 - 3 = 11 101
-> (A réviser avec la giga formule générale de inclusion-exclusion pour n ensembles) :
  n        n
| U E_i| = ∑(-1)^(k+1)(        ∑             | E_i1 ∩ E_i2 ∩ ... ∩ E_ik |)
 i=1      k=1          1 =< i < ... < i =< n
-> RESUMÉ: On fait la somme de chaque union de 1 ensemble puis on soustrait la somme de chaque union de 2 ensembles puis on ajoute la somme de chaque union de 3 ensembles puis on soustrait la somme de chaque union de 4 ensembles etc ;

EXO 3: Modélisation
1. Soit un panier de 100 pommes. 20 parmis elles sont véreuses 15 sont abîmées et 10 sont véreuses et abîmées. On ne peut vendre que les pommes qui ne sont ni véreuses ni abîmées. Combien de pommes du panier peut-on vendre ?
Soit V : ensemble des pommes véreuses et A: ensemble des pommes abîmées
|V| = 20, |A| = 15, |V ∩ A| = 10
Le nombre de pommes qui ne sont ni véreuses ni abîmées est donné par la @formule du principe de inclusion-exclusion :
|V^c ∩ A^c| = |V^c| + |A^c| - |V^c ∪ A^c|
|V^c| = 100 - |V| = 80
|A^c| = 100 - |A| = 85
|V^c ∪ A^c| = 100 - |V ∩ A| = 90
Donc, |V^c ∩ A^c| = 80 + 85 - 90 = 75
On peut vendre 75 pommes du panier.

2. 
Une association sportive propose une excursion alpinisme et reçoit 1000 candidatures. Parmis ces candidatures, 450 ont le vertige puis 622 sont en mauvaise condition physique et 30 on est sévères allergies.
- On sait que 111 candidats ont à la fois le vertige et une mauvaise condition physique
- On sait que 14 candidats ont la fois le vertige et des allergies sévères
- On sait que 18 candidats sont à la fois en mauvaise condition physique et ont des allergies sévères
- On sait que 9 candidats ont le vertige une mauvaise condition physique et des allergies sévères
Les seules candidatures recevables sont celles de personnes en bonne condition physique qui ont pas le vertige et qui ont pas des allergies sévères. 
Combien de candidatures recevables cette association reçoit-elle ?

Soit V : ensemble des candidats ayant le vertige
     C : ensemble des candidats en mauvaise condition physique
     A : ensemble des candidats ayant des allergies sévères
|V| = 450, |C| = 622, |A| = 30
|V ∩ C| = 111, |V ∩ A| = 14, |C ∩ A| = 18
|V ∩ C ∩ A| = 9
Le nombre de candidatures recevables est donné par la formule du principe de inclusion-exclusion :
|V^c ∩ C^c ∩ A^c| = |V^c| + |C^c| + |A^c| - |V^c ∩ C^c| - |V^c ∩ A^c| - |C^c ∩ A^c| + |V^c ∩ C^c ∩ A^c|
On regarde les différentes parties de la formule:
|V^c| = 1000 - |V| = 550
|C^c| = 1000 - |C| = 378
|A^c| = 1000 - |A| = 970
On regarde ensuite les doublets:
|V^c ∩ C^c| = 1000 - |V ∩ C| = 889
|V^c ∩ A^c| = 1000 - |V ∩ A| = 986
|C^c ∩ A^c| = 1000 - |C ∩ A| = 982
Puis on regarde le triplet:
|V^c ∩ C^c ∩ A^c| = 1000 - |V ∩ C ∩ A| = 991
Donc, |V^c ∩ C^c ∩ A^c| = 550 + 378 + 970 - 889 - 986 - 982 + 991 = 942
Il y a 942 candidatures recevables que cette association reçoit.

3.
A une soirée, chaque invité peut mettre des accessoires. Les accessoires à disposition sont des lunettes des chapeaux des vestes et des cravates.
Les invités peuvent mettre plusieurs accessoires mais pas plusieurs fois le même accessoire. Chacun des accessoires est porté par 10 personnes. Chaque paire
de accessoire est portée par 5 personnes. Chaque ensemble de 3 accessoires est porté par 3 personnes et une seule personne a choisi de porter 4 accessoires.
Si tous les invités portent au moins un accessoire combien de invités y a-t-il à cette soirée ?

Soit L : ensemble des invités portant des lunettes
     C : ensemble des invités portant des chapeaux
     V : ensemble des invités portant des vestes
     R : ensemble des invités portant des cravates
|L| = |C| = |V| = |R| = 10
|L ∩ C| = |L ∩ V| = |L ∩ R| = |C ∩ V| = |C ∩ R| = |V ∩ R| = 5
|L ∩ C ∩ V| = |L ∩ C ∩ R| = |L ∩ V ∩ R| = |C ∩ V ∩ R| = 3
|L ∩ C ∩ V ∩ R| = 1
Le nombre des invités à cette soirée est donné par la formule du principe de inclusion-exclusion :
|L ∪ C ∪ V ∪ R| = |L| + |C| + |V| + |R| - |L ∩ C| - |L ∩ V| - |L ∩ R| - |C ∩ V| - |C ∩ R| - |V ∩ R| + |L ∩ C ∩ V| + |L ∩ C ∩ R| + |L ∩ V ∩ R| + |C ∩ V ∩ R| - |L ∩ C ∩ V ∩ R|
Donc, |L ∪ C ∪ V ∪ R| = 10 + 10 + 10 + 10 - 5 - 5 - 5 - 5 - 5 - 5 + 3 + 3 + 3 + 3 - 1 = 28
Il y a 28 invités à cette soirée.

