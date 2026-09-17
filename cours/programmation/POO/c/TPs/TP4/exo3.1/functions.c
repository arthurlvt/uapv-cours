#include <stdio.h>
#include "include.h"

int getMinArray(int array[], int size) {
    if (size <= 0) {
        return 0;
    }
    int min = array[0];
    for (int i = 1; i < size; i++) {
        if (array[i] < min) {
            min = array[i];
        }
    }
    return min;
}
int getMaxArray(int array[], int size) {
    if (size <= 0) {
        return 0;
    }
    int max = array[0];
    for (int i = 1; i < size; i++) {
        if (array[i] > max) {
            max = array[i];
        }
    }
    return max;
}