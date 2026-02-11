#ifndef PP_H
#define PP_H

typedef struct {
    int id;
    int pollutingMeasures[5];
    int sizeOfArray;
} pollutingProject;

typedef struct {
    int id;
    int maxOfProject = 100;
} pollutingProjectAnalizer;

void addMeasure(pollutingProject *pp);
void displayArrayValues(pollutingProject *pp);

#endif