#include <stdio.h>
#include "include.h"

int main() {
    int array[100];

    printf("Here are the initial values:\n");
    for (int i = 0; i < 100; i++) {
        printf("%d ", array[i]);
    }
    initializeArray(array, 100);
    printf("\n\nHere are the values after initialization:\n");
    for (int i = 0; i < 100; i++) {
        printf("%d ", array[i]);
    }
}
