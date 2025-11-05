from gpiozero import PWMLED
from time import sleep
led1 = PWMLED(12)
led2 = PWMLED(13)
try:
    while True:
        for value in range(0,101):
            led1.value = value / 100
            led2.value = 1 - (value /100)
            sleep(0.02)
        for value in range(100, -1, -1):
            led1.value = value / 100
            led2.value = 1 - (value / 100)
            sleep(0.02)
except keboardInterrupt:
    print("Exit program!")