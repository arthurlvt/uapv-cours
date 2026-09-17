/* EXERCICE 2 - PARTIE B : Calcul de la factorielle de 12*/

#include <stdio.h>
int main(void) {
    int factorielle = 1;
    for (int i = 1; i <= 12; i++) {
        factorielle *= i;
    }
    printf("La factorielle de 12 est : %d\n", factorielle);
}