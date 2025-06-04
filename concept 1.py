import customtkinter as ctk
import tkinter.messagebox as mbox
from CTkTable import CTkTable
from PIL import Image

LOGO_PATH = r"Resources\Images\logo.png"
FONT_PATH = r"Resources\Fonts\Outfit-Medium.ttf"

win=ctk.CTk()
win.geometry("1200x800")
win.title("Julie's Party Hire")
#win.resizable(False, False)
ctk.set_appearance_mode("Dark")
ctk.FontManager.load_font(FONT_PATH)

win.grid_columnconfigure(0, weight=0)
win.grid_columnconfigure(1, weight=1)

title_font = ("Outfit Medium", 24)
body_font = ("Outfit Medium", 18)

#logo image
logo_image = ctk.CTkImage(light_image=Image.open(LOGO_PATH), dark_image=Image.open(LOGO_PATH), size=(40, 40))
logo_label = ctk.CTkLabel(win, text="", image=logo_image)
logo_label.grid(row=0, column=0, padx=40, pady=20, sticky="w")

#title label
title_label = ctk.CTkLabel(win, text="Julie's Party Hire", font=title_font)
title_label.grid(row=0, column=0, padx=100, pady=20, sticky="w")

#first name label
name_label = ctk.CTkLabel(win, text="Name:", font=body_font)
name_label.grid(row=1, column=0, padx=40, pady=10, sticky="w")
name_entry = ctk.CTkEntry(win, width=200, font=body_font)
name_entry.grid(row=1, column=1, padx=20, pady=10, sticky="w")

#last name label
last_name_label = ctk.CTkLabel(win, text="Last Name:", font=body_font)
last_name_label.grid(row=2, column=0, padx=40, pady=10, sticky="w")
last_name_entry = ctk.CTkEntry(win, width=200, font=body_font)
last_name_entry.grid(row=2, column=1, padx=20, pady=10, sticky="w")

#submit button
def submit():
    first_name = name_entry.get()
    last_name = last_name_entry.get()
    if not first_name or not last_name:
        mbox.showerror("Input Error", "Please enter both first and last names.")

win.mainloop()
