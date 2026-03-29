// EXERCICE 2 BIS: FONCTIONS DYNAMIQUES
#include <stdio.h>
#include <stdlib.h>
#include "include.h"

int main() {
    double *table;
    int n;
    printf("Combien de valeurs voulez-vous stocker dans le tableau ? ");
    scanf("%d", &n);
    initTable(&table, n);
    printf("Les valeurs du tableau sont :\n");
    for (int i = 0; i < n; i++) {
        printf("%f ", table[i]);
    }
    free(table);
}