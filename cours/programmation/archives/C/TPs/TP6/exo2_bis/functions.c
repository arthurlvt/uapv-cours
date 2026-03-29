#include <stdio.h>
#include <stdlib.h>
#include "include.h"

void initTable(double **table, int n) {
    *table = malloc(n * sizeof(double));
    for (int i = 0; i < n; i++) {
        (*table)[i] = rand() % 101; // random value between 0 and 100
    }
}