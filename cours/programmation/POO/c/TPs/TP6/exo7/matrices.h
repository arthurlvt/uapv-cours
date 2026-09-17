#include <stdio.h>

#ifndef MATRICES_H
#define MATRICES_H

typedef struct {
    int height;
    int width;
    int* arr;
} Matrix;

Matrix createMatrices(int height, int width);
void fillMatrixAndPutRandomValues(Matrix* matrices);
void display(Matrix* matrices);

# endif