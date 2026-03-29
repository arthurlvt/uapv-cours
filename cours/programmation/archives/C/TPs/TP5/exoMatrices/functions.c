#include "matrices.h"
#include <stdio.h>


void fillMatrix(Matrix* matrices) {
    // fill the lines and columns
    for (int i = 0; i < matrices->height ; i++) {
        for (int j = 0; j < matrices->width ; j++) {
            printf("Ligne %d, Nombre %d : ", i, j);
            scanf("%d", &matrices->arr[i][j]);
        }
    }
}

void display(Matrix* matrices) {
    for (int i = 0; i < matrices->height ; i++) {
        for (int j = 0; j < matrices->width ; j++) {
            printf("%d ", matrices->arr[i][j]);
        }
        printf("\n");
    }
}

int diagSum(Matrix* matrices) {
    int sumDiag = 0;
    int size = (matrices->height < matrices->width) ? matrices->height : matrices->width;
    for (int i = 0 ; i < size; i++) {
        sumDiag += matrices->arr[i][i];
    }
    return sumDiag;
}

int transpose(Matrix* matrices) {    
    if (matrices->height != matrices->width) {
        printf("\nErreur : La transposition in-place est risquée pour les matrices non-carrées sans allocation dynamique.\n");
        return -1; // Échec
    }
    for (int i = 0; i < matrices->height; i++) {
        for (int j = i + 1; j < matrices->width; j++) {
            // Échange (Swap) des éléments arr[i][j] et arr[j][i]
            int temp = matrices->arr[i][j];
            matrices->arr[i][j] = matrices->arr[j][i];
            matrices->arr[j][i] = temp;
        }
    }
}