#include <stdbool.h>
#include "include.h"
#include <stdio.h>

int modifyValue(int value) {
    if (value >= 0) {
        value = value/2;
    } else {
        value = value*3;
    }
    return value;
}

bool isPositive(int value) {
    if (value >= 0) {
        return true;
    } else {
        return false;
    }
}