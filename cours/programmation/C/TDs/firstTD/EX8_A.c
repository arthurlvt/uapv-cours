// EXERCICE 8 - PARTIE Arthur : JUSTE PRIX

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int main(void) {
    srand((unsigned)time(NULL));
    int randNum = rand() % 10 + 1;
    int valuser = 0;
    int counter_tries = 0;
    while (valuser != randNum) {
        printf("Veuillez entrer un nombre entre 1 et 10: ");
        if (scanf("%d", &valuser) != 1) return 1;
        counter_tries++;
        if (valuser < randNum) {
            printf("C'est plus!\n");
        } else if (valuser > randNum) {
            printf("C'est moins!\n");
        } else {
            printf("Bravo! Vous avez trouve le nombre %d en %d essais!\n", randNum, counter_tries);
        }
    }
    return 0;
}