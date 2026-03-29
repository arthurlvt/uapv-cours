#include <stdio.h>

int main() {
    int grade[5] = {13, 9, 16, 15, 19};
    printf("Valeur du troisième élement: %d\n", grade[2]);
    grade[3] = 14;
    printf("Tableau après modification (boucle): ");
    for(int i = 0; i < 5; i++) {
        printf("%d ", grade[i]);
    }
    printf("\n");
}