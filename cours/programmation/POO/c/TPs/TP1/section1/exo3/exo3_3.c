#include <stdio.h>

int main(void) { 
    // exo 3.3
    int n, result;
    printf("Entrez un entier n pour obtenir sa table: ");
    scanf("%d", &n);
    for (int i = 1; i <= 10; i++) { 
        printf("%d x %d = %d \n", i, n, i * n);
    }
    // exo 3.3 bis
    int saisie, count;
    printf("Entrez une valeur entière (0 pour arreter): ");
    scanf("%d", saisie);
    while (saisie != 0) {
        count += 1;
    }
    printf("Vous avez saisie %d valeur(s)", count);
}