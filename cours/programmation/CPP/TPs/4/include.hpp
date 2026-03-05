#ifndef INCLUDE_HPP
#define INCLUDE_HPP

#include <iostream>
using namespace std;

class Carte {
    friend class Jeu;
    int valeur;
    int couleur = -1;  // -1: undefined, 0: hearts, 1: spades, 2: clubs, 3: diamonds
    Carte *suiv;
    void createNewCard(int val, int coul);
    void deleteCard();
    void compareCards(Carte &C1, Carte &C2);
};

class Jeu {
    Carte *tete; // pointeur vers la première carte du jeu
    Carte *queue; // pointeur vers la dernière carte du jeu

    public:
        Jeu(int numberOfCards);
        ~Jeu();
        void displayCards();
        void concatenateCards(Jeu &J1, Jeu &J2);
        void drawCard(Jeu &J);
        void addCard(int val, int coul);
        void split(Jeu &J1, Jeu &J2);
        void startGame(Jeu &J1, Jeu &J2);
};


#endif // INCLUDE_HPP