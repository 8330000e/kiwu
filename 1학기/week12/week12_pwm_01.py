import RPi.GPIO as GPIO
import time

LED_PIN = 18 #board11
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT) # set output

pwm  = GPIO.PWM(LED_PIN, 1000) # 주파수설정 1kHz == 1000Hz, pwm 객체 생성
pwm.start(0)  #Duty cycle 0%로 할당

try:
    while True:
        for dc in range(0, 101, 5):
            pwm.ChangeDutyCycle(dc)
            time.sleep(0.05)
        for dc in range(100, -1, -5):
            pwm.ChangeDutyCycle(dc)
            time.sleep(0.05)
except KeyboardInterrupt:
    print("Exit Program!")
finally:
    pwm.stop()
    GPIO.cleanup() # initialize gpio setting
