#include <stdio.h>

int main() {
    int grade[5] = {13, 9, 16, 15, 19};
    printf("Valeur du troisième élement: %d\n", grade[2]);
    grade[3] = 14;
    printf("Tableau après modification: %d, %d, %d, %d, %d\n", grade[0], grade[1], grade[2], grade[3], grade[4]);
}