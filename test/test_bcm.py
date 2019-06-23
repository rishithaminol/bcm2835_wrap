#!/usr/bin/env python

import bcm2835_wrap
import time

print(dir(bcm2835_wrap))

try:
    bcm2835_wrap.py_init_pwm_on_pin()

    direction = 1
    data = 1

    while (True):
        if data == 1:
            direction = 1
        elif data == (1024 -1):
            direction = -1
        
        data += direction
        print("data:", data)
        bcm2835_wrap.py_motor_tune(data)
        time.sleep(0.001)

except KeyboardInterrupt as e:
    bcm2835_wrap.py_stop()
