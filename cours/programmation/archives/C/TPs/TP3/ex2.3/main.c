// Ex 2.3 Modify a value with a function using pointers
#include <stdio.h>
#include <stdbool.h>
#include "include.h"

int main() {
    int value;
    int *valuePtr = &value;
    printf("Enter an integer value: ");
    scanf("%d", valuePtr);
    int modifiedValue = modifyValue(*valuePtr);
    if (isPositive(modifiedValue)) {
        printf("The modified value is %d and is positive.\n", modifiedValue);
    } else {
        printf("The modified value is %d and is negative.\n", modifiedValue);
    }
}