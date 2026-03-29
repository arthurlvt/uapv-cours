#include "include.h"
#include <stdio.h>

int swap(int *minNbr2, int *maxNbr2) {
    int temp = *minNbr2;
    *minNbr2 = *maxNbr2;
    *maxNbr2 = temp;
    return 0;
}

void sortValues(int *a, int *b, int *c) {
    int temp;
    if(*a > *b) {
        temp = *a;
        *a = *b;
        *b = temp;
    }
    if(*b > *c) {
        temp = *b;
        *b = *c;
        *c = temp;
    }
    if(*a > *b) {
        temp = *a;
        *a = *b;
        *b = temp;
    }
}