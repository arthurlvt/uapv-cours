#include <stdio.h>

int main(void) {
    int n;
    printf("Saisissez un entier: ");
    scanf("%d", n);
    if (n > 10) {
        printf("%d est plus grand que 10", n);
    }
    else {
        printf("%d n'est pas plus grand que 10", n);
    }
}
