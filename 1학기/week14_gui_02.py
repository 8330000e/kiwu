import tkinter as tk
from gpiozero import LED

led = LED(16)

led_on = False

def get_input_value():
    num = en_input.get()
    if num == "1":
        led.on()
        lbl_display.config(text='LED ON')
    elif num == "0":
        led.off()
        lbl_display.config(text='LED OFF')
    else:
        lbl_display.config(text='0 또는 1을 입력하세요')


win = tk.Tk()
win.title("GUI")
win.geometry("400x200")

en_input = tk.Entry(win, width=15)
btn_click = tk.Button(win, text='Click', width=15, command=get_input_value)
lbl_display = tk.Label(win, text='Display', width=30)

#layout (grid :행열)
lbl_display.grid(row=0, column=0, columnspan=2)
en_input.grid(row=1, column=0)
btn_click.grid(row=1, column=1)

win.mainloop()

