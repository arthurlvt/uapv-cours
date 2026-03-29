#include <stdio.h>
#include <time.h>
#include "include.h"

int main() {
    int nbr;
    printf("Enter how many values you want in the arrzay (max 100): ");
    scanf("%d", &nbr);
    if (nbr > 100) {
        nbr = 100;
    }
    int array[nbr];
    srand((unsigned int)time(0));
    // Generate random values between 0 and 1000
    for (int i = 0; i < nbr; i++) {
        array[i] = rand() % 1001;
    }
    printf("Array values:\n");
    for (int i = 0; i < nbr; i++) {
        printf("%d ", array[i]);
    }
    int minValue = getMinArray(array, nbr);
    int maxValue = getMaxArray(array, nbr);
    printf("\nMinimum value in the array: %d\n", minValue);
    printf("Maximum value in the array: %d\n", maxValue);
}