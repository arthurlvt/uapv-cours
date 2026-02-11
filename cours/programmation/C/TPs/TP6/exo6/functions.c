#include <stdio.h>
#include <stdlib.h>
#include "include.h"

void addToCensus(Census *census, int numberOfMerles) {
    // Rescencement des merles dans le quartier
    census->sizeOfArray += 1;
    census->array[census->sizeOfArray] = numberOfMerles;
}
