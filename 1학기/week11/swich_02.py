import RPi.GPIO as GPIO
import time

BUTTON_PIN = 17
red_led = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN)
GPIO.setup(red_led, GPIO.OUT)

try:
    while True:
        state = GPIO.input(BUTTON_PIN)
        print(f"스위치 상태  : {state}")
        time.sleep(0.1)
        if state == 0 :
            GPIO.output(red_led, 1)
        else:
            GPIO.output(red_led, 0)
        time.sleep(0.1)
        
except KeyboardInterrupt:
    print("프로그램 종료")
finally:
    GPIO.cleanup()