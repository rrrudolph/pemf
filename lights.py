from pinmap import Pin
from machine import PWM
from utime import sleep

light = PWM(Pin.D3)
min_brightness = 10000
max_brightness = 65025

class Light:
    def on():
        print('lights on')
        for i in range(min_brightness, max_brightness):
            light.duty(i) # duty for D1 mini, duty_u16 for pico
            sleep(0.015)

    def off():
        light.duty(0)

