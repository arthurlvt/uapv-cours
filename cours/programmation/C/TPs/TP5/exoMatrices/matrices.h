#include <stdio.h>
#include "main.c"
#include "functions.c"

# ifndef MATRICES_H
# define MATRICES_H

typedef struct {
    int height;
    int width;
    int arr[3][3];
} Matrix;

Matrix createMatrices(int height, int width);
void fillMatrix(Matrix* matrices);
void display(Matrix* matrices);
int diagSum(Matrix* matrices);
int transpose(Matrix* matrices);

# endif