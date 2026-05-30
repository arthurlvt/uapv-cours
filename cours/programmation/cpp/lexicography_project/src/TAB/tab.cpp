#include <cstdio>
#include <cstdlib>
#include <cstring>
#include "TAB/tab.hpp"

// Comparateur pour qsort : qsort travaille avec des éléments génériques (void*). 
// Notre tableau est un char** : chaque élément est un char*. 
// Donc quand qsort passe au comparateur deux "éléments", ce sont des adresses de char* (i.e. char**).
// On déréférence pour obtenir les char*, puis on compare avec strcmp.
static int comparePointersToStrings(const void* a, const void* b) {
    const char* sa = *(const char* const*)a;
    const char* sb = *(const char* const*)b;
    return strcmp(sa, sb);
}

// constructeur sans argument
Tab::Tab() : buf(nullptr), tab(nullptr), nb(0), taille_buf(0) {}

// constructeur depuis le fichier
Tab::Tab(const char* fileName) : buf(nullptr), tab(nullptr), nb(0), taille_buf(0) {
    FILE* f = fopen(fileName, "r");
    if (f == nullptr) {
        fprintf(stderr, "Erreur ouverture du fichier : %s\n", fileName);
        return;
    }

    char tmp[256];
    while (fscanf(f, "%255s", tmp) == 1) {
        nb++;
        taille_buf += (int)strlen(tmp) + 1;  // +1 pour le '\0' final
    }
    if (nb == 0) { 
        fclose(f);
        return;
    }
    buf = new char[taille_buf];
    tab = new char*[nb];

    rewind(f);
    int offset = 0, i = 0;
    while (fscanf(f, "%255s", tmp) == 1) {
        int len = (int)strlen(tmp);
        memcpy(buf + offset, tmp, len + 1); // copie y compris le '\0'
        tab[i] = buf + offset;
        offset += len + 1;
        i++;
    }
    fclose(f);

    qsort(tab, nb, sizeof(char*), comparePointersToStrings);
}

// destructeur
Tab::~Tab() {
    delete[] buf;
    delete[] tab;
}

// constructeur par recopie
Tab::Tab(const Tab& autre): buf(nullptr), tab(nullptr), nb(0), taille_buf(0) {
    if (autre.nb == 0) return;
    nb = autre.nb;
    taille_buf = autre.taille_buf;
    buf = new char[taille_buf];
    memcpy(buf, autre.buf, taille_buf);
    tab = new char*[nb];
    for (int i = 0; i < nb; i++) tab[i] = buf + (autre.tab[i] - autre.buf);
}

// search : recherche binaire dans le tableau trié
bool Tab::search(const char* mot) const {
    if (nb == 0) return false;
    int lo = 0, hi = nb - 1;
    while (lo <= hi) {
        int mid = (lo + hi) / 2;
        int cmp = strcmp(mot, tab[mid]); // strcmp renvoie <0, 0, >0 selon que mot est respectivement <, =, > tab[mid]
        if (cmp == 0) return true;
        if (cmp < 0)  hi = mid - 1;
        else lo = mid + 1;
    }
    return false;
}