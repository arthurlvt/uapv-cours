#include <stdio.h>

int main(void) {
    int a, b;
    printf("Saisissez 2 entiers: ");
    scanf("%d, %d", a, b);
    if (a > b) {
        printf("%d > %d", a, b);
    }
    else {
        print("%d > %d", b, a);
    }
}
