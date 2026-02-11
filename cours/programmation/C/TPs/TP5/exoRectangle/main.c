#include "rectangle.h"

rectangle defineRectangle(int height, int width) {
    rectangle Rectangle;
    Rectangle.width = width;
    Rectangle.height = height;
    return Rectangle;
}

int main() {
    rectangle MyRectangle = defineRectangle(12, 15);
    int areaValue = getAreaValue(&MyRectangle);
    double diagLenght = getDiagonale(&MyRectangle);
    printf("Value of the area: %d m2, Diagonale : %2.lfcms", areaValue, diagLenght);
}