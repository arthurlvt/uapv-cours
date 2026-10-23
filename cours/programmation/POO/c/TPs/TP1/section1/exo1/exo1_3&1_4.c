#include <stdio.h>

int main(void) {
    float x, y;
    int choice;
    printf("Entrez 2 flottants x et y: ");
    scanf("%f, %f", x, y);
    printf("Quelle opération souhaitez-vous réaliser? \n(1) Addition \n(2) Soustraction \n(3) Multiplication \n(4) Division \n Votre choix: ");
    scanf("%d", &choice);
    if (choice == 1) {
        printf("%.1f + %.1f = %.1f", x, y, x + y);
    }
    else if (choice == 2) {
        printf("%.1f - %.1f = %.1f", x, y, x - y);
    }
    else if (choice == 3) {
        printf("%.1f * %.1f = %.1f", x, y, x * y);
    }
    else if (choice == 4) {
        if (y != 0) {
            printf("%.1f / %.1f = %.1f", x, y, x / y);
        }
        else {
            printf("Erreur! b doit être différent de 0!");
        }
    }
    else {
        printf("Une erreur s'est produite!");
    }
}
