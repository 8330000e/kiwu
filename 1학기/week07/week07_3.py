from gpiozero import LED
# import time
from time import sleep

led =LED(17)

try:
    while True:
        led.on()
        sleep(2)
        led.off()
        sleep(2)
except KeyboardInterrupt:
    print("Exit Program!")
finally:
    led.close()
