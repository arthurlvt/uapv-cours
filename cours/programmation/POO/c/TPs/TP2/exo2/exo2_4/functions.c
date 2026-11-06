#include <stdio.h>
#include <stdbool.h>

bool isPrime(int nbr) {
    if (nbr <= 1)
        return false;

    int count = 0;
    for (int i = 1; i <= nbr; i++) {
        if (nbr % i == 0)
            count++;
    }
    return count == 2;
}

int findPreviousPrime(int nbr) {
    for (int i = nbr - 1; i >= 2; i--) {
        if (isPrime(i))
            return i;
    }
    return -1; 
}

void findTwoPreviousPrimes(int nbr) {
    int first = findPreviousPrime(nbr);
    if (first == -1) {
        printf("Il n'y a pas deux nombres premiers avant %d\n", nbr);
        return;
    }
    int second = findPreviousPrime(first);
    if (second == -1) {
        printf("Il n'y a pas deux nombres premiers avant %d\n", nbr);
        return;
    }
    printf("Les deux premiers avant %d sont %d et %d\n", nbr, first, second);
}