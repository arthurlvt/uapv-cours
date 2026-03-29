#include <stdio.h>
#include <time.h>
#include "include.h"

int searchInRange(int array[], int size, int number, int x, int y) {
    for (int i = x; i < y && i < size; i++) {
        if (array[i] == number) {
            return i;
        }
    }
    return -1;
}

int countWithRange(int array[], int size, int number) {
    int count = 0;
    int index = -1;
    do {
        index = searchInRange(array, size, number, index + 1, size);
        if (index != -1) {
            count++;
        }
    } while (index != -1);
    return count;
}

// on va ensuite si on trouve plusieurs fois la meme valeur la mettre à 0
void resetValue(int array[], int size, int value) {
    for (int i = 0; i < size; i++) {
        if (array[i] == value) {
            array[i] = 0;
        }
    }
}