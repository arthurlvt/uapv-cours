#include <stdio.h>
#include <stdlib.h>

int main() {
    int z;
    int *pZ = &z;
    *pZ = 100;
    // or
    int e;
    int *pE = &e;
    pE = 25;
}