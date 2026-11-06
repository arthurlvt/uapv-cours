// EXERCICE 2.5: MAX AND MIN WITH POINTORS

#include <stdio.h>
#include "include.h"

int main() {
    int minNbr, maxNbr;
    int *pMinNbr = &minNbr;
    int *pMaxNbr = &maxNbr;
    printf("Entrez la valeur minimum ainsi que la valeur maximum");
    scanf("%d %d", &minNbr, &maxNbr);
    if (minNbr < maxNbr) {
        modify(&minNbr, &maxNbr);
        printf("Les nouvelles valeurs sont : min = %d et max = %d\n", *pMinNbr, *pMaxNbr);
    } else {
        printf("Erreur : la valeur minimum doit être inférieure à la valeur maximum.\n");
        printf("Entrez 2 nouvelles valeurs : ");
        scanf("%d %d", &minNbr, &maxNbr);
        modify(&minNbr, &maxNbr);
        if((*pMinNbr) >(*pMaxNbr)) {
            // les valeurs sont donc inversés
            swap(&minNbr, &maxNbr);
            modify(&minNbr, &maxNbr);
            printf("Erreur! Les valeurs sont inversés! L'ordre est donc inversé!\n Les nouvelles valeurs sont : min = %d et max = %d\n", *pMinNbr, *pMaxNbr);
        } else {
            printf("Les nouvelles valeurs sont : min = %d et max = %d\n", *pMinNbr, *pMaxNbr);
        }    
    }   
}