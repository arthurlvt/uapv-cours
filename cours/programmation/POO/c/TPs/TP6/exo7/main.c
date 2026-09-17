#include <stdio.h>
#include <stdlib.h>
#include <time.h>

Matrix createMatrices(int height, int width) {
    Matrix matrices;
    matrices.height = height; 
    matrices.width = width;
    matrices.arr = (int*)malloc(height * width * sizeof(int));
    return matrices;
}

int main() {
    srand(time(NULL)); 
    int height = 3;
    int width = 4;
    Matrix matrices = createMatrices(height, width);
    fillMatrixAndPutRandomValues(&matrices);
    printf("Matrice (%d x %d):\n", height, width);
    display(&matrices);
    free(matrices.arr);
}
