#include <stdio.h>
#include <stdbool.h>

bool compareTo10(int nbr) {
    return nbr > 10;
}

int main()
{
    printf("Donner un nombre entier: ");
    int num;
    scanf("%d", &num);

    if (compareTo10(num))
    {
        printf("Le nombre est supérieur à 10.\n");
    }
    else
    {
        printf("Le nombre n'est pas supérieur à 10.\n");
    }
}