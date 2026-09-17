// EXERCICE 3 - PARTIE B : Compteur selon un délimiteur

#include <stdio.h>
int main(void) {
    int binf, bsup, delimiteur;
    int compteurinf = 0;
    int compteursup = 0;
    printf("Veuillez entrer la borne inferieure: ");
    if (scanf("%d", &binf) != 1) return 1;
    printf("Veuillez entrer la borne superieure: ");
    if (scanf("%d", &bsup) != 1) return 1;
    printf("Veuillez entrer le delimiteur: ");
    if (scanf("%d", &delimiteur) != 1) return 1;

    if (binf > bsup) { int tmp = binf; binf = bsup; bsup = tmp; }

    for (int i = binf; i <= bsup; i++) {
        if (i < delimiteur) compteurinf++;
        else compteursup++;
    }
    printf("Compteur inferieur: %d\n", compteurinf);
    printf("Compteur superieur (>= delimiteur): %d\n", compteursup);
}