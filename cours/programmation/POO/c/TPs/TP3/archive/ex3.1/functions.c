#include <stdio.h>
#include "include.h"

void arithmetic(double *a, double *b) {
    double sum = *a + *b;
    double factor = (*a) * (*b);
    printf("Somme de a et b: %.4f\nProduit de a et b: %.4f", sum, factor);
}