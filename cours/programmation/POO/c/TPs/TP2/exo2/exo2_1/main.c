#include <stdio.h>
#include "include.h"

int main() {
    int nGrades;
    printf("Combien de notes avez-vous? ");
    scanf("%d", &nGrades);

    if (nGrades <= 0) {
        printf("Il faut au moins une note.\n");
        return 1;
    }

    float currentMean = mean(nGrades);
    printf("La moyenne de vos notes est %.2f\n", currentMean);
    return 0;
}