#include <stdio.h>
#include "include.h"

int main() {
    int table1[3] = {1, 2, 3};
    double table2[6] = {1.5, 2.8, 0.7};
    int table3[5];
    int table4[3];

    printf("Table 2 d'éléments:\n");
    displayArrayForDouble(table2, 6, 2);
    table2[5] = 12.92;
    printf("Après modification, la table2 d'élements ressemble à ça:\n");
    displayArrayForDouble(table2, 6, 2);

    printf("Table 3 d'éléments (non initialisée):\n");
    displayArray(table3, 5, 3);
    table3[0] = 9;
    table3[1] = 4;
    table3[2] = 6;
    table3[3] = 8;
    table3[4] = 3;

    printf("Pour le tableau 4, veuillez entrer 3 entiers:\n");
    for (int i = 0; i < 3; i++) {
        printf("Entier %d: ", i + 1);
        scanf("%d", &table4[i]);
    }
    displayArray(table4, 3, 4);
    // printf("table4[%d] = %d, %d, %d\n", 4, table4[0], table4[1], table4[2]);

}