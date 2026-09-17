#include <iostream>
#include "include.hpp"

using namespace std;

void Carte::createNewCard(int val, int coul) {
    valeur = val;
    couleur = coul;
    suiv = nullptr;
}

void Carte::deleteCard() {
    delete this;
}

Jeu::Jeu(int numberOfCards) {
    tete = nullptr;
    queue = nullptr;

    cout << "How many cards do you want to get in your set?" << endl;
    cin >> numberOfCards;

    if (numberOfCards != 32 && numberOfCards != 52) {
        cout << "Invalid number of cards. You must choose either 32 or 52 cards." << endl;
        return;
    }

    int colorCount[4] = {0, 0, 0, 0};  // compteur par couleur
    int maxPerColor = numberOfCards / 4;

    for (int val = 1; val <= numberOfCards; val++) {
        int coul;
        do {
            coul = rand() % 4;
        } while (colorCount[coul] >= maxPerColor);  // couleur pleine → retirer

        colorCount[coul]++;

        Carte* newCard = new Carte();
        newCard->createNewCard(val, coul);

        if (tete == nullptr) {
            tete = newCard;
            queue = newCard;
        } else {
            queue->suiv = newCard;
            queue = newCard;
        }
    }
}

Jeu::~Jeu() {
    Carte* current = tete;
    while (current != nullptr) {
        Carte* next = current->suiv;
        current->deleteCard();
        current = next;
    }
}

// constructeur par copie
Jeu::Jeu(const Jeu &other) {
    tete = nullptr;
    queue = nullptr;

    Carte* current = other.tete;
    while (current != nullptr) {
        addCard(current->valeur, current->couleur);
        current = current->suiv;
    }
}



void Jeu::displayCards() {
    Carte* current = tete;
    while (current != nullptr) {
        std::string displayedColor;
        if (current->couleur == 0) { displayedColor = "hearts"; }
        else if (current->couleur == 1) { displayedColor = "spades"; }
        else if (current->couleur == 2) { displayedColor = "clubs"; }
        else if (current->couleur == 3) { displayedColor = "diamonds"; }

        cout << "Card " << current->valeur << ": " << displayedColor << endl;
        current = current->suiv;
    }
}

void Jeu::concatenateCards(Jeu &J1, Jeu &J2) {
    Carte* current1 = J1.tete;
    Carte* current2 = J2.tete;

    while (current1 != nullptr) {
        Carte* newCard = new Carte();
        newCard->createNewCard(current1->valeur, current1->couleur);

        if (tete == nullptr) {
            tete = newCard;
            queue = newCard;
        } else {
            queue->suiv = newCard;
            queue = newCard;
        }
        current1 = current1->suiv;
    }

    while (current2 != nullptr) {
        Carte* newCard = new Carte();
        newCard->createNewCard(current2->valeur, current2->couleur);

        if (tete == nullptr) {
            tete = newCard;
            queue = newCard;
        } else {
            queue->suiv = newCard;
            queue = newCard;
        }
        current2 = current2->suiv;
    }

    cout << "Concatenated cards from both games:" << endl;
    displayCards();
}

void Carte::compareCards(Carte &C1, Carte &C2) {
    if (C1.valeur > C2.valeur) {
        cout << "Card 1 is stronger than Card 2." << endl;
    } else if (C1.valeur < C2.valeur) {
        cout << "Card 2 is stronger than Card 1." << endl;
    } else {
        cout << "Both cards have the same value." << endl;
    }
}

void Jeu::drawCard(Jeu &J) {
    if (tete == nullptr) {
        cout << "No cards left in the game." << endl;
        return;
    }

    Carte* drawnCard = tete;
    tete = tete->suiv;

    if (tete == nullptr) {
        queue = nullptr; // le jeu est maintenant vide
    }

    cout << "Drew card: " << drawnCard->valeur << " of color " << drawnCard->couleur << endl;
    drawnCard->deleteCard();
}

void Jeu::addCard(int val, int coul) {
    Carte* newCard = new Carte();
    newCard->createNewCard(val, coul);

    if (tete == nullptr) {
        tete = newCard;
        queue = newCard;
    } else {
        queue->suiv = newCard;
        queue = newCard;
    }
}

// void Jeu::isSorted(Jeu &J) {} 

void Jeu::split(Jeu &J1, Jeu &J2) {
    Carte* current = J1.tete;
    while (current != nullptr) {
        Carte* newCard = new Carte();
        newCard->createNewCard(current->valeur, current->couleur);

        if (J2.tete == nullptr) {
            J2.tete = newCard;
            J2.queue = newCard;
        } else {
            J2.queue->suiv = newCard;
            J2.queue = newCard;
        }
        current = current->suiv;
    }

    // Vider J1
    current = J1.tete;
    while (current != nullptr) {
        Carte* next = current->suiv;
        current->deleteCard();
        current = next;
    }
    J1.tete = nullptr;
    J1.queue = nullptr;

    cout << "Split completed. Game 1 is now empty and Game 2 has the cards." << endl;
}


// Créer une fonction pour démarrer une partie de jeu de cartes
void Jeu::startGame(Jeu &J1, Jeu &J2) {
    cout << "|------------------ Welcome to the Card Game! ------------------|" << endl;
    cout << "Player 1, please enter the number of cards you want (32 or 52): ";
    int numberOfCards;
    cin >> numberOfCards;
    Jeu player1(numberOfCards);
    Jeu player2(numberOfCards);
    cout << "Player 1's cards:" << endl;
    player1.displayCards();
    cout << "Player 2's cards:" << endl;
    player2.displayCards();
    
}
