#include <stdio.h>

int triangle(void) {
    printf("Triangle d'étoiles \n");
    int nbr, count;
    printf("Entrez un nombre de lignes: ");
    scanf("%d", &nbr);
    for (int i = 1; i <= nbr; i++) {
        for (int j = 1; j <= i; j++) {
            printf("*");
        }
        printf("\n");
    }
    return 0;
}