#include <stdio.h>
#include "include.h"

int main() {
    int nbr1, nbr2, nbr3;
    printf("Entrez 3 entiers à comparer: ");
    if (scanf("%d %d %d", &nbr1, &nbr2, &nbr3) != 3) {
        printf("Saisie invalide.\n");
        return 1;
    }
    printf("Le max de %d, %d et %d est %d\n", nbr1, nbr2, nbr3, max3(nbr1, nbr2, nbr3));
    return 0;
}