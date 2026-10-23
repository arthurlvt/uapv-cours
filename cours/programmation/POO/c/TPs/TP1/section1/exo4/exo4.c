#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int main(void) {
    srand(time(0));
    int mysteryNumber = rand() % 100 + 1;
    int n = 0, count = 0;

    while (n != mysteryNumber) {
        printf("Devinez le nombre mystère (entre 1 et 100): ");
        scanf("%d", &n);
        count++;

        if (n < mysteryNumber) {
            printf("Plus bas!\n");
        } else if (n > mysteryNumber) {
            printf("Plus haut!\n");
        } else {
            printf("Bravo! Vous avez trouvé le nombre en %d tentative(s).\n", count);
        }
    }
}