// EXERCICE 2.4: Salary adjustment with pointers
#include <stdio.h>
#include "include.h"

void adjustSalary(double *salary1, double *salary2, double *salary3, double bonus) {
    *salary1 += bonus/3;
    *salary2 += bonus/3;
    *salary3 += bonus/3;
}

int main() {
    double salary1, salary2, salary3, bonus;
    double *pSalary1 = &salary1;
    double *pSalary2 = &salary2;
    double *pSalary3 = &salary3;
    double *pBonus = &bonus;
    printf("Enter the salaries of three employees:\n");
    scanf("%lf %lf %lf", &salary1, &salary2, &salary3);
    printf("Enter the total bonus amount to be distributed:\n");
    scanf("%lf", &bonus);
    adjustSalary(&salary1, &salary2, &salary3, bonus);

    printf("Salaries after adjustment:\n");
    printf("Person 1: %.2f\n", *pSalary1);
    printf("Person 2: %.2f\n", *pSalary2);
    printf("Person 3: %.2f\n", *pSalary3);
}

