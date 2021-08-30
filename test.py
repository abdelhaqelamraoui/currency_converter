import tkinter as tk
from converter import *
from tkinter import ttk


window = tk.Tk() # main window object
window.title("test")

choices = ["one", "twso"]
n = tk.StringVar()
cb = ttk.Combobox(window, values=choices)
cb.grid(row=0, column=0)
print(cb.get())

window.mainloop()