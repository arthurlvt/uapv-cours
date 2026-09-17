#include "matrices.h"
#include <stdlib.h>
#include <time.h>

void fillMatrixAndPutRandomValues(Matrix* matrices) {
    for (int i = 0; i < matrices->height ; i++) {
        for (int j = 0; j < matrices->width ; j++) {
            int index = i * matrices->width + j;
            matrices->arr[index] = rand() % 10;
        }
    }
}

void display(Matrix* matrices) {
    for (int i = 0; i < matrices->height ; i++) {
        for (int j = 0; j < matrices->width ; j++) {
            int index = i * matrices->width + j;
            printf("%d ", matrices->arr[index]);
        }
        printf("\n");
    }
}