import tkinter as tk
import RPi.GPIO as GPIO
from time import sleep

led = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)
pwm = GPIO.PWM(led, 1000)
pwm.start(0)

def get_input_value():
    dc = int(en_input.get())
    if 0 < dc < 101:
            pwm.ChangeDutyCycle(dc)
            lbl_display.config(text=f'현재 LED 밝기: {dc}')
    else:
        lbl_display.config(text='1에서 100사이의 값을 입력하세요')
        
def on_exit():
    pwm.stop()
    GPIO.output(led, GPIO.LOW)
    GPIO.cleanup()
    win.destroy()

win = tk.Tk()
win.title("GUI")
win.geometry("400x200")

en_input = tk.Entry(win, width=15)
btn_click = tk.Button(win, text='Click', width=15, command=get_input_value)
lbl_display = tk.Label(win, text='Display', width=30)
btn_exit = tk.Button(win, text='Exit', width=15, command=on_exit)

#layout (grid :행열)
lbl_display.grid(row=0, column=0, columnspan=2)
en_input.grid(row=1, column=0)
btn_click.grid(row=1, column=1)
btn_exit.grid(row=2, column=0, columnspan=2, sticky="EW")

win.mainloop()


