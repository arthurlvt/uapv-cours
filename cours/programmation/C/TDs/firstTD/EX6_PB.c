// EXERCICE 6 - PARTIE B : Suite de Fibonacci

#include <stdio.h>
int main(void) {
    int secondtolast = 0;
    int last = 1;
    int fibo;
    for (int i = 1; i <= 18; i++) {
        fibo = last + secondtolast;
        secondtolast = last;
        last = fibo;
        printf("%d", last);
        if (i < 18) printf(", ");
    }
    printf("\n");
}