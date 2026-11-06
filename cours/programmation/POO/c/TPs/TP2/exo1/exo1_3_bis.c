#include <stdio.h>
#include <stdbool.h>

bool compareToX(int nbr, int nbrCompared) {
    return nbr > nbrCompared;
}

int main()
{
    int nbrToCompare;
    int nbrCompared;
    printf("Donner un nombre entier à comparer: ");
    scanf("%d", &nbrToCompare);
    printf("Donnez le nombre entier comparé: ");
    scanf("%d", &nbrCompared);

    if (compareToX(nbrToCompare, nbrCompared))
    {
        printf("Le nombre est supérieur à %d.\n", nbrCompared);
    }
    else
    {
        printf("Le nombre n'est pas supérieur à %d.\n", nbrCompared);
    }
}