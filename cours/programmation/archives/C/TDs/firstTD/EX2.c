// EXERCICE 2 : Moyenne des carrés de 1 à 15

#include <stdio.h>
int main(void) {
    int somme = 0;
    for (int i = 1; i <= 15; i++) {
        somme += i * i;
    }
    printf("La moyenne des carrés de 1 à 15 est : %.2f\n", somme / 15.0);
}