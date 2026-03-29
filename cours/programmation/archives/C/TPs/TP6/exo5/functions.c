#include <stdio.h>
#include <stdlib.h>
#include "include.h"

void reallocateMemory(int **reallocateMemory, int value) {
    if (*reallocateMemory != NULL) {
        free(*reallocateMemory);
    }
    *reallocateMemory = malloc(sizeof(int));
    **reallocateMemory = value;
}