/* GUESS THE NUMBER (BINGO!) - FIRST WAY */
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int main(void) {
    srand(time(0));  // Initialize random number generator
    int mysteryNumber = rand() % 100 + 1;  // Number between 1 and 100
    int n = 0, count = 0;

    while (n != mysteryNumber) {
        printf("Guess the number (between 1 and 100): ");
        scanf("%d", &n);
        count++;

        if (n < mysteryNumber) {
            printf("Higher!\n");
        } else if (n > mysteryNumber) {
            printf("Lower!\n");
        } else {
            printf("Congratulations! You found the number in %d attempts.\n", count);
        }
    }
}

/* GUESS THE NUMBER (BINGO!) - SECOND WAY */
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    srand((unsigned)time(NULL));
    int randNum = rand() % 10 + 1;
    int valuser = 0;
    int counter_tries = 0;
    while (valuser != randNum) {
        printf("Please enter an int between 1 and 9: ");
        if (scanf("%d", &valuser) != 1) return 1;
        counter_tries++;
        if (valuser < randNum) {
            printf("My number is bigger!!\n");
        } else if (valuser > randNum) {
            printf("My number is smaller!\n");
        } else {
            printf("Congrats! You found %d by %d tries!\n", randNum, counter_tries);
        }
    }
}
