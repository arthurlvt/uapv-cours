#include <cstdio>
#include <cstring>
#include <algorithm>
#include "APC/apc.hpp"

Noeud::Noeud(char c) : info(c), fils(nullptr), frere(nullptr) {}

// constructeur sans argument : crée un arbre vide (racine avec info='\0' mais ne représente pas un mot)
Arbre::Arbre() : racine(nullptr) { 
    racine = new Noeud('\0');
}

// constructeur depuis le fichier : crée un arbre vide, puis insère tous les mots du fichier
Arbre::Arbre(const char* fileName) : racine(nullptr) {
    racine = new Noeud('\0');
    FILE* f = fopen(fileName, "r");
    if (f == nullptr) {
        fprintf(stderr, "Erreur ouverture du fichier : %s\n", fileName);
        return;
    }
    char buf[256];
    while (fscanf(f, "%255s", buf) == 1) {
        insert(buf);
    }
    fclose(f);
}

// constructeur par recopie : utilise un helper récursif pour copier tous les nœuds de l'autre arbre
Arbre::Arbre(const Arbre& autre) : racine(nullptr) {
    racine = copyByRec(autre.racine);
}

// helper récursif pour le constructeur par recopie
Noeud* Arbre::copyByRec(Noeud* n) {
    if (n == nullptr) return nullptr;
    Noeud* nouveau = new Noeud(n->info);
    nouveau->fils = copyByRec(n->fils);
    nouveau->frere = copyByRec(n->frere);
    return nouveau;
}

// destructeur de Arbre
Arbre::~Arbre() {
    racine = nullptr;
}

// helper récursif pour le destructeur : parcours en post-ordre pour supprimer tous les nœuds
void Arbre::removeByRec(Noeud* n) {
    if (n == nullptr) return;
    removeByRec(n->fils);
    removeByRec(n->frere);
    delete n;
}

// fonction d'insertion : descend dans l'arbre lettre par lettre, en créant les nœuds. Le mot est terminé par un '\0' pour marquer la fin du mot
void Arbre::insert(const char* mot) {
    Noeud* courant = racine;
    int i = 0;
    while (true) {
        char c = mot[i];
        Noeud* prev = nullptr;
        Noeud* cur  = courant->fils;
        while (cur != nullptr && cur->info < c) {
            prev = cur;
            cur  = cur->frere;
        }
        if (cur != nullptr && cur->info == c) courant = cur;
        else {
            Noeud* nouveau = new Noeud(c);
            nouveau->frere = cur;
            if (prev == nullptr) courant->fils = nouveau;
            else prev->frere = nouveau;
            courant = nouveau;
        }
        if (c == '\0') break;
        i++;
    }
}

// search : descend dans l'arbre lettre par lettre.
bool Arbre::search(const char* mot) const {
    Noeud* courant = racine;
    int i = 0;
    while (true) {
        char c = mot[i];
        Noeud* cur = courant->fils;
        while (cur != nullptr && cur->info < c) cur = cur->frere;
        if (cur == nullptr || cur->info != c) return false;  // lettre absente
        if (c == '\0') return true;                          // mot complet trouvé
        courant = cur;
        i++;
    }
}

// remove : supprime le mot du dictionnaire + noeuds inutiles
bool Arbre::remove(const char* mot) {
    return removeWordByRec(racine->fils, mot);
}

// Le helper récursif prend une RÉFÉRENCE au pointeur (Noeud*&) qui pointe
// vers la chaîne de frères courante : ainsi, quand on retire un nœud, on
// peut directement modifier ce pointeur dans le parent
bool Arbre::removeWordByRec(Noeud*& sibling, const char* mot) { 
    Noeud* prev = nullptr;
    Noeud* cur  = sibling;
    while (cur != nullptr && cur->info < mot[0]) {
        prev = cur;
        cur  = cur->frere;
    }
    if (cur == nullptr || cur->info != mot[0]) return false;  // mot absent


    if (mot[0] == '\0') {
        if (prev == nullptr) sibling = cur->frere;
        else prev->frere = cur->frere;
        delete cur;
    } else {
        bool ok = removeWordByRec(cur->fils, mot + 1);
        if (!ok) return false;  // le mot n'existait pas plus bas
    }

    if (mot[0] == '\0' || cur->fils == nullptr) {
        if (prev == nullptr) sibling = cur->frere;
        else prev->frere = cur->frere;
        delete cur;
    }
    return true;
}


// countWord : compte le nombre de mots = nombre de '\0' dans l'arbre (hors racine)
int Arbre::countWord() const {
    int compteur = 0;
    countByRec(racine->fils, compteur);
    return compteur;
}

// helper récursif pour countWord : parcours en profondeur, incrémente le compteur à chaque '\0' rencontré
void Arbre::countByRec(Noeud* n, int& compteur) const {
    if (n == nullptr) return;
    if (n->info == '\0') compteur++;
    else countByRec(n->fils, compteur);
    countByRec(n->frere, compteur);
}


// lengthOfLongestWord : profondeur max d'un '\0' moins 1 (le '\0' final ne fait pas partie du mot)
int Arbre::lengthOfLongestWord() const {
    int max = 0;
    lengthByRec(racine->fils, 1, max);
    return max;
}

void Arbre::lengthByRec(Noeud* n, int profondeur, int& max) const {
    if (n == nullptr) return;
    if (n->info == '\0') {
        if (profondeur - 1 > max) max = profondeur - 1;
    } else {
        lengthByRec(n->fils, profondeur + 1, max);
    }
    lengthByRec(n->frere, profondeur, max);
}

// save : écrit tous les mots du dictionnaire dans le fichier, un par ligne.
// On utilise un buffer dimensionné par lengthOfLongestWord(), et on accumule les lettres au fil de la descente.
void Arbre::save(const char* fileName) const {
    FILE* f = fopen(fileName, "w");
    if (f == nullptr) {
        fprintf(stderr, "Erreur ouverture pour écriture : %s\n", fileName); // ici stderr pour ne pas écraser le fichier d'origine
        return;
    }
    int taille = lengthOfLongestWord() + 2;  // +1 pour '\0', +1 sécurité
    char* buf = new char[taille];
    saveByRec(racine->fils, buf, 0, f);
    delete[] buf;
    fclose(f);
}

void Arbre::saveByRec(Noeud* n, char* buf, int prof, FILE* f) const {
    if (n == nullptr) return;
    if (n->info == '\0') {
        buf[prof] = '\0';
        fprintf(f, "%s\n", buf);
    } else {
        buf[prof] = n->info;
        saveByRec(n->fils, buf, prof + 1, f);
    }
    saveByRec(n->frere, buf, prof, f);
}


// [getCompletions : descend dans l'arbre jusqu'à la fin du préfixe, puis
// collecte tous les mots du sous-arbre restant. Si une lettre du préfixe est absente, renvoie un vector vide.
std::vector<std::string> Arbre::getCompletions(const char* prefixe) const {
    std::vector<std::string> result;
    // on suit le préfixe lettre par lettre dans l'arbre.
    Noeud* courant = racine;
    for (int i = 0; prefixe[i] != '\0'; i++) {
        char c = prefixe[i];
        Noeud* cur = courant->fils;
        while (cur != nullptr && cur->info < c) cur = cur->frere;
        if (cur == nullptr || cur->info != c) return result;  // préfixe absent
        courant = cur;
    }

    //courant pointe sur la dernière lettre du préfixe. 
    //On parcourt son sous-arbre (via courant->fils) en accumulant les lettres dans `acc`, initialisé avec le préfixe.
    std::string acc(prefixe);
    collectCompletions(courant->fils, acc, result);
    return result;
}

// Helper : parcours en profondeur du sous-arbre, avec backtracking. ('\0' = mot complet, sinon on ajoute 'acc' à la lettre et on déscends, enleve la lettre au retour, puis continue dans les frères).
void Arbre::collectCompletions(Noeud* n,
                               std::string& acc,
                               std::vector<std::string>& result) const {
    if (n == nullptr) return;

    if (n->info == '\0') {
        result.push_back(acc); // mot complet : on copie l'accumulateur
    } else {
        acc.push_back(n->info); // descend : on étend le préfixe
        collectCompletions(n->fils, acc, result);
        acc.pop_back(); // backtrack : on retire la lettre ajoutée
    }

    collectCompletions(n->frere, acc, result);
}


// findClosest : correction orthographique via descente dans l'arbre.
// À la racine, on commence avec la ligne D[j] = j (m+1 cases).
// Quand on descend dans un nœud porteur d'une lettre c, on calcule la nouvelle ligne D' à partir de D (récurrence de Levenshtein).
// Si min(D') > seuil, on n'explore pas ce sous-arbre (élagage).
// Quand on tombe sur un '\0' (mot complet), D[m] est la distance entre le mot trouvé et le mot recherché ; on l'ajoute aux candidats si <= seuil.
// À la fin, on trie les candidats par distance croissante et on garde les k premiers.
std::vector<std::pair<int, std::string>>
Arbre::findClosest(const char* mot, int k, int seuil) const {
    int m = (int)strlen(mot);

    // Ligne initiale à la racine : D[j] = j (transformer "" en mot[0..j])
    std::vector<int> initialRow(m + 1);
    for (int j = 0; j <= m; j++) initialRow[j] = j;

    std::vector<std::pair<int, std::string>> candidats;
    std::string acc;
    descendCorrection(racine->fils, mot, m, initialRow, seuil, acc, candidats);

    // Tri par distance croissante (les paires se comparent lexicographiquement,
    // donc d'abord par int puis par string : ordre stable et naturel).
    std::sort(candidats.begin(), candidats.end());

    // On tronque à k au maximum
    if ((int)candidats.size() > k) candidats.resize(k);
    return candidats;
}

void Arbre::descendCorrection(Noeud* n,
                              const char* mot, int m,
                              const std::vector<int>& parentRow,
                              int seuil,
                              std::string& acc,
                              std::vector<std::pair<int, std::string>>& cands) const {
    if (n == nullptr) return;

    if (n->info == '\0') {
        // Mot complet : la distance est parentRow[m].
        int dist = parentRow[m];
        if (dist <= seuil) {
            cands.push_back(std::make_pair(dist, acc));
        }
        // On continue avec les frères du '\0' (mêmes parents, même ligne).
        descendCorrection(n->frere, mot, m, parentRow, seuil, acc, cands);
        return;
    }

    // Nœud porteur d'une lettre : on calcule la nouvelle ligne.
    char c = n->info;
    std::vector<int> newRow(m + 1);
    newRow[0] = parentRow[0] + 1;
    int minVal = newRow[0];
    for (int j = 1; j <= m; j++) {
        int delta = (mot[j - 1] == c) ? 0 : 1;
        int sup = parentRow[j]     + 1; // suppression
        int ins = newRow[j - 1]    + 1; // insertion
        int sub = parentRow[j - 1] + delta;
        newRow[j] = std::min({sup, ins, sub});
        if (newRow[j] < minVal) minVal = newRow[j];
    }

    // Élagage : si min(newRow) > seuil, inutile de descendre — toutes les distances dans ce sous-arbre seront supérieures à seuil.
    if (minVal <= seuil) {
        acc.push_back(c);
        descendCorrection(n->fils, mot, m, newRow, seuil, acc, cands);
        acc.pop_back();
    }

    // Frères de n : ils descendent du même parent, donc même parentRow.
    descendCorrection(n->frere, mot, m, parentRow, seuil, acc, cands);
}
