import RPi.GPIO as GPIO

red_led = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(red_led, GPIO.OUT)

try:
    while True:
        num = int(input("1) LED ON 2) LED OFF 0) QUIT : "))
        if num == 1:
            GPIO.output(red_led, 1)
        elif num == 2:
            GPIO.output(red_led, 0)
        else:        
            break
except KeyboardInterrupt:
    print("Exit Program!")
finally:
    GPIO.cleanup()

