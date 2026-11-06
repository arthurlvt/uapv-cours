#include <stdio.h>
#include "modify.h" // <-- L'erreur venait de l'absence de cette ligne

int main(void) {
    float number;
    float *pNumber = &number;
    
    printf("Veuillez entrer une valeur: ");
    if (scanf("%f", &number) != 1) {
        printf("Erreur de saisie.\n");
        return 1;
    }
    
    modify(pNumber);
    printf("valeur finale: %.2f\n", number);
    
    return 0;
}
