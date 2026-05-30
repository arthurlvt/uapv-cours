#ifndef TAB_HPP
#define TAB_HPP

// ============================================================================
// Tableau dynamique trié de mots (représentation alternative au dico)
//
// Stratégie de stockage :
//   - buf : un seul grand tableau char où tous les mots sont concaténés,
//           chacun séparé par son '\0' final (chaque mot reste donc une
//           C-string utilisable avec strcmp, strlen, ...)
//   - tab : un tableau de pointeurs char*, chaque case pointe sur le début
//           d'un mot dans buf
//   - nb  : nombre de mots stockés
//   - tab est trié par ordre alphabétique APRÈS chargement, ce qui permet
//     une recherche dichotomique en O(log nb).
// ============================================================================

class Tab {
    char*  buf;
    char** tab;
    int nb;
    int taille_buf;
    public:
        Tab();
        Tab(const char* fileName);
        ~Tab();
        Tab(const Tab& autre);
        bool search(const char* mot) const;
        int  countWord() const { return nb; }
};

#endif
