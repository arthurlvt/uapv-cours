#include <stdio.h>
#include "include.h"

int main() {
    float number = 0;
    printf("Entrez un nombre dont vous souhaitez obtenir son opposé: ");
    scanf("%f", &number);
    printf("L'opposé de %.2f est %.2f", number, getOpposite(number));
}