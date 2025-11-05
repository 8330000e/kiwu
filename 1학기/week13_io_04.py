import tkinter as tk
import RPi.GPIO as GPIO

red_led = 18
led = False

GPIO.setmode(GPIO.BCM)
GPIO.setup(red_led, GPIO.OUT)

def led_on_off():
    #print("LED 켜짐")
    global led
    if led:
        lbl_display.config(text="LED 꺼짐")
        led = False
        GPIO.output(red_led, 0)
    else:
        lbl_display.config(text="LED 켜짐")
        led = True
        GPIO.output(red_led, 1)
    
#def led_off():
#    lbl_display.config(text="LED 꺼짐")

win = tk.Tk() # 윈도우 객체 생성
win.title("GUI")
win.geometry("400x200")

btn_led_on_off = tk.Button(win, text="LED ON/OFF", command=led_on_off) # 버튼 객체 생성
#btn_led_off = tk.Button(win, text="LED OFF", command=led_off)
lbl_display = tk.Label(win, text="LED DISPLAY") # 라벨 객체 생성

lbl_display.pack()
btn_led_on_off.pack(fill='x')
#btn_led_off.pack(fill='x')

win.mainloop()