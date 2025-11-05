import RPi.GPIO as GPIO
import time

BUTTON_PIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN)

try:
    while True:
        state = GPIO.input(BUTTON_PIN)
        print(f"스위치 상태  : {state}")
        time.sleep(0.5)
except KeyboardInterrupt:
    print("프로그램 종료")
finally:
    GPIO.cleanup()