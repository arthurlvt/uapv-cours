#include "modify.h"

void modify(float *number) {
    if (*number > 0) { 
        *number = *number / 2; 
    }
    else if (*number < 0) {
        *number = *number * 3;
    }
}
