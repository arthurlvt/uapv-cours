#include <cstring>
#include <vector>
#include <algorithm>
#include "levenshtein.hpp"

/* Distance de Levenshtein par programmation dynamique.
* On construit une matrice D de taille (m+1) x (n+1) où :
*  - m = longueur de v   (indice des lignes)
*  - n = longueur de w   (indice des colonnes)
*  - D[i][j] = distance entre les i premières lettres de v et les j premières lettres de w
* Initialisation :
*   D[i][0] = i  (transformer v[0..i] en "" coûte i suppressions)
*   D[0][j] = j  (transformer "" en w[0..j] coûte j insertions)
* Récurrence :
*   D[i][j] = min(  D[i-1][j]   + 1 // suppression de v[i-1]
*                 , D[i][j-1]   + 1 // insertion  de w[j-1]
*                 , D[i-1][j-1] + δ // substitution (ou égalité)
*              )
*   avec δ = 0 si v[i-1] == w[j-1], sinon 1.
* La distance finale est D[m][n].
*/
int levenshtein(const char* v, const char* w) {
    int m = (int)strlen(v);
    int n = (int)strlen(w);

    // Cas dégénérés rapides
    if (m == 0) return n;
    if (n == 0) return m;

    // Matrice (m+1) x (n+1) initialisée à 0
    std::vector<std::vector<int>> D(m + 1, std::vector<int>(n + 1, 0));

    // Initialisation des bords
    for (int i = 0; i <= m; i++) D[i][0] = i;
    for (int j = 0; j <= n; j++) D[0][j] = j;

    // Remplissage : on parcourt ligne par ligne
    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            int delta = (v[i - 1] == w[j - 1]) ? 0 : 1; // substitution ou égalité
            int suppression  = D[i - 1][j] + 1; // suppression de v[i-1]
            int insertion    = D[i][j - 1] + 1; // insertion de w[j-1]
            int substitution = D[i - 1][j - 1] + delta; // substitution ou égalité
            D[i][j] = std::min({suppression, insertion, substitution});
        }
    }
    return D[m][n];
}

// comment le programme marche concretement?
// -> l'algo de levenshtein est un algo de programmation dynamique qui calcule la distance entre deux chaînes de caractères en construisant une matrice de distances partielles. Chaque cellule de la matrice représente la distance minimale entre les préfixes des deux chaînes jusqu'à ce point. L'algorithme remplit cette matrice en utilisant les opérations de suppression, d'insertion et de substitution, et à la fin, la distance finale est trouvée dans la cellule correspondant à la longueur totale des deux chaînes.
// -> dans le contexte de ce projet, cette fonction de distance de Levenshtein est utilisée pour la fonctionnalité de correction orthographique dans l'arbre de préfixes. Lorsqu