#include <stdio.h>
#include "include.h"

void displayArray(int array[], int size, int numberOfTable) {
    for (int i = 0; i < size; i++) {
        printf("table%d[%d] = %d, ", numberOfTable, i, array[i]);
    }
    return;
}
void displayArrayForDouble(double array[], int size, int numberOfTable) {
    for (int i = 0; i < size; i++) {
        printf("table%d[%d] = %.2f\n", numberOfTable, i, array[i]);
    }
    return;
}