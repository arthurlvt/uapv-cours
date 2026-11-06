#include <stdio.h>

int factorielle(int nbr) {
    if (nbr == 0) {
        return 1;
    }
    else {
        return nbr * factorielle(nbr-1);
    }
}

int main() {
    int nbrToFacto;
    printf("Entrez un nombre pour lequel vous souhaitez obtenir la factorielle: ");
    scanf("%d", &nbrToFacto);
    printf("%d! = %d", nbrToFacto, factorielle(nbrToFacto));
}