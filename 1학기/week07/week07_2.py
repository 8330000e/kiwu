import RPi.GPIO as GPIO
import time

LED_PIN = 17 #board11
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT) # set output

try:
    while True:
        GPIO.output(LED_PIN, GPIO.HIGH)
        #GPIO.output(LED_PIN, 1)
        time.sleep(2) # delay 2sec
        GPIO.output(LED_PIN, GPIO.LOW)
        time.sleep(2) # delay 2sec
except KeyboardInterrupt:
    print("Exit Program!")
finally:
    GPIO.cleanup() # initialize gpio setting