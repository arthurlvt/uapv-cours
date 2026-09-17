#include "rectangle.h"

int getHeight(rectangle* Rectangle) {
    return Rectangle->height;
}
int getWidth(rectangle* Rectangle) {
    return Rectangle->width;
}
int getAreaValue(rectangle* Rectangle) {
    int areaValue;
    areaValue = (getHeight(Rectangle)) * (getWidth(Rectangle));
    return areaValue;
}
double getDiagonale(rectangle* Rectangle) {
    double diagonale = sqrt(((getHeight(Rectangle))*(getHeight(Rectangle)))+((getWidth(Rectangle))*(getWidth(Rectangle))));
    return diagonale;
}