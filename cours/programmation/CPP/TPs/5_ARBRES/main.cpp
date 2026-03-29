#include <iostream>
using namespace std;

class noeud
{
    int info;
    noeud *fg, *fd;
    public:
        noeud(int i, noeud *g, noeud *d) { info = i; fg = g; fd = d; };
        ~noeud() { delete fg; delete fd; };
        int depth() {
            if (fg == nullptr && fd == nullptr) return 1;
            int pfg = 0, pfd = 0;
            if (fg != nullptr) pfg = fg->depth();
            if (fd != nullptr) pfd = fd->depth(); 
            return 1 + max(pfg, pfd);
        }
        int max_2() {
            if (fg == nullptr && fd == nullptr) return info;
            int mfg = 0, mfd = 0;
            if (fg != nullptr) mfg = fg->max_2();
            if (fd != nullptr) mfd = fd->max_2();
            return max(info, max(mfg, mfd));
        }
};
class arbre
{
    noeud *racine;
    public:
        arbre() { racine = nullptr; };
        arbre(noeud *n) { racine = n; };
        ~arbre() { delete racine; };
        // obtenir la hauteur d'un arbre
        int height() {
            if (racine == nullptr) return 0;
            return racine->depth();
        }
        // maximum of values in the tree
        int max_2() {
            if (racine == nullptr) return 0;
            return racine->max_2();
        }
        // maximum dans une arbre ordonné
        
};