/* PART 1 - Ex3:  True and False logical assertions */
#include <stdio.h>

int main() {
    int average = 10, grade1 = 6, grade2 = 8, age = 15;

    if (age >= 15 && age < 25) {
        printf("Assertion A true\n");
    } else {
        printf("Assertion A false\n");
    }

    if (age >= 18 || age < 25) {
        printf("Assertion B true\n");
    } else {
        printf("Assertion B false\n");
    }

    if (!(age >= 18) && age < 25) {
        printf("Assertion C true\n");
    } else {
        printf("Assertion C false\n");
    }

    if (average < 10 || grade1 < 7 || grade2 < 7) {
        printf("Assertion D true\n");
    } else {
        printf("Assertion D false\n");
    }

    if ((average < 10 || grade1 < 7) && (average < 10 || grade2 < 7)) {
        printf("Assertion E true\n");
    } else {
        printf("Assertion E false\n");
    }

    if (average < 10 || (grade1 < 7 && grade2 < 7)) {
        printf("Assertion F true\n");
    } else {
        printf("Assertion F false\n");
    }
}


