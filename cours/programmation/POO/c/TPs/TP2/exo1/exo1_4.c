#include <stdio.h>

int addOne(int nbr)
{
    return nbr + 1;
}

int main()
{
    printf("Donner un nombre entier: ");
    int nbr;
    scanf("%d", &nbr);
    printf("%d\n", addOne(nbr));
    return 0;
}