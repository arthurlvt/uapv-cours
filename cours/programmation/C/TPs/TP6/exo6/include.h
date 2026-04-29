#ifndef EXO6_INCLUDE_H
#define EXO6_INCLUDE_H

typedef struct {
    int *array;
    int sizeOfArray;
} Census;

void addToCensus(Census *census, int value);

#endif