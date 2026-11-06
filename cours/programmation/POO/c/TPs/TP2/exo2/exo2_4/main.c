#include <stdio.h>
#include <stdbool.h>
#include "include.h"

int main() {
    int nbr;
    printf("Entrez un entier: ");
    if (scanf("%d", &nbr) != 1) {
        printf("Saisie invalide.\n");
        return 1;
    }
    if (isPrime(nbr)) {
        printf("%d est premier", nbr);
    } else {
        printf("%d n'est pas premier", nbr);
    }
    findTwoPreviousPrimes(nbr);
    return 0;
}