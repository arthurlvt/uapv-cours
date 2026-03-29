#include <stdio.h>
#include "include.h"

int main() {
    double a, b, c;
    double *pA = &a;
    double *pB = &b;
    double *pC = &c;
    printf("Entrez 3 valeurs a, b, c: ");
    scanf("%lf %lf %lf", &a, &b, &c);
    sortValues(&a, &b, &c);
    printf("Max des valeurs: %.4f\nMin des valeurs: %.4f", *pC, *pA);
}
