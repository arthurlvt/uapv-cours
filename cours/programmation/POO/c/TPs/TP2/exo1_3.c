#include <stdio.h>
#include <stdbool.h>

bool higherThanX(n, x) {
    if (n > x) {
        return 1;
    }
    else {
        return 0;
    }
}

void display(n, x) {
    if (higherThan10(n, x)) {
        printf("Le nombre est supérieur à 10.\n");
    }  
    else {
        printf("Le nombre n'est pas supérieur à 10.\n");
    }
}

int main()
{
    int num;
    int nbrToCompare;
    printf("Donner un nombre entier et la valeur à laquelle le comparer: ");
    scanf("%d, %d", &num, &nbrToCompare);
    display(num);
}