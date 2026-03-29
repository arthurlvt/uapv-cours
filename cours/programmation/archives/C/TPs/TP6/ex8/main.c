#include <stdio.h>
#include <stdlib.h> // Nécessaire pour malloc et free

typedef struct {
    DynamicArray dArray;
    int *array;
    int size;
} DynamicArray;

void displayArray(DynamicArray dArray) {
    for (int i = 0; i < dArray.size; i++) {
        printf("%d ", dArray.array[i]);
    }
    printf("\n");
}
void addValue(DynamicArray *dArray, int *valueToAdd) {
    if(dArray.array[])
}

int main() {
    DynamicArray dArray;
    int nbr, valueToAdd, size, capacity, casePosition = 0;
    int *pValueToAdd = &valueToAdd;
    dArray.array = (int *)malloc(1 * sizeof(int)); 

    printf("Entrez un entier : ");
    scanf("%d", &nbr);

    dArray.array[0] = nbr;
    printf("--- Résultat ---\n");
    displayArray(dArray);
    printf("Entrez une valeur à ajouter : ");
    scanf("%d", &valueToAdd);
    addValue(array, pValueToAdd);
    free(array);
}