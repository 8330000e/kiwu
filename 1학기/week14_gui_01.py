import tkinter as tk

def get_input_value():
    lbl_display.config(text=en_input.get())


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

# import tkinter as tk
# 
# win = tk.Tk()
# win.title("GUI")
# win.geometry("400x200")
# 
# en_input = tk.Entry(win)
# btn_click = tk.Button(win, text='Click')
# lbl_display = tk.Label(win, text='Display')
# 
# lbl_display.pack()
# en_input.pack()
# btn_click.pack()
# 
# win.mainloop()