[ OUTIL DE COPIE-COLLE DES SYMBOLES LOGIQUES : ∀ ¬ ∧ ∨ ∃ => <=> ]

EXERCICE 1 : Dire si les applications suivantes sont linéaires
RAPPEL DU COURS :
Une application f : E -> F entre deux espaces vectoriels E et F est linéaire si elle vérifie les propriétés suivantes pour 
tous les éléments u, v de E et tous les scalaires λ. f : E -> F est une application linéaire si :
∀(x, y) ∈ E, f(x + y) = f(x) + f(y)
∀x ∈ E, ∀λ ∈ K, f(λx) = λf(x)
par conséquent : f(0E) = 0F où 0E et 0F sont les éléments neutres de E et F respectivement.

1. f : R^2 -> R^3, (x, y) |-> (x - y, 2x + 3y, 0)
-> Lapplication est linéaire, car elle vérifie les propriétés de linéarité :
- f((x1, y1) + (x2, y2)) = f(x1 + x2, y1 + y2) = ((x1 + x2) - (y1 + y2), 2(x1 + x2) + 3(y1 + y2), 0);
<=> (x1 - y1, 2x1 + 3y1, 0) + (x2 - y2, 2x2 + 3y2, 0) = f(x1, y1) + f(x2, y2);
- f(λ(x, y)) = f(λx, λy) = (λx - λy, 2λx + 3λy, 0) = λ(x - y, 2x + 3y, 0) = λf(x, y)

2. f : R^2 -> R^3, (x, y) |-> (x - y, 2x + 3y, 1)
-> Lapplication est pas linéaire, car elle ne vérifie pas les propriétés de linéarité :
- f((x1, y1) + (x2, y2)) = f(x1 + x2, y1 + y2) = ((x1 + x2) - (y1 + y2), 2(x1 + x2) + 3(y1 + y2), 1);
<=> (x1 - y1, 2x1 + 3y1, 1) + (x2 - y2, 2x2 + 3y2, 1) = f(x1, y1) + f(x2, y2);
<=> (x1 - y1 + x2 - y2, 2x1 + 3y1 + 2x2 + 3y2, 2) = f(x1, y1) + f(x2, y2);
- f(λ(x, y)) = f(λx, λy) = (λx - λy, 2λx + 3λy, 1) = λ(x - y, 2x + 3y, 1) = λf(x, y)
ou plus simplement: f(0, 0) = (0 - 0, 2*0 + 3*0, 1) = (0, 0, 1) ≠ (0, 0, 0) = 0F donc f est pas linéaire

3. f : R^2 -> R^3, (x, y) |-> (x^2 + y^2, 2x + 3y)
-> Lapplication est pas linéaire, car elle ne vérifie pas les propriétés de linéarité :
on peut utiliser un contre-exemple pour montrer que f est pas linéaire:


EXERCICE 2 :
-> Soit f : R^2 -> R^3, application linéaire définie par:
f((x, y)) = (x + y, x -y, x + y)
Déterminer le noyau et image de f. Est-elle injective? surjective?

x + y = 0    |    x + y = 0 => 2x = 0
x - y = 0
x + y = 0   

ker f = {(0, 0)} => f est injective, dim(img f) = 0
pour rappel, le noyau d'une application linéaire f : E -> F est l'ensemble des éléments de E qui sont envoyés sur l'élément neutre de F, c'est-à-dire ker f = {x ∈ E | f(x) = 0F}.