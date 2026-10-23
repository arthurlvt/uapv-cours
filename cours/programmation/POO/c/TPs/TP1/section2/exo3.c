#include <stdio.h>

int main(void) {
    float a, b, result;
    int choice1, choice2, modeOpp;
    printf("Que souhaitez-vous faire ? \n(0) Menu \n(1) Réaliser une oppération \n Votre choix: ");
    scanf("%d", &choice1);
    while (choice1 != 0) {
        printf("Entrez 2 oppérandes a et b");
        scanf("%lf %lf", a, b);
        printf("Entrez un mode d'oppération: \n(1) Réaliser a + b \n(2) Réaliser a - b \n(3) Réaliser a * b \n(4) Réaliser a / b \nVotre choix: ");
        scanf("%d", modeOpp);
        if (modeOpp == 1) {
            printf("%lf + %lf = %lf", a, b, a + b);
        }
        else if (modeOpp == 2) {
            printf("%lf - %lf = %lf", a, b, a - b);
        }
        else if (modeOpp == 3) {
            printf("%lf * %lf = %lf", a, b, a * b);
        }
        else if (modeOpp == 4) {
            if (b == 0) {
                printf("Erreur! Ici b vaut 0 or la division par 0 est impossible");
                while (b == 0) {
                    printf("Entrez une nouvelle valeur pour b: ");
                    scanf("%lf", &b);
                }
            }
            printf("%lf - %lf = %lf", a, b, a / b);
        }
        else {
            printf("Erreur! Vous avez saisie un mauvais choix pour le mode d'opération!");
        }
    }
    printf("Que souhaitez-vous faire? \n(1) Changer les valeurs a et b \n(2) Quitter");
    scanf("%d", choice2);
    if (choice2 == 1) {
        choice1 = 1;
    }
    else {
        return 0;
    }
}