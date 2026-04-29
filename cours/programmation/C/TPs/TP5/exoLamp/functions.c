#include <stdio.h>
#include "lamp.h"

// Create lamp
Lamp createLamp(int color, double brightness) {
    Lamp lamp;
    lamp.state = false;
    lamp.color = color;
    lamp.brightness = brightness;
    return lamp;
}

// Swap ON/OFF
void swapLamp(Lamp* lamp) {
    lamp->state = !lamp->state;
    printf("Lamp is now %s.\n", lamp->state ? "ON" : "OFF");
}

// Define lamp color for the first time
void defineLampColorFirstTime(Lamp* lamp) {
    int color;

    printf("Choose a color for the lamp (0 = WHITE, 1 = RED, 2 = BLUE, 3 = GREEN, 4 = PURPLE): ");
    scanf("%d", &color);
    if (color == 3 || color == 4) {
        printf("Error! You cannot start with GREEN or PURPLE.\n");
        printf("Color is now set to WHITE by default.\n");
        lamp->color = 0; // WHITE
    } else {
        lamp->color = color;
    }

    printf("Lamp color set to: %d\n", lamp->color);
}

// Change lamp color
void changeLampColor(Lamp* lamp) {
    int color;

    printf("Choose a new color for the lamp (0 = WHITE, 1 = RED, 2 = BLUE, 3 = GREEN, 4 = PURPLE): ");
    scanf("%d", &color);

    lamp->color = color;
    printf("Lamp color changed to: %d\n", lamp->color);
}

// Set brightness
void defineBrightness(Lamp* lamp) {
    double brightness;
    printf("Set brightness (0 to 1): ");
    scanf("%lf", &brightness);

    lamp->brightness = brightness;
    printf("Brightness set to %.0lf%%.\n", lamp->brightness * 100);
}

// Create a new lamp (reset)
void createNewLamp(Lamp* lamp) {
    *lamp = createLamp(0, 0.5);
    printf("New lamp created (WHITE, 50%% brightness, OFF).\n");
}

// Display lamp properties
void displayLamp(const Lamp* lamp) {
    printf("\n--- LAMP STATUS ---\n");
    printf("State:      %s\n", lamp->state ? "ON" : "OFF");
    printf("Color:      %d\n", lamp->color);
    printf("Brightness: %.0lf%%\n", lamp->brightness * 100);
    printf("---------------------\n\n");
}