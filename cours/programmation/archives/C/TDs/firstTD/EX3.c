#include <stdio.h>
int main(void) {
    int compteur1 = 0;
    int compteur2 = 0;
    for (int i = 1; i <= 10; i++) {
        if (i <= 5) compteur1++;
        else compteur2++;
    }
    printf("Compteur1: %d, Compteur2: %d\n", compteur1, compteur2);
}