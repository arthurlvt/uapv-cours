// EXERCICE 6 : Conversion de Fahrenheit en Celsius

#include <stdio.h>
int main(void) {
    double temp;
    printf("Entrez la temperature en Fahrenheit: ");
    if (scanf("%lf", &temp) != 1) return 1;
    temp = (temp - 32) * (5.0 / 9.0);
    printf("La temperature est de %.2lf Celsius.\n", temp);
}