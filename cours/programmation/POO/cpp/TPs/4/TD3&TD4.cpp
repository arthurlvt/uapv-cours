#include <iostream>

using namespace std;

class Maillon {
public:
    int Info;
    Maillon* suivant;

};

class Liste {
public:
    Maillon* tete;
    Liste();
    Liste(int tab[], int taille);
    void afficher();
    ~Liste();
    bool chercher(int v);
    bool chercher2(int v);
    int Nb_occurences(int val);
    void deleteOccurences(int val);
};

// 1. Constructeur vide
Liste::Liste() {
    tete = nullptr;
}

// 2. Maillon vide
Maillon::Maillon() {
    Info = 0;
    suivant = nullptr;
}

// 3. Constructeur Maillon avec une valeur
Maillon::Maillon(int val) {
    Info = val;
    suivant = nullptr;
}

// 3bis. Constructeur Maillon avec une valeur et un pointeur suivant
Maillon::Maillon(int val, Maillon* suiv) {
    Info = val;
    suivant = suiv;
}

// 4. Constructeur de liste avec tableau d'entiers
Liste::Liste(int tab[], int taille) {
    tete = nullptr;
    for (int i = 0; i < taille; i++) {
        Maillon* nouveau = new Maillon(tab[i]);
        if (tete == nullptr) {
            tete = nouveau;
        } else {
            Maillon* temp = tete;
            while (temp->suivant != nullptr) {
                temp = temp->suivant;
            }
            temp->suivant = nouveau;
        }
    }
}

// 5. Affichage de la liste
void Liste::afficher() {
    Maillon* temp = tete;
    while (temp != nullptr) {
        cout << temp->Info << " ";
        temp = temp->suivant;
    }
    cout << endl;
}

// 6. Destructeur de la liste
Liste::~Liste() {
    Maillon* temp = tete;
    while (temp != nullptr) {
        Maillon* suivant = temp->suivant;
        delete temp;
        temp = suivant;
    }
};

// 7.

//8. 
bool Liste::chercher(in v) {
    Maillon *elem = tete;
    while (elem != nullptr) {
        if (elem->Info == v) {
            return true;
    elem = elem->suivant;
    }
    return false;
}

// 9.
bool Liste::chercher2(int v) {
    Maillon *elem = tete;
    while (elem != nullptr && elem->Info <= v) {
        elem = elem->suivant;
    if (elem != nullptr && elem->Info == v) { return true; }
    if (elem != nullptr && elem->Info > v) { return false; }
    }
    return false;
}

// 10.
int Liste::Nb_occurences(int val) {
    int occurences = 0;
    Maillon *elem = tete;
    while (elem != nullptr) {
        if (elem->Info == val) {
            occurences++;
        }
        elem = elem->suivant;
    }
    return occurences;
}

// 11. Supprimer toutes les occurrences d'une valeur donnée
void Liste::deleteOccurences(int val) {
    int occurences = 0;
    Maillon *elem = tete;
    Maillon *prev = nullptr;
    while (elem != nullptr) {
        if (elem->Info == val) {
            occurences++;
            if (prev == nullptr) {
                tete = elem->suivant;
            } else {
                prev->suivant = elem->suivant;
            }
            Maillon *temp = elem;
            elem = elem->suivant;
            delete temp;
        } else {
            prev = elem;
            elem = elem->suivant;
        }
    }
    cout << "Nombre d'occurences supprimées: " << occurences << endl;
}

void Liste::inSeter(int x) {
    if(this->state == NULL) { 
        this->state = new Maillon(x); 
        return ;
    }

    Maillon *pc = tete;
    Maillon *pr = NULL;

    while(pc != NULL & pc->info < x) {
        pr = pc;
        pc = pc->suiv;
    } // pc pointe vers soit NULL soit le premier maillon de la valeur >= x
    if(pr == NULL) {
        this->state = new Maillon(x, pc);
        return;
    }
    pr->suiv = new Maillon(x, pc);
}

void Liste::SupprimerTout(int v) {
    Maillon *pc = tete;
    Maillon *pr = NULL;

    while(pc != NULL && pc->info < x) {
        if(pc->info == v) {
            if(pr == NULL) {
                tete = tete->suiv;
                pc->suiv = NULL;
                delete pc;
            
            }
            else {
                pr->suiv = pc->suiv;
                pc->suiv = NULL;
                
            }
        }
    }
}

void Liste::concat(Liste &L1, Liste &L2) {
    Maillon *pc1 = L1.tete;
    Maillon *pc2 = L2.tete;
    Maillon *pr = NULL;

    while(pc1 != NULL && pc2 != NULL) {
        if(pc1->info < pc2->info) {
            if(pr == NULL) {
                this->tete = new Maillon(pc1->info);
                pr = this->tete;
            }
            else {
                pr->suiv = new Maillon(pc1->info);
                pr = pr->suiv;
            }
            pc1 = pc1->suiv;
        }
        else {
            if(pr == NULL) {
                this->tete = new Maillon(pc2->info);
                pr = this->tete;
            }
            else {
                pr->suiv = new Maillon(pc2->info);
                pr = pr->suiv;
            }
            pc2 = pc2->suiv;
        }
    }

    while(pc1 != NULL) {
        if(pr == NULL) {
            this->tete = new Maillon(pc1->info);
            pr = this->tete;
        }
        else {
            pr->suiv = new Maillon(pc1->info);
            pr = pr->suiv;
        }
        pc1 = pc1->suiv;
    }

    while(pc2 != NULL) {
        if(pr == NULL) {
            this->tete = new Maillon(pc2->info);
            pr = this->tete;
        }
        else {
            pr->suiv = new Maillon(pc2->info);
            pr = pr->suiv;
        }
        pc2 = pc2->suiv;
    }
}