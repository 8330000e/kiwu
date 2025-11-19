from gpiozero import LED
import threading
import time

led = LED(17)

# LED 깜빡이는 함수
def blink_led():
    print("LED 깜빡임 시작")
    for i in range(10):
        led.on()
        time.sleep(0.3)
        led.off()
        time.sleep(0.3)
    print("LED 깜빡임 종료")

# 숫자 세는 함수
def count_numbers():
    print("카운팅 시작")
    for i in range(1, 11):
        print(f"카운트: {i}")
        time.sleep(0.5)
    print("카운팅 종료")

# 스레드 없이 실행 - 순차적
print("=== 순차 실행 ===")
start = time.time()
blink_led()
count_numbers()
print(f"소요시간: {time.time() - start:.1f}초\n")

# 스레드로 동시 실행
print("=== 동시 실행 (스레드 사용) ===")
start = time.time()

thread1 = threading.Thread(target=blink_led)
thread2 = threading.Thread(target=count_numbers)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(f"소요시간: {time.time() - start:.1f}초")

led.close()