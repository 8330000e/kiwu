import RPi.GPIO as GPIO
import time

LED_PIN = 17 #board11
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT) # set output

while True:
    GPIO.output(LED_PIN, GPIO.HIGH)
    time.sleep(2) # delay 2sec
    GPIO.output(LED_PIN, GPIO.LOW)
    time.sleep(2) # delay 2sec
    
GPIO.cleanUp() # initialize gpio setting