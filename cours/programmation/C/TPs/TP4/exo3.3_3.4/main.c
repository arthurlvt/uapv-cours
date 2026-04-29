#include <stdio.h>
#include "include.h"

int main() {
    int n, valueToCheck;
    printf("How many values do you want in the array? ");
    scanf("%d", &n);
    float array[n];
    srand((unsigned int)time(0));
    for (int i = 0; i < n; i++) {
        array[i] = rand() % 1001;
    }
    printf("Array values:\n");
    for (int i = 0; i < n; i++) {
        printf("%d ", (int)array[i]);
    }
    printf("\n");

    while (valueToCheck != -1) {
        printf("Enter a value to check: (-1 to quit) ");
        scanf("%d", &valueToCheck);
        int index = searchInArray(valueToCheck, array, n);
        if (index != -1) {
            printf("The value %d is in the array, at the case %d\n", valueToCheck, index);
        } else {
            printf("The value %d is not in the array.\n", valueToCheck);
        }
    }
}