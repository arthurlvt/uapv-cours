#include "lamp.h"

int main() {
    // Create initial lamp
    Lamp myLamp = createLamp(1, 0.5);  // OFF, RED, 50%
    displayLamp(&myLamp);

    int choice = -1;
    swapLamp(&myLamp); // Turn ON the lamp initially
    defineLampColorFirstTime(&myLamp);
    defineBrightness(&myLamp);
    displayLamp(&myLamp);
    while (choice != 0) {
        printf("===== LAMP MENU =====\n");
        printf("1. Swap lamp ON/OFF\n");
        printf("2. Change lamp color\n");
        printf("3. Change brightness\n");
        printf("4. Create a new lamp\n");
        printf("0. Exit\n");
        printf("Choose: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                swapLamp(&myLamp);
                break;

            case 2:
                changeLampColor(&myLamp);
                break;

            case 3:
                defineBrightness(&myLamp);
                break;

            case 4:
                createNewLamp(&myLamp);
                break;

            case 0:
                printf("Goodbye!\n");
                break;

            default:
                printf("Invalid choice.\n");
        }

        displayLamp(&myLamp);
    }

    return 0;
}
