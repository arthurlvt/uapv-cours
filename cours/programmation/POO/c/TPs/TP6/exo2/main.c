// EXERCICE 2 : TABLEAU DYNAMIQUE
#include <stdio.h>
#include <stdlib.h>

int main() {
    // generate random value for table
    int n;
    printf("Combien de valeurs voulez-vous stocker dans le tableau ? ");
    scanf("%d", &n);
    double *array = malloc(n * sizeof(double));
    for (int i = 0; i < n; i++) {
        array[i] = rand() % 101; // random value between 0 and 100
    }
    printf("Les valeurs du tableau sont :\n");
    for (int i = 0; i < n; i++) {
        printf("%d ", array[i]);
    }
    free(array);
}