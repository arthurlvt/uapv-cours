// STRUCTURES AND DYNAMIC MEMORY ALLOCATION
#include <stdio.h>
#include <stdlib.h>
#include "include.h"

Census createCensus(int *array, int size) {
    Census census;
    census.array = malloc(size * sizeof(int));
    census.sizeOfArray = size;
    return census;
}

int main() {
    Census census = createCensus(NULL, 0);
    int numberOfMerles;
    printf("Enter number of merles to make a census: ");
    scanf("%d", &numberOfMerles);
    addToCensus(&census, numberOfMerles);
    for (int i = 0; i < census.sizeOfArray; i++) {
        printf("Census Value %d: %d\n", i, census.array[i]);
    }
    free(census.array);
}