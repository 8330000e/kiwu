객체
생성자

from gpiozero(모듈) import LED(클래스)
# import time
from time import sleep

led(객체) = LED(17)
led에 생성자가 들어있음...

try:
    while True:
        led(생성자).on()(LED클래스안에 들어있는 것.)
        sleep(2)
        led.off()
        sleep(2)
except KeyboardInterrupt:
    print("Exit Program!")
finally:
    led.close()

'''
리눅스 데비안 슬랙웨어 수세 레드햇
우리가 vscode 설치했던 명령어는 데비안 계열 리눅스 명령어...apt-get
데비안 출신 우분투가 대표적.. 패키지 관리 도구 APT
아치 리눅스는  apt안먹히고 pacman를 씀
우리는 (구)라즈비안OS (현)라즈베리파이OS...데비안 계열..우분투랑 동일하게 쓸 수 있음

오라클 버추얼박스에다 여러 리눅스 깔아볼 수 있음 스펙좋으면 함해보래
'''





















