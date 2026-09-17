#include <math.h>
#include <stdio.h>

#ifndef RECTANGLE_H
#define RECTANGLE_H

typedef struct {
    int height;
    int width;
} rectangle;

rectangle defineRectangle(int height, int width);
int getHeight(rectangle* Rectangle);
int getWidth(rectangle* Rectangle);
int getAreaValue(rectangle* Rectangle);

#endif