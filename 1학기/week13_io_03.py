from tkinter import *
from gpiozero import LED

# LED 핀 번호 설정 (예: BCM 18번)
led = LED(18)

# tkinter 윈도우 생성
win = Tk()
win.title("LED 제어 GUI")
win.geometry("300x150")

# LED 상태를 저장할 변수
led_on = False

def toggle_led():
    global led_on
    if led_on:
        led.off()
        led_button.config(text="LED ON")
        led_on = False
    else:
        led.on()
        led_button.config(text="LED OFF")
        led_on = True

def on_exit():
    led.off()
    win.destroy()

# LED 제어 버튼
led_button = Button(win, text="LED ON", command=toggle_led, height=2, width=10)
led_button.pack(pady=20)

# 종료 버튼
exit_button = Button(win, text="Exit", command=on_exit, height=2, width=10)
exit_button.pack()

win.mainloop()
