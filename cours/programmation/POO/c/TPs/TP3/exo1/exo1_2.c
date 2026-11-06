#include <stdio.h>

int main() {
    int age = 18;
    int *pAge = &age;
    *pAge = 25;
    printf("Vous avez %d ans", age);
}