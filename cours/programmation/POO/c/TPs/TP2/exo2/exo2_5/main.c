#include <stdio.h>
#include "include.h"

int main() {
    int n, m;
    printf("Entrez successivement n et m: ");
    if (scanf("%d %d", &n, &m) != 2) {
        printf("Une erreur s'est produite!");
        return -1;
    }
    makeRectangle(n, m);
}