/* (ALMOST) COMPLETE CALCULATOR */
#include <stdio.h>
int main(void) {
    int a, b, operator, mode;
    printf("Choose mode (1: calculate, 2: quit): ");
    scanf("%d", &mode);

    while (mode != 2) {
        printf("Enter an operator (1: addition, 2: subtraction, 3: multiplication, 4: division, menu: 0): ");
        scanf("%d", &operator);

        if (!(operator == 0 || operator == 1 || operator == 2 || operator == 3 || operator == 4)) {
            printf("Error\n");
        } else {
            if (operator == 1) {
                printf("Enter two integer values: ");
                scanf("%d %d", &a, &b);
                printf("The sum of %d and %d is equal to: %d\n", a, b, a + b);
            } else if (operator == 2) {
                printf("Enter two integer values: ");
                scanf("%d %d", &a, &b);
                printf("The difference of %d and %d is equal to: %d\n", a, b, a - b);
            } else if (operator == 3) {
                printf("Enter two integer values: ");
                scanf("%d %d", &a, &b);
                printf("The product of %d and %d is equal to: %d\n", a, b, a * b);
            } else if (operator == 4) {
                printf("Enter two integer values: ");
                scanf("%d %d", &a, &b);
                if (b != 0) {
                    printf("The quotient of %d divided by %d is: %d\n", a, b, a / b);
                } else {
                    printf("Error! You cannot divide by 0!\n");
                }
            } else if (operator == 0) {
                printf("Returning to main menu.\n");
                break;
            } else {
                printf("Invalid operator!\n");
            }
        }
    }
    printf("Goodbye!\n");
}
