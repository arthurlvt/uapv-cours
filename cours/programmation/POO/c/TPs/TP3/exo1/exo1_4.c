#include <stdio.h>
#include <stdbool.h>

int main() {
    float price = 100.50;
    bool isActive = true;
    printf("-> valeurs initiales respectives de price et isActive: %.2f, %d \n", price, isActive);
    float *pPrice = &price;
    bool *pIsActive = &isActive;
    *pPrice = 150.75;
    *pIsActive = false;
    printf("-> valeurs finales respectives de price et isActive après modification: %.2f, %d \n", price, isActive);
}