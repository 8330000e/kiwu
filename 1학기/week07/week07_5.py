import RPi.GPIO as GPIO
# import time
from time import sleep

red_led = 18
green_led = 6

GPIO.setmode(GPIO.BCM)
GPIO.setup(red_led, GPIO.OUT)
GPIO.setup(green_led, GPIO.OUT)

try:
    while True:
        GPIO.output(red_led, 1)
        GPIO.output(green_led, 0)
        sleep(2)
        GPIO.output(red_led, 0)
        GPIO.output(green_led, 1)
        sleep(2)
except KeyboardInterrupt:
    print("Exit Program!")
finally:
    GPIO.cleanup()
