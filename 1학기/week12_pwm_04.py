import RPi.GPIO as GPIO
import time

# GPIO 핀 번호 정의
TRIG = 23
ECHO = 24
RED_LED = 12  # 빨간색 LED를 GPIO 12번 핀에 연결

# 거리 임계값 (cm) - 최소/최대 밝기 기준
MIN_DIST = 2    # 이 거리 이하로 가까워지면 최대 밝기
MAX_DIST = 30   # 이 거리 이상 멀어지면 최소 밝기

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)
    GPIO.setup(RED_LED, GPIO.OUT)
    GPIO.output(TRIG, False)
    print("초음파센서 및 LED 준비 중 ....")
    time.sleep(2)

def get_distance():
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    pulse_start = time.time()
    time_out = pulse_start + 1
    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()
        if pulse_start > time_out:
            return -1

    pulse_end = time.time()
    time_out = pulse_end + 1
    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()
        if pulse_end > time_out:
            return -1

    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 34300 / 2
    return round(distance, 2)

def map_distance_to_duty(distance):
    # 거리(MIN_DIST~MAX_DIST)를 듀티사이클(100~0)로 선형 매핑
    if distance < MIN_DIST:
        return 100
    elif distance > MAX_DIST:
        return 0
    else:
        duty = 100 - ((distance - MIN_DIST) / (MAX_DIST - MIN_DIST)) * 100
        return duty

def cleanup():
    GPIO.cleanup()
    print("GPIO 자원 회수 완료")

if __name__ == "__main__":
    try:
        setup()
        pwm = GPIO.PWM(RED_LED, 1000)  # 1kHz로 PWM 시작
        pwm.start(0)  # 처음엔 LED 꺼짐

        while True:
            distance = get_distance()
            if distance == -1:
                print("측정 오류: 신호를 받지 못함")
                pwm.ChangeDutyCycle(0)
            else:
                duty = map_distance_to_duty(distance)
                pwm.ChangeDutyCycle(duty)
                print(f"거리: {distance}cm, LED 밝기: {int(duty)}%")
            time.sleep(0.2)
    except KeyboardInterrupt:
        print("프로그램 종료")
    finally:
        pwm.stop()
        cleanup()
