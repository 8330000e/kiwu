import tkinter as tk
import RPi.GPIO as GPIO

LED_PIN = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
led = False

def led_on_off():
    global led
    if led:
        lbl_display.config(text="LED 꺼짐")
        GPIO.output(LED_PIN, GPIO.LOW)
        led = False
    else:
        lbl_display.config(text="LED 켜짐")
        GPIO.output(LED_PIN, 1)
        led = True

win = tk.Tk()
win.title("GUI")
win.geometry("400x200")

btn_on_off = tk.Button(win, text="LED ON/OFF", command=led_on_off)
lbl_display = tk.Label(win, text="LED DISPLAY")

lbl_display.pack()
btn_on_off.pack(fill='x')

win.mainloop()


# import tkinter as tk
#
# led = False
#
# def led_on_off():
#     global led
#     if led:
#         lbl_display.config(text="LED 꺼짐")
#         led = False
#     else:
#         lbl_display.config(text="LED 켜짐")
#         led = True
#
#
# win = tk.Tk()
# win.title("GUI")
# win.geometry("400x200")
#
# btn_on_off = tk.Button(win, text="LED ON/OFF", command=led_on_off)
# lbl_display = tk.Label(win, text="LED DISPLAY")
#
# lbl_display.pack()
# btn_on_off.pack(fill='x')
#
# win.mainloop()


# import tkinter as tk
#
# def led_on():
#     # print("LED 켜짐")
#     lbl_display.config(text="LED 켜짐")
#
# def led_off():
#     lbl_display.config(text="LED 꺼짐")
#
# win = tk.Tk()
# win.title("GUI")
# win.geometry("400x200")
#
# btn_on = tk.Button(win, text="LED ON", command=led_on)
# btn_off = tk.Button(win, text="LED OFF", command=led_off)
# lbl_display = tk.Label(win, text="LED DISPLAY")
#
# lbl_display.pack()
# btn_on.pack(fill='x')
# btn_off.pack(fill='x')
#
# win.mainloop()


# import tkinter as tk
#
# win = tk.Tk()
# win.title("GUI")
# win.geometry("400x200")
# win.resizable(False, False)
#
# btn_test = tk.Button(win, text="IoT GUI 실습 중...")
# btn_test.pack()
#
# win.mainloop()