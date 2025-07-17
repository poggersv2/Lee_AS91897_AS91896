import customtkinter as ctk
import tkinter as tk
from PIL import Image
import os
import sys

win = ctk.CTk()
win.title("Simple Tkinter Window")
win.geometry("1000x700")

l = ["Balloons", "Party Hats", "Streamers", "Confetti", "Glitter"]
price = [1,2,3,4,5]

quantity_vars = []
checkbox_vars = []
total_labels = []


        

for position, item in enumerate(l):
    row_pos = position+1
    column_pos = 0

    checkbox_var = ctk.BooleanVar()
    checkbox_vars.append(checkbox_var)

    checkbox = ctk.CTkCheckBox(win, text="")
    checkbox.grid(row=row_pos, column=column_pos)
    column_pos += 1

    item_label = ctk.CTkLabel(win, text=f"{item}")
    item_label.grid(row=row_pos,  column=column_pos)
    column_pos += 1

    quantity_var = ctk.StringVar(value="")
    quantity_vars.append(quantity_var)
    quantity_var.trace_add("write", lambda *args: check_totals())  

    quantity = ctk.CTkEntry(win, width=100, height=5, textvariable=quantity_var)
    quantity.grid(row=row_pos, column=column_pos, padx=50)
    column_pos += 1

    item_price = ctk.CTkLabel(win, text=f"${price[position]}")
    item_price.grid(row=row_pos, column=column_pos, padx=50)
    column_pos += 1

    item_total_label = ctk.CTkLabel(win, text="$0.00")
    item_total_label.grid(row=row_pos, column=column_pos, padx=50)
    total_labels.append(item_total_label)


def check_totals():
    print("trace var ran")
    for pos, item in enumerate(l):
        try:
            value = int(quantity_vars[pos].get())
            if value <= 0 or value > 500:
                total_labels[pos].configure(text="$0.00")
            else:
                total = price[pos] * value
                total_labels[pos].configure(text=f"${total:.2f}")
        except ValueError:
            total_labels[pos].configure(text="$0.00")


entry = ctk.CTkEntry(win)
entry.grid(row=6)

def select():
    selected_number = int(entry.get())-1
    print(l[selected_number])
    selected_item = ctk.CTkLabel(win, text=l[selected_number])
    selected_item.grid(row = 8)

button = ctk.CTkButton(win, text="select", command=select)
button.grid(row = 7)

win.mainloop()


