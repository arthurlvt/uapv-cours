#include <stdbool.h>
#include <stdio.h>

#ifndef LAMP_H
#define LAMP_H

typedef struct {
    bool state;
    int color;
    double brightness;
    int nbrCreatedLamps;
} Lamp;
Lamp createLamp(int color, double brightness);
void displayLamp(const Lamp* lamp);
void swapLamp(Lamp* lamp);
void changeLampColor(Lamp* lamp);
void defineBrightness(Lamp* lamp);
void defineLampColorFirstTime(Lamp* lamp);
void createNewLamp(Lamp* lamp);


#endif