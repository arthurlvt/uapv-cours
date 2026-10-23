#include <stdio.h>

void display(num)
{
    printf("%d\n", num);
}

int main()
{
    printf("Donner un nombre entier: ");
    int num;
    scanf("%d", &num);
    display(num);
}