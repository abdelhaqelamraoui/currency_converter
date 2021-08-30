

import tkinter as tk
from converter import *
from tkinter import ttk


window = tk.Tk() # main window object
window.title("Currency Converter")

tk.Label(window, text="Amount").grid(row=0)
tk.Label(window, text="From").grid(row=1)
tk.Label(window, text="To").grid(row=2)
tk.Label(window, text="Result").grid(row=3)


amount_w = tk.Entry(window)
result_w = tk.Entry(window)

currencies = all_currencies()
currencies.sort()
var_1 = tk.StringVar()
var_2 = tk.StringVar()
from_combobox = ttk.Combobox(window, values=currencies, textvariable=var_1)
to_combobox = ttk.Combobox(window, values=currencies, textvariable=var_2)


def func():
   amt = int(amount_w.get())
   from_curr = from_combobox.get()
   to_curr = to_combobox.get()
   res = convert(amt, from_curr, to_curr)
   result_w.delete(0, 'end')
   result_w.insert(0, str(res))

button = tk.Button(window, text='Convert', width=10, height=1, command=func)

amount_w.grid(row=0, column=1)

from_combobox.grid(row=1, column=1)
to_combobox.grid(row=2, column=1)
result_w.grid(row=3, column=1)
button.grid(row=4, column=1)

window.mainloop()


