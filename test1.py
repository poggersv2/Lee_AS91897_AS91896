import customtkinter as ctk
import tkinter.messagebox as mbox
from PIL import Image
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOGO_PATH = os.path.join(BASE_DIR, "Resources", "Images", "logo.png")
FONT_PATH = os.path.join(BASE_DIR, "Resources", "Fonts", "Outfit-Medium.ttf")

ctk.set_appearance_mode("Dark")
ctk.FontManager.load_font(FONT_PATH)

win = ctk.CTk()
win.state("zoomed")
win.title("Julie's Party Hire")

for i in range(5):
    win.grid_columnconfigure(i, weight=1 if i in [0, 4] else 0)
win.grid_rowconfigure(2, weight=0)

title_font = ("Outfit Medium", 28, "bold")
body_font = ("Outfit Medium", 18)
header_font = ("Outfit Medium", 20, "bold")

logo_image = ctk.CTkImage(light_image=Image.open(LOGO_PATH), dark_image=Image.open(LOGO_PATH), size=(40, 40))
ctk.CTkLabel(win, text="", image=logo_image).grid(row=0, column=0, padx=(20, 10), pady=20, sticky="e")
ctk.CTkLabel(win, text="Julie's Party Hire", font=title_font).grid(row=0, column=1, columnspan=3, padx=0, pady=20, sticky="w")

ctk.CTkLabel(win, text="First Name:", font=body_font).grid(row=1, column=1, padx=(0, 10), pady=10, sticky="e")
name_entry = ctk.CTkEntry(win, width=200, font=body_font, corner_radius=10, fg_color="#FFF", text_color="black", border_color="#FFF")
name_entry.grid(row=1, column=2, padx=(0, 10), pady=10, sticky="w")

ctk.CTkLabel(win, text="Last Name:", font=body_font).grid(row=1, column=3, padx=(10, 10), pady=10, sticky="e")
last_name_entry = ctk.CTkEntry(win, width=200, font=body_font, corner_radius=10, fg_color="#FFF", text_color="black", border_color="#FFF")
last_name_entry.grid(row=1, column=4, padx=(0, 40), pady=10, sticky="w")

def submit():
    if not name_entry.get() or not last_name_entry.get():
        mbox.showerror("Input Error", "Please enter both first and last names.")

ctk.CTkButton(
    win, text="Submit", font=body_font, command=submit,
    fg_color="#FFF", text_color="#000", hover_color="#E0E0E0",
    corner_radius=12, width=100, height=36
).grid(row=3, column=0, padx=40, pady=10, sticky="w")

# Items Table
items_frame = ctk.CTkFrame(win, corner_radius=20, fg_color="#232323")
items_frame.grid(row=2, column=0, columnspan=10, padx=40, pady=10, sticky="nsew")

headers = ["", "Items", "Quantity", "Price", "Total"]
for col, header in enumerate(headers):
    ctk.CTkLabel(items_frame, text=header, font=header_font, text_color="#FFF").grid(row=0, column=col, padx=10, pady=5)

item_names = ["Balloons", "Party Hats", "Streamers", "Confetti", "Glitter"]
item_prices = [5.0, 7.0, 3.0, 1.0, 2.0]
quantity_vars, checkbox_vars, total_labels = [], [], []

def update_totals(*_):
    total_price = 0.0
    for qty_var, price, total_label, checkbox_var in zip(quantity_vars, item_prices, total_labels, checkbox_vars):
        qty = qty_var.get()
        checked = checkbox_var.get()
        item_total = qty * price if checked and qty > 0 else 0
        total_label.configure(text=f"${item_total:.2f}")
        total_price += item_total
    total_amount_label.configure(text=f"Total: ${total_price:.2f}")

for i, (item, price) in enumerate(zip(item_names, item_prices)):
    cb_var = ctk.BooleanVar()
    ctk.CTkCheckBox(
        items_frame, variable=cb_var, text="", width=30, command=update_totals,
        fg_color="#FFF", border_color="#888", hover_color="#DDD"
    ).grid(row=i+1, column=0, padx=5)
    checkbox_vars.append(cb_var)

    ctk.CTkLabel(items_frame, text=item, font=body_font, text_color="#FFF").grid(row=i+1, column=1, padx=10, sticky="w")

    qty_var = ctk.IntVar(value=0)
    quantity_vars.append(qty_var)
    ctk.CTkEntry(
        items_frame, textvariable=qty_var, width=60, font=body_font,
        corner_radius=8, fg_color="#FFF", text_color="#000", border_color="#DDD"
    ).grid(row=i+1, column=2)
    qty_var.trace_add("write", update_totals)

    ctk.CTkLabel(items_frame, text=f"${price:.2f}", font=body_font, text_color="#FFF").grid(row=i+1, column=3)
    total_label = ctk.CTkLabel(items_frame, text="$0.00", font=body_font, text_color="#FFF")
    total_label.grid(row=i+1, column=4)
    total_labels.append(total_label)

total_amount_label = ctk.CTkLabel(win, text="Total: $0.00", font=body_font, text_color="#FFF")
total_amount_label.grid(row=3, column=4, padx=40, pady=(0, 10), sticky="e")

# Receipts Section
receipts_frame = ctk.CTkFrame(win, corner_radius=20, fg_color="#232323")
receipts_frame.grid(row=4, column=0, columnspan=10, padx=40, pady=20, sticky="nsew")

ctk.CTkLabel(receipts_frame, text="Receipts", font=header_font, text_color="#FFF").grid(row=0, column=0, columnspan=5, pady=(10, 10))
receipt_headers = ["", "Receipt No.", "Items", "Total"]
for col, header in enumerate(receipt_headers):
    ctk.CTkLabel(receipts_frame, text=header, font=body_font, text_color="#FFF").grid(row=1, column=col, padx=10, pady=5, sticky="w")

example_receipts = [
    ("692232", "Balloons x20, Part Hats x5, Streamers x2, Confetti x100, Glitter x50", "$341.00"),
    ("218922", "Balloons x10, Part Hats x1, Streamers x100, Confetti x50, Glitter x25", "$923.00"),
    ("1231233", "Balloons x10, Part Hats x1, Streamers x100", "$923.00"),
    ("920323", "Balloons x299", "$1495.00"),
]

for i, (num, items, total) in enumerate(example_receipts):
    ctk.CTkCheckBox(receipts_frame, text="", width=30, fg_color="#FFF", border_color="#888", hover_color="#DDD").grid(row=i+2, column=0, padx=5)
    ctk.CTkLabel(receipts_frame, text=num, font=body_font, text_color="#FFF").grid(row=i+2, column=1, sticky="w")
    ctk.CTkLabel(receipts_frame, text=items, font=body_font, text_color="#FFF", wraplength=500, anchor="w", justify="left").grid(row=i+2, column=2, sticky="w")
    ctk.CTkLabel(receipts_frame, text=total, font=body_font, text_color="#FFF").grid(row=i+2, column=3, sticky="w")

ctk.CTkButton(
    win, text="More Info", font=body_font, fg_color="#FFF", text_color="#000",
    hover_color="#E0E0E0", corner_radius=12, width=120, height=36
).grid(row=5, column=0, padx=70, pady=10, sticky="w")

ctk.CTkButton(
    win, text="Delete", font=body_font, fg_color="#E74C3C", text_color="#FFF",
    hover_color="#C0392B", corner_radius=12, width=120, height=36
).grid(row=5, column=4, padx=40, pady=10, sticky="e")

win.mainloop()