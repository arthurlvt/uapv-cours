#include <time.h>
#include "include.h"

void initializeArray(int *array, int size) {
    for (int i = 0; i < size; i++) {
        array[i] = i*2;
    }
}
void fillArrayWithRandomNumbers(int* array, int size, int min, int max) {
    srand((unsigned int)time(NULL));
    for (int i = 0; i < size; i++) {
        array[i] = (rand() % (max - min + 1)) + min;
    }
}