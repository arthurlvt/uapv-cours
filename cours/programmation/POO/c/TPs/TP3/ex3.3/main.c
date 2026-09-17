#include <stdio.h>
#include <stdbool.h>
#include "include.h"

int main() {
    int a, b;
    bool val1, val2;
    bool *pVal1 = &val1;
    bool *pVal2 = &val2;
    bool resultOR = false, resultAND = false, resultXOR = false;
    bool *pResultOR = &resultOR;
    bool *pResultAND = &resultAND;
    bool *pResultXOR = &resultXOR;

    printf("Enter first boolean value (0 or 1): ");
    scanf("%d", &a);
    printf("Enter second boolean value (0 or 1): ");
    scanf("%d", &b);

    val1 = (bool)a;
    val2 = (bool)b;

    logicOperation(pVal1, pVal2, &resultOR, &resultAND, &resultXOR);
    
    printf("Result of OR operation: %d\n", *pResultOR);
    printf("Result of AND operation: %d\n", *pResultAND);
    printf("Result of XOR operation: %d\n", *pResultXOR);
}
