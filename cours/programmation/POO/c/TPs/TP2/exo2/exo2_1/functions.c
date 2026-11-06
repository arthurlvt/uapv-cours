#include <stdio.h>

float addGrade(float sumGrades, float grade) {
    return sumGrades + grade;
}

float mean(int nGrades) {
    float actualGrade, sumGrades = 0;
    for (int i = 0; i < nGrades; i++) {
        printf("Quelle note souhaitez-vous entrer? ");
        scanf("%f", &actualGrade);
        sumGrades = addGrade(sumGrades, actualGrade);
    }
    return sumGrades / nGrades;
}