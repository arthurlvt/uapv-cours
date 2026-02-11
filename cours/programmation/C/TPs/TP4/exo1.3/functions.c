#include <stdio.h>
#include "include.h"

void initializeArray(int *array, int size) {
    for (int i = 0; i < size; i++) {
        array[i] = i;
    }
}