#include <stdio.h>
#include "include.h"

void displayArray(int arr[], int size) {
    printf("Tableau après modification: ");
    for(int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}