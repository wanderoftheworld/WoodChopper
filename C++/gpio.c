#include <stdint.h>

// Define the Gpio_ConfigType structure
typedef struct {
    uint8_t pinNumber;
    Gpio_DirectionType direction;
    // ... other configuration fields
} Gpio_ConfigType;

// Function to configure a single pin
void Gpio_InitPin(uint8_t pinNumber, Gpio_DirectionType direction) {
    // Access hardware registers based on pin number and direction
    // ... (implementation details specific to the microcontroller)
}

// Example usage
Gpio_ConfigType myConfig = {12, GPIO_OUTPUT}; // Configure pin 12 as output
Gpio_Init(&myConfig); // Initialize the pin using the configuration
