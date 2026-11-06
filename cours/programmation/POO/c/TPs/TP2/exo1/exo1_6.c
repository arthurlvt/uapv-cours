#include <stdio.h>

int sum(int a, int b) {
    return a + b;
}

int main(void) {
    int a, b;

    printf("Entrez deux entiers : ");
    if (scanf("%d %d", &a, &b) != 2) {
        printf("Saisie invalide.\n");
        return 1;
    }
    printf("Somme : %d\n", sum(a, b));
    return 0;
}

