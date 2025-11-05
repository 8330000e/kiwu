import tkinter as tk

win = tk.Tk()
win.title("GUI")
win.geometry("400x200")
win.resizable(False, False)

btn_test = tk.Button(win, text="IoT GUI 실습 중...")
btn_test.pack()

win.mainloop()