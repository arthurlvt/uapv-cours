#include <stdio.h>
#include "pp.h"

void addMeasure(pollutingProject *pp) {
    for (int i = 0; i < pp->sizeOfArray; i++) {
        pp->pollutingMeasures[i] = -1;
    }
    for(int i = 0; i < pp->sizeOfArray; i++) {
        if (pp->pollutingMeasures[i] == -1) { 
            printf("Entrez la valeur de la case n°%d", i);
            scanf("%d", &pp->pollutingMeasures[i]);
        }
    }

}
void displayArrayValues(pollutingProject *pp) {
    printf("Valeurs mesurées (en tonnes) de rejet dans l'air pour le projet: ");
    for (int i = 0; i < pp->sizeOfArray ; i++ ) {
        printf("%d", pp->pollutingMeasures[i]);  
    }   
}

int meanOfMeasure(pollutingProject *pp) {
    int sum = 0;
    double mean;
    if (mean1 == 0 || mean2 == 0) {
        printf("Il n'y a aucune mesures");
        mean = 0;
    }
    for (int i = 0; i < pp->sizeOfArray; i++) {
        sum += pp->pollutingMeasures[i];
    }
    mean = (double)sum / pp->sizeOfArray;
    return mean;
}

void worseThan(pollutingProjet *pp, int mean1, int mean2) {
    if (mean1 > mean2) {
        printf("Le projet %d est plus polluant que le projet comparé.\n", pp->id);
    } else {
        printf("Le projet %d est moins polluant que le projet comparé.\n", pp->id);
    }
    if (mean1 == mean2) {
        printf("Les deux projets ont le même niveau de pollution.\n");
    } 
}

void addNewProject(pollutingProjectAnalizer *ppAnalizer, pollutingProject *pp) {
    if (pp->id < ppAnalizer->maxOfProject) {
        pp->id += 1;
    } else {
        pp->id = -1; // Indicate that no more projects can be added
    }
    addMeasure(pp);
    displayArrayValues(pp);
}
