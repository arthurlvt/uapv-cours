// REALLOCATE MEMORY
#include <stdio.h>
#include <stdlib.h>

void reallocateMemory(int **reallocateMemory, int value) {
    if (*reallocateMemory != NULL) {
        free(*reallocateMemory);
    }
    *reallocateMemory = malloc(sizeof(int));
    **reallocateMemory = value;
}
int main() {
    while(1) {
        int *value = NULL;
        int choosedValue;
        printf("Enter a value: ");
        scanf("%d", &choosedValue);
        reallocateMemory(&value, choosedValue);
        printf("Reallocated Value: %d, Adress: %p\n", *value, (void*)value, &value);
        free(value);
    }
}