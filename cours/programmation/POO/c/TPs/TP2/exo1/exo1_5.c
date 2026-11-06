#include <stdio.h>
#include <stdbool.h>

bool greaterThan(int nbr, int nbrCompared) {
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

    if (greaterThan(nbrToCompare, nbrCompared))
    {
        printf("True");
    }
    else
    {
        printf("False");
    }
}