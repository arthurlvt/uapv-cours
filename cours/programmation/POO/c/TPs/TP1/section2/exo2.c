#include <stdio.h>

int square(void) {
    int n;
    printf("Entrez un nombre entier n: ");
    scanf("%d", &n);
    if (n >= 3) {
        // Ligne du Haut
        for (int i = 1; i <= n; i++) {
            printf("*");
        }
        printf("\n");

        // Partie Centrale
        for (int i = 1; i <= n - 2; i++) {
            printf("*");
            for (int j = 1; j <= n - 2; j++) {
                printf(" ");
            }
            printf("*\n");
        }

        // Ligne du bas
        for (int i = 1; i <= n; i++) {
            printf("*");
        }
    }
    return 0;
}