#include <stdio.h>

int main(void) { 
    int n;
    int sum;
    printf("Entrez un entier n: ");
    scanf("%d", &n);
    for (int i = 1; i <= n; i++) { 
        sum += i; 
    } 
    printf("La somme des entiers de 1 à %d vaut %d", n, sum);
}