

import tkinter as tk
import converter as ct
from tkinter import ttk


window = tk.Tk() # main window object
window.title("Currency Converter")

amount_label = tk.Label(window, text="Amount")
from_label = tk.Label(window, text="From")
to_label = tk.Label(window, text="To")
result_label = tk.Label(window, text="Result")
status_label = tk.Label(window, text=ct.get_status())


amount_w = tk.Entry(window)
result_w = tk.Entry(window)

currencies = ct.all_currencies()

var_1 = tk.StringVar()
var_2 = tk.StringVar()
from_combobox = ttk.Combobox(window, values=currencies, textvariable=var_1)
to_combobox = ttk.Combobox(window, values=currencies, textvariable=var_2)


def func():
   amt = int(amount_w.get())
   from_curr = from_combobox.get()
   to_curr = to_combobox.get()
   res = ct.convert(amt, from_curr, to_curr)
   result_w.delete(0, 'end')
   result_w.insert(0, str(res))


convert_button = tk.Button(window, text='Convert', width=10, height=1, command=func)


amount_label.grid(row=0)
from_label.grid(row=1)
to_label.grid(row=2)
result_label.grid(row=3)
status_label.grid(row=4, column=0)

amount_w.grid(row=0, column=1)
from_combobox.grid(row=1, column=1)
to_combobox.grid(row=2, column=1)
result_w.grid(row=3, column=1)
convert_button.grid(row=4, column=1)

window.mainloop()


