#include <stdio.h>
#include "include.h"

int main() {
    float price;
    printf("Sur quel prix souhaitez-vous ajouter les taxes? ");
    scanf("%f", &price);
    printf("Le prix après application des taxes est le suivant: %.2f euros ", getPriceWithTaxes(price));
}