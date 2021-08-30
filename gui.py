

import tkinter as tk
from converter import convert



main_window = tk.Tk() # main window object
main_window.title("Currency Converter")

tk.Label(main_window, text="Amount").grid(row=0)
tk.Label(main_window, text="From").grid(row=1)
tk.Label(main_window, text="To").grid(row=2)
tk.Label(main_window, text="Result").grid(row=3)



amount_w = tk.Entry(main_window)
from_currency_w = tk.Entry(main_window)
to_currency_w = tk.Entry(main_window)
result_w = tk.Entry(main_window)

amount_w.grid(row=0, column=1)
from_currency_w.grid(row=1, column=1)
to_currency_w.grid(row=2, column=1)
result_w.grid(row=3, column=1)


def func():
   amt = int(amount_w.get())
   from_curr = from_currency_w.get()
   to_curr = to_currency_w.get()
   res = convert(amt, from_curr, to_curr)
   result_w.delete(0, 'end')
   result_w.insert(0, str(res))

button = tk.Button(main_window, text='Convert', width=10, height=1, command=func).grid(row=4, column=1)


main_window.mainloop()


