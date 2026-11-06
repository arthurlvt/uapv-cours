#include <stdio.h>

int main() {
    int age = 0;
    int *pAge = &age;
    printf("Quel âge avez vous? ");
    scanf("%d", pAge);
    printf("Vous avez %d ans", age);
}