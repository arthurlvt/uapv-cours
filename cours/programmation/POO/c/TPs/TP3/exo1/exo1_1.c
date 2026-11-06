#include <stdio.h>

int main() {
    int age = 3;
    int *pAge = &age;
    printf("Vous avez %d ans et %d ans", age, *pAge);
}