#include <stdio.h>
#include "include.h"

void sortValues(double *a, double *b, double *c) {
    double temp;
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