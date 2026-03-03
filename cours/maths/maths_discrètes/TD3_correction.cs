[ OUTIL DE COPIE-COLLE DES SYMBOLES LOGIQUES : ∀ ¬ ∧ ∨ ∃ => <=> ]


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

