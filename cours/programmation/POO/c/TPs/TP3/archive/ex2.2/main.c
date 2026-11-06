// Ex 2.2 Opposite numbers via function and pointers
#include <stdio.h>
#include "include.h"

int main() {
    int nbr1, nbr2;
    int *pnbr1 = &nbr1;
    int *pnbr2 = &nbr2;
    printf("Entrez deux nombres entiers : ");
    scanf("%d %d", &nbr1, &nbr2);
    oppositNbr(nbr1, nbr2);
    printf("L'opposé de %d est %d\n", nbr1, -*pnbr1);
    printf("L'opposé de %d est %d\n", nbr2, -*pnbr2);
}
