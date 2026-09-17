#include <stdio.h>
#include <stdlib.h>
#include "include.h"

void memoryLeak() {
    while (1) {
        double *leakTable = malloc(100000000 * sizeof(double)); // allocate 100 doubles continuously
        printf("Allocated 100 doubles at address %p\n", (void*)leakTable);
        free(leakTable); // memory leak occurs here
    }
}