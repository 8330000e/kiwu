from gpiozero import LED

led = LED(18)

while True:
    try:
        cmd = input("1 LED ON, 2 LED OFF, 0 QUIT: ")
        if cmd == '1':
            led.on()
            print("LED ON")
        elif cmd == '2':
            led.off()
            print("LED OFF")
        elif cmd == '0':
            print("프로그램 종료")
            break
        else:
            print("잘못된 입력입니다. 1, 2, 0 중 하나를 입력하세요.")
    except KeyboardInterrupt:
        print("\n프로그램 강제 종료")
        break
    except Exception as e:
        print(f"예외 발생: {e}")

