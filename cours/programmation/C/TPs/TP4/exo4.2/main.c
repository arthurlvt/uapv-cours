#include <stdio.h>
#include <time.h>
#include "include.h"

int main() {
    int size, occurences;
    printf("How many values do you want to get in the array?");
    scanf("%d", &size);
    int array[size];
    srand((unsigned int)time(0));
    for (int i = 0; i < size; i++) {
        array[i] = rand() % 100;
    }
    int nbrTimes = 0;
    while (nbrTimes != -1) {
        printf("Enter the number you want to check: ");
        scanf("%d", &nbrTimes);
        occurences = countWithRange(array, size, nbrTimes);
        if (occurences >= 2) {
            removeValue(array, &size, nbrTimes);
            printf("The number %d appears %d times in the array and has been removed: \n ", nbrTimes, occurences);
            for (int i = 0; i < size; i++) {
                printf("%d ", array[i]);
            }
            printf("\n");
        } else if (nbrTimes != -1) {
            printf("The number %d does not appear in the array.\n", nbrTimes);
        }
    }
    return 0;
}