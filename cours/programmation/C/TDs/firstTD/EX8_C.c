// EXERCICE 8: Afficher les diviseurs d'un nombre entier

#include <stdio.h>
int main(void) {
    int n;
    printf("Entrez un nombre entier: ");
    if (scanf("%d", &n) != 1) return 1;
    printf("Les diviseurs de %d sont: ", n);
    for (int i = 1; i <= n; i++) {
        if (n % i == 0) printf("%d ", i);
    }
    printf("\n");
}