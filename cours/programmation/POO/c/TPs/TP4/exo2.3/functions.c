#include <stdio.h>
#include "include.h"

int isPrime(int number) {
    if (number <= 1) {
        return 0;
    }
    for (int i = 2; i * i <= number; i++) {
        if (number % i == 0) {
            return 1;
        }
    }
    return 0;
}

void putPrimesNumberInArray(int* array, int size) {
    int index = 0;
    for (int num = 2; index < size; num++) {
        if (isPrime(num) == 0) {
            array[index++] = num;
        }
    }
}