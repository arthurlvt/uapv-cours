#include "matrices.h"
#include <stdio.h>

Matrix createMatrices(int height, int width) {
    Matrix matrices;
    matrices.height = height; 
    matrices.width = width;
    return matrices;
}

int main() {
    Matrix matrices = createMatrices(3, 3);
    
    printf("--- Remplissage de la Matrice Originale ---\n");
    fillMatrix(&matrices);
    
    printf("\n--- Matrice Originale ---\n");
    display(&matrices);
    int value = diagSum(&matrices);
    int success = transpose(&matrices);
   
    printf("\n--- Matrice Transposée (même structure) ---\n");
    display(&matrices);
    printf("\nSomme de la diagonale : %d\n", value);
    printf("Transposition (Code de retour) : %d (0 signifie succès)\n", success);
}