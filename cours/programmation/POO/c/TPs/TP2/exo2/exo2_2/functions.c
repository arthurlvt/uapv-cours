#include <stdio.h>

int max(int nbr1, int nbr2) {
    int max;
    if (nbr1 == nbr2) {
        return 0;
    }
    if (nbr1 > nbr2) {
        return nbr1;
    }
    else {
        return nbr2;
    }
}

int max3(int nbr1, int nbr2, int nbr3) {
    int max1 = max(nbr1, nbr2);
    int globalMax = max(max1, nbr3);
    return globalMax;
}