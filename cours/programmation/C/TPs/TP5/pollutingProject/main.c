#include "pp.h"
#include <stdio.h>
#include <stdlib.h>

pollutingProject createPollutingProject(int id) {
    pollutingProject pp;
    pp.id = id;
    pp.sizeOfArray = 5;
    return pp;
}

pollutingProjectAnalizer createPollutingProjectAnalizer(int id) {
    pollutingProjectAnalizer ppAnalizer;
    ppAnalizer.id = id;
    ppAnalizer.maxOfProject = 100;
    return ppAnalizer;
}

int main() {
    // create a new pollutingProject with id = 0 and then add +1 to next project id for each new
    pollutingProject pp = createPollutingProject(0);
    addMeasure(&pp);
    displayArrayValues(&pp);
    int mean = meanOfMeasure(&pp);
    printf("La moyenne des mesures est de : %d\n", mean);

    // to compare with another project
    pollutingProject pp2 = createPollutingProject(1);
    addMeasure(&pp2);
    int mean2 = meanOfMeasure(&pp2);
    worseThan(&pp, mean, mean2);
}

