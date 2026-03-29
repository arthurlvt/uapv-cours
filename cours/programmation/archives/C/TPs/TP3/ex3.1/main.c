#include <stdio.h>
#include "include.h"

int main() {
    double a, b;
    double *pA = &a;
    double *pB = &b;
    printf("Enter two integers: ");
    scanf("%lf %lf", pA, pB);
    arithmetic(&a, &b);
}
