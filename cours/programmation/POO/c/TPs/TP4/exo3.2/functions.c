#include <stdio.h>
#include "include.h"

int getUserGrades(float grades[], int maxGrades) {
    float grade;
    int count = 0;
    printf("Enter grades (negative number to stop):\n");
    while (count < maxGrades) {
        printf("Grade %d: ", count + 1);
        scanf("%f", &grade);
        if (grade < 0) {
            break;
        }
        grades[count] = grade;
        count++;
    }
    return count;
}

float meanCalculation(float grades[], int numGrades) {
    float sum = 0.0;
    for (int i = 0; i < numGrades; i++) {
        sum += grades[i];
    }
    return (numGrades > 0) ? (sum / numGrades) : 0.0;
}