#include <stdio.h>
#include "include.h"

int main() {
    int countGrades;
    printf("How many grades do you have? ");
    scanf("%d", &countGrades);
    float grades[countGrades];
    int numGrades = getUserGrades(grades, countGrades);
    for (int i = 0; i < numGrades; i++) {
        printf("Grade %d: %.2f\n", i + 1, grades[i]);
    }
    float mean = meanCalculation(grades, numGrades);
    printf("Mean of the grades: %.2f\n", mean);
    return 0;
}