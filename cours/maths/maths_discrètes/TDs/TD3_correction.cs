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
1. "Tous les hommes sont mortels. Or Socrate est un homme. Donc Socrate est mortel" : 
Prédicats: H(x) : "x est un homme" ; M(x) : "x est mortel"
- Prémisse 1: ∀x (H(x) => M(x)) (Hypothèse 1)
- Prémisse 2: H(Socrate) (Hypothèse 2)
- Conclusion: M(Socrate) et Type inférence: Modus Ponens Universel




