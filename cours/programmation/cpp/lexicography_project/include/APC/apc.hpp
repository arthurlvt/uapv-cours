#ifndef APC_HPP
#define APC_HPP

#include <cstdio>
#include <string>
#include <utility>
#include <vector>

class Noeud;

class Arbre {
    Noeud* racine;
    public:
        Arbre();
        Arbre(const char* fileName);
        ~Arbre();
        Arbre(const Arbre& autre);
        void insert(const char* mot);
        bool search(const char* mot) const;
        bool remove(const char* mot);
        int countWord() const;
        int lengthOfLongestWord() const;
        void save(const char* fileName) const;
        // ---- Fonctionnalités avancées ----
        // [11] Autocomplétion : renvoie tous les mots du dictionnaire qui
        //      commencent par le préfixe donné. Si aucun, renvoie un vector vide.
        std::vector<std::string> getCompletions(const char* prefixe) const;
        // [14] Correction orthographique : renvoie jusqu'à k mots du dictionnaire
        //      dont la distance de Levenshtein au mot recherché est <= seuil,
        //      triés par distance croissante. Utilise un parcours d'arbre qui
        //      maintient une ligne de la matrice de Levenshtein à chaque nœud,
        //      avec élagage (pruning) quand min(ligne) > seuil.
        std::vector<std::pair<int, std::string>>
            findClosest(const char* mot, int k, int seuil) const;
    private:
        void removeByRec(Noeud* n);
        bool removeWordByRec(Noeud*& sibling, const char* mot);
        Noeud* copyByRec(Noeud* n);
        void countByRec(Noeud* n, int& compteur) const;
        void lengthByRec(Noeud* n, int profondeur, int& max) const;
        void saveByRec(Noeud* n, char* buf, int prof, FILE* f) const;
        void collectCompletions(Noeud* n, std::string& acc, std::vector<std::string>& result) const;
        void descendCorrection(Noeud* n, const char* mot, int m, const std::vector<int>& parentRow, int seuil, std::string& acc, std::vector<std::pair<int, std::string>>& cands) const;
};

class Noeud {
    friend class Arbre;
    char info;
    Noeud* fils;
    Noeud* frere;
    public:
        Noeud(char c);
};

#endif
