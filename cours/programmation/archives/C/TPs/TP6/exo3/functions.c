#include <stdio.h>
#include <stdlib.h>
#include "include.h"

void getTablePositiveValues(int *table, int n, int **positiveTable, int *positiveCount) {
    *positiveCount = 0;
    for (int i = 0; i < n; i++) {
        if (table[i] > 0) {
            (*positiveCount)++;
        }
    }
    *positiveTable = malloc((*positiveCount) * sizeof(int));
    int index = 0;
    for (int i = 0; i < n; i++) {
        if (table[i] > 0) {
            (*positiveTable)[index++] = table[i];
        }
    }
}