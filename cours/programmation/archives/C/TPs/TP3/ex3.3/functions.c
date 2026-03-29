#include <stdio.h>
#include <stdbool.h>
#include "include.h"

bool logicOperation(bool *val1, bool *val2, bool *resultOR, bool *resultAND, bool *resultXOR) {
    *resultOR = *val1 || *val2;
    *resultAND = *val1 && *val2;
    *resultXOR = *val1 ^ *val2;

    return true;
}