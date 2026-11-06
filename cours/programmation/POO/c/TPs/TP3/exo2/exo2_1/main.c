#include <stdio.h>
#include "includes.h"

int main()
{
    int age;
    int *pAge = &age;
    printf("Quel âge avez vous : ");
    scanf("%d", &age);
    addOne(pAge);
    printf("Votre âge l'an prochain : %d.\n", age);
}