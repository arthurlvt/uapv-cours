/* n VALUES IN * */
#include <stdio.h>
int main(void) {
    int n;
    printf("Enter an integer value n: ");
    scanf("%d", &n);
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= i; j++) {
            printf("*");
        }
        printf("\n");
    }
}

/* SQUARE OF n VALUES IN * */
#include <stdio.h>
int main(void) {
    int n;
    printf("Enter an integer value n: ");
    scanf("%d", &n);
    if (n >= 3) {
        // Top border
        for (int i = 1; i <= n; i++) {
            printf("*");
        }
        printf("\n");

        // Middle part
        for (int i = 1; i <= n - 2; i++) {
            printf("*");
            for (int j = 1; j <= n - 2; j++) {
                printf(" ");
            }
            printf("*\n");
        }

        // Bottom border
        for (int i = 1; i <= n; i++) {
            printf("*");
        }
    }
}
