/* Temperature Convertissor */
#include <stdio.h>

int main() {
    double temp;
    int mode;
    printf("Welcome to the Temperature Convertissor!\n");
    printf("Choose conversion mode:\n1. Celsius to Fahrenheit\n2. Fahrenheit to Celsius\n");
    if (scanf("%d", &mode) != 1) return 1;
    if (mode == 1) {
        printf("Please enter the temperature in °Celsius: ");
        if (scanf("%lf", &temp) != 1) return 1;
        temp = (temp * (9.0 / 5.0)) + 32;
        printf("It's %.2lf Fahrenheit!.\n", temp);
    } else if (mode == 2) {
        printf("Please enter the temperature in °Fahrenheit: ");
        if (scanf("%lf", &temp) != 1) return 1;
        temp = (temp - 32) * (5.0 / 9.0);
        printf("It's %.2lf Celsius!.\n", temp);
    } else {
        printf("Invalid mode selected.\n");
    }
    return 0;
}