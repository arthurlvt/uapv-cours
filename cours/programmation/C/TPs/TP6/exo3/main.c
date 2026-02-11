// EXERCICE 3: GET POSITIVE VALUES
#include <stdio.h>
#include <stdlib.h>
#include "include.h"

int main() {
    int n;
    printf("Combien de valeurs voulez-vous stocker dans le tableau ? ");
    scanf("%d", &n);
    int *table = malloc(n * sizeof(int));
    for (int i = 0; i < n; i++) {
        table[i] = (rand() % 201) - 100; // random value between -100 and 100
    }
    int *positiveTable;
    int positiveCount;
    getTablePositiveValues(table, n, &positiveTable, &positiveCount);
    printf("Les valeurs positives du tableau sont :\n");
    for (int i = 0; i < positiveCount; i++) {
        printf("%d ", positiveTable[i]);
    }
    free(table);
    free(positiveTable);
} 