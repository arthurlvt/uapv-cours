#include <stdio.h>

void makeRectangle(int n, int m) {
    for (int i = 0; i < m; i++) {
        printf("*");
    }
    printf("\n");
    for (int i = 0; i <= n; i++) {
        printf("*");
        for (int j = 3; j <= m; j++ ) {
            printf("^");
        }
        printf("* \n");
    }
    for (int i = 0; i < m; i++) {
        printf("*");
    }
}