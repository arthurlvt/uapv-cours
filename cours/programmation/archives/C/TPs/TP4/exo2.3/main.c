#include <stdio.h>
#include "include.h"

int main() {
    int primes[100];
    putPrimesNumberInArray(primes, 100);
    printf("The first 100 prime numbers are:\n");
    for (int i = 0; i < 100; i++) {
        printf("%d ", primes[i]);
    }
    printf("\n");
}