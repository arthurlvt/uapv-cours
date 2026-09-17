#include <stdio.h>
#include "include.h"

int main() {
    int grade[5] = {13, 9, 16, 15, 19};
    printf("Valeur du troisième élement: %d\n", grade[2]);
    grade[3] = 14;
    displayArray(grade, 5);
}