from tkinter import *
from tkinter.ttk import *

from time import strftime
def time():
    str = strftime("%H:%M:%S %p")
    label.config(text=str)
    label.after(1000, time)

ms = Tk()
ms.title("Digital Clock")

label = Label(ms, font=("ds-digital",200), background = "aqua" , foreground = "white")
label.pack(anchor = "center")
time()
mainloop()
