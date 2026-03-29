/* EXERCICE 8 - PARTIE B: TRIE DE VALEURS A, B, C */

#include <stdio.h> 
int main(void) {
    int a, b, c;
    printf("Entrez trois valeurs entières (A, B, C): ");
    scanf("%d %d %d", &a, &b, &c);
    if (a > b) {
        if (a > c) {
            printf("L'ordre décroissant est: %d, %d, %d\n", a, b > c ? b : c, b > c ? c : b);
        } else {
            printf("L'ordre décroissant est: %d, %d, %d\n", c, a, b);
        }
    } else {
        if (b > c) {
            printf("L'ordre décroissant est: %d, %d, %d\n", b, a > c ? a : c, a > c ? c : a);
        } else {
            printf("L'ordre décroissant est: %d, %d, %d\n", c, b, a);
        }
    }
}