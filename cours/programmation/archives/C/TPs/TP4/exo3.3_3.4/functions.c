#include <stdio.h>
#include "include.h"

int IsInArray(int value, float array[], int size) {
    for (int i = 0; i < size; i++) {
        if (array[i] == value) {
            return 1; // Value found in array
        }
    }
    return 0; // Value not found in array
}

int searchInArray(int value, float array[], int size) {
    for (int i = 0; i < size; i++) {
        if (array[i] == value) {
            return i; // Return the index of the found value
        }
    }
    return -1; // Value not found in array
}