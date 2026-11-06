// Ex 2.1 Increment age via function
#include <stdio.h>
#include "include.h"

int main() {
    int age;
    int *pAge = &age;
    printf("Bjr, quel age as tu ? ");
    scanf("%d", &age);
    addOne(age, *pAge);
    printf("Tu as %d ans. Dans un an, tu auras donc %d ans\n", age, *pAge + 1);
}