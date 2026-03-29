#include <stdio.h>
#include "include.h"

void adjustSalary(double *salary1, double *salary2, double *salary3, double bonus) {
    *salary1 += bonus/3;
    *salary2 += bonus/3;
    *salary3 += bonus/3;
}