// EXERCICE 2.5: MAX AND MIN WITH POINTORS

#include <stdio.h>
#include "include.h"

int main() {
    int a, b, c;
    int *pA = &a;
    int *pB = &b;
    int *pC = &c;
    printf("Entrez 3 valeurs a, b, c à trier: ");
    scanf("%d %d %d", &a, &b, &c);  
    sortValues(&a, &b, &c);
    printf("Trie des valeurs: %d > %d > %d", *pC, *pB, *pA);
}