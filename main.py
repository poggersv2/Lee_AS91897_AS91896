import customtkinter as ctk
import tkinter.messagebox as mbox
import tkinter as tk
from PIL import Image
import os
import sys
import os

class App(ctk.CTk):
    # Initialize class
    def __init__(self):
        # Initialize the function
        super().__init__()


win=ctk.CTk()
win.state("zoomed") 
win.title("Julie's Party Hire")
ctk.set_appearance_mode("Dark")

win.grid_columnconfigure(0, weight=1)
win.grid_columnconfigure(1, weight=0)
win.grid_columnconfigure(2, weight=0)
win.grid_columnconfigure(3, weight=0)
win.grid_columnconfigure(4, weight=1)

title_font = ("Outfit Medium", 24)
body_font = ("Outfit Medium", 18)

ENTRY_CORNER_RADIUS = 10
ENTRY_COLOR = "#FFFFFF"

#logo image
logo_image = ctk.CTkImage(light_image=Image.open(LOGO_PATH), dark_image=Image.open(LOGO_PATH), size=(40, 40))
logo_label = ctk.CTkLabel(win, text="", image=logo_image)
logo_label.grid(row=0, column=0, padx=(0, 10), pady=20, sticky="e")

title_label = ctk.CTkLabel(win, text="Julie's Party Hire", font=title_font)
title_label.grid(row=0, column=1, columnspan=3, padx=(0, 0), pady=20, sticky="w")

name_label = ctk.CTkLabel(win, text="Name:", font=body_font)
name_label.grid(row=1, column=1, padx=(0, 10), pady=10, sticky="e")
name_entry = ctk.CTkEntry(win, width=200, font=body_font, corner_radius=ENTRY_CORNER_RADIUS, fg_color=ENTRY_COLOR, text_color="black", border_color=ENTRY_COLOR)
name_entry.grid(row=1, column=2, padx=(0, 10), pady=10, sticky="w")

last_name_label = ctk.CTkLabel(win, text="Last Name:", font=body_font)
last_name_label.grid(row=1, column=3, padx=(10, 10), pady=10, sticky="e")
last_name_entry = ctk.CTkEntry(win, width=200, font=body_font, corner_radius=ENTRY_CORNER_RADIUS, fg_color=ENTRY_COLOR, text_color="black", border_color=ENTRY_COLOR)
last_name_entry.grid(row=1, column=4, padx=(0, 40), pady=10, sticky="w")

order_frame = ctk.CTkFrame(win, corner_radius=20)
order_frame.grid(row=6, column=0, columnspan=10, padx=40, pady=20, sticky="nsew")

items_frame = ctk.CTkFrame(win, corner_radius=15)
items_frame.grid(row=2, column=0, columnspan=10, padx=40, pady=10, sticky="nsew")

headers = ["", "Items", "Quantity", "Price", "Total"]
items = ["Balloons", "Party Hats", "Streamers", "Confetti", "Glitter"]
item_prices = [5.0, 7.0, 3.0, 1.0, 2.0]
quantity_vars = []
checkbox_vars = []
total_labels = []

for i in headers:
    ctk.CTkLabel(items_frame, text=i, font=body_font).grid(row=0, column=headers.index(i), padx=10, pady=5)

for position, i in enumerate(items):
    checkbox_var = ctk.BooleanVar()
    checkbox_vars.append(checkbox_var)
    checkbox = ctk.CTkCheckBox(items_frame, text="", variable=checkbox_var, font=body_font)
    checkbox.grid(row=position + 1, column=0, padx=10, pady=5, sticky="w")
    item_label = ctk.CTkLabel(items_frame, text=i, font=body_font)
    item_label.grid(row=position + 1, column=1, padx=10, pady=5, sticky="w")
    
    quantity_var = ctk.StringVar(value="")
    quantity_vars.append(quantity_var)
    quantity_var.trace_add("write", lambda *args: check_totals()) 
    
    quantity_input = ctk.CTkEntry(
        items_frame, width=50, font=body_font, corner_radius=ENTRY_CORNER_RADIUS,
        fg_color=ENTRY_COLOR, text_color="black", border_color=ENTRY_COLOR,
        textvariable=quantity_var
    )
    quantity_input.grid(row=position+ 1, column=2, padx=10, pady=5, sticky="w")
    
    price_label = ctk.CTkLabel(items_frame, text=f"${item_prices[position]:.2f}", font=body_font)
    price_label.grid(row=position + 1, column=3, padx=10, pady=5, sticky="w")
    
    total_label = ctk.CTkLabel(items_frame, text="$0.00", font=body_font)
    total_label.grid(row=position + 1, column=4, padx=10, pady=5, sticky="w")
    total_labels.append(total_label)

def submit():
    first_name = name_entry.get()
    last_name = last_name_entry.get()
    if not first_name or not last_name:
        error_message("name")

def error_message(reason, *args):
    if reason == "type":
        mbox.showerror("Input Error", f"Please enter a valid quantity for {args[0]}.")
        quantity_vars[args[1]].set("")
    elif reason == "negative":
        mbox.showerror("Input Error", f"Quantity for {args[0]} cannot be negative.")
        quantity_vars[args[1]].set("")
    elif reason == "too big":
        mbox.showerror("Input Error", f"Quantity for {args[0]} is too large (max 500).")
        quantity_vars[args[1]].set("")
    elif reason == "name":
        mbox.showerror("Input Error", "Please enter both first and last names.")

def check_totals():
    for i, item in enumerate(items):
        try:
            if not quantity_vars[i].get():
                total_labels[i].configure(text="$0.00")
                continue
            quantity = int(quantity_vars[i].get())
            if quantity < 0:
                error_message("negative", item, i)
                total_labels[i].configure(text="$0.00")
                continue
            if quantity > 500:
                error_message("too big", item, i)
                total_labels[i].configure(text="$0.00")
                continue
            total = item_prices[i] * quantity
            total_labels[i].configure(text=f"${total:.2f}")
        except ValueError:
            total_labels[i].configure(text="$0.00")
            error_message("type", item, i)

if __name__ == "__main__":
    app = App()
    app.mainloop()