// Ex 1.1 Age et pointeurs
#include <stdio.h>
#include <stdbool.h>
int main() {
    int age;
    printf("Bjr, quel age as tu ? ");
    scanf("%d", &age);
    printf("Tu as %d ans\n", age);
    printf("La valeur de la variable age est de %d\n", age);
}

// Ex 1.2 Fetching age via pointer
#include <stdio.h>
int main() {
    int age = 18;
    int *pAge = &age;
    printf("Quel age as tu ? ");
    scanf("%d", pAge);
    printf("Tu as %d ans\n", *pAge);
    printf("La valeur de la variable age est de %d\n", age);
}