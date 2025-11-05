from gpiozero import LED
# import time
from time import sleep

red_led =LED(17)
green_led =LED(27)

try:
    while True:
        red_led.on()
        green_led.off()
        sleep(2)
        red_led.off()
        green_led.on()
        sleep(2)
except KeyboardInterrupt:
    print("Exit Program!")
finally:
    red_led.close()
    green_led.close()
