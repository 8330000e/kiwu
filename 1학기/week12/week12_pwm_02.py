import RPi.GPIO as GPIO
from time import sleep

LED1 = 12
LED2 = 13
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(LED2, GPIO.OUT)
pwm1 = GPIO.PWM(LED1, 1000)
pwm2 = GPIO.PWM(LED2, 1000)
pwm1.start(0) # 0% Duty Cycle
pwm2.start(0)

try:
    while True:
        for dc in range(0, 101, 1):
            pwm1.ChangeDutyCycle(dc)
            pwm2.ChangeDutyCycle(100-dc)
            sleep(0.02)
        for dc in range(100, -1, -1):
            pwm1.ChangeDutyCycle(dc)
            pwm2.ChangeDutyCycle(100-dc)
            sleep(0.02)
except KeyboardInterrupt:
    print("Exit Program!")
finally:
    pwm1.stop()
    pwm2.stop()
    GPIO.cleanup() # initialize gpio setting

