// EXERCICE 1 : ALLOCATION ET DESALLOCATION DYNAMIQUE
#include <stdio.h>
#include <stdlib.h>

int main() {
    int *value;
    value = malloc(sizeof(int));
    *value = 42;
    printf("Value: %d\n", *value);
    free(value);
}