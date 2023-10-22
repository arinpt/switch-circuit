from machine import Pin, Timer
import time
#Assigning pin values to LEDs
red_led = Pin(1, Pin.OUT)
green_led = Pin(28, Pin.OUT)

#Assigning pin values to Button
button = Pin(5, Pin.IN, Pin.PULL_UP)
#Pin.PULL_UP defines on and off values of button
red_led.value(1)
green_led.value(0)

while True:
    while red_led.value() == 1:  
        if button.value() == 0:
            red_led.value(0)
            green_led.value(1)
            time.sleep(0.2)
            
    while green_led.value() == 1:             
        if button.value() == 0:
            red_led.value(1)
            green_led.value(0)
            time.sleep(0.2)