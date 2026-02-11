#include "include.h"
#include <stdio.h>

int modify(int *minNbr, int *maxNbr) {
    *minNbr = *minNbr * 2;
    *maxNbr = *maxNbr / 2;
    return 0;
}

int swap(int *minNbr2, int *maxNbr2) {
    int temp = *minNbr2;
    *minNbr2 = *maxNbr2;
    *maxNbr2 = temp;
    return 0;
}