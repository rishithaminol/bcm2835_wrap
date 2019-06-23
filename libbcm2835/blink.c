#include "bcm2835.h"
#include <stdio.h>
#include <time.h>

// Blinks on RPi Plug P1 pin 11 (which is GPIO pin 17)
#define PIN RPI_GPIO_P1_11

int main(int argc, char **argv)
{
    float hp, lp;
    struct timespec wait_ms;

    if (!bcm2835_init())
      return 1;

    // Set the pin to be an output
    bcm2835_gpio_fsel(PIN, BCM2835_GPIO_FSEL_OUTP);

    hp = 1;
    lp = 2 - hp;

    bcm2835_mk_msec(&wait_ms, 1);

    // Blink
    while (1)
    {
        // Turn it on
        bcm2835_gpio_write(PIN, HIGH);
        
        // wait a bit
        nanosleep(&wait_ms, NULL);
        
        // turn it off
        bcm2835_gpio_write(PIN, LOW);
        
        // wait a bit
        nanosleep(&wait_ms, NULL);
    }
    bcm2835_close();
    return 0;
}
