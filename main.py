import customtkinter as ctk
import tkinter.messagebox as mbox
from CTkTable import CTkTable
from PIL import Image
import sys



LOGO_PATH = r"Resources\Images\logo.png"
FONT_PATH = r"Resources\Fonts\Outfit-Medium.ttf"
ENTRY_CORNER_RADIUS = 10
ENTRY_COLOR = "#FFFFFF"  # White color for the entry fields

win=ctk.CTk()
win.state("zoomed") 
#win.geometry(f"{win.winfo_screenwidth()}x{win.winfo_screenheight()}+0+0")
#win.geometry("1200x800")
win.title("Julie's Party Hire")
ctk.set_appearance_mode("Dark")
ctk.FontManager.load_font(FONT_PATH)

win.grid_columnconfigure(0, weight=1)
win.grid_columnconfigure(1, weight=0)
win.grid_columnconfigure(2, weight=0)
win.grid_columnconfigure(3, weight=0)
win.grid_columnconfigure(4, weight=1)

win.grid_rowconfigure(2, weight=0)
win.grid_columnconfigure(2, weight=10)

title_font = ("Outfit Medium", 24)
body_font = ("Outfit Medium", 18)

#logo image
logo_image = ctk.CTkImage(light_image=Image.open(LOGO_PATH), dark_image=Image.open(LOGO_PATH), size=(40, 40))
logo_label = ctk.CTkLabel(win, text="", image=logo_image)
logo_label.grid(row=0, column=0, padx=(0, 10), pady=20, sticky="e")

#title label
title_label = ctk.CTkLabel(win, text="Julie's Party Hire", font=title_font)
title_label.grid(row=0, column=1, columnspan=3, padx=(0, 0), pady=20, sticky="w")


#first name label and entry
name_label = ctk.CTkLabel(win, text="Name:", font=body_font)
name_label.grid(row=1, column=1, padx=(0, 10), pady=10, sticky="e")
name_entry = ctk.CTkEntry(win, width=200, font=body_font, corner_radius=ENTRY_CORNER_RADIUS, fg_color=ENTRY_COLOR, text_color="black", border_color=ENTRY_COLOR)
name_entry.grid(row=1, column=2, padx=(0, 10), pady=10, sticky="w")

#last name label and entry
last_name_label = ctk.CTkLabel(win, text="Last Name:", font=body_font)
last_name_label.grid(row=1, column=3, padx=(10, 10), pady=10, sticky="e")
last_name_entry = ctk.CTkEntry(win, width=200, font=body_font, corner_radius=ENTRY_CORNER_RADIUS, fg_color=ENTRY_COLOR, text_color="black", border_color=ENTRY_COLOR)
last_name_entry.grid(row=1, column=4, padx=(0, 40), pady=10, sticky="w")

"""value = [[1,2,3,4,5],
         [1,2,3,4,5],
         [1,2,3,4,5],
         [1,2,3,4,5],
         [1,2,3,4,5]]


table = CTkTable(master=win, row=2, column=2, values=value)
table.grid(padx=20, pady=20, sticky="nsew")

"""
order_frame = ctk.CTkFrame(win, corner_radius=20)
order_frame.grid(row=6, column=0, columnspan=4, padx=40, pady=20, sticky="nsew")


#submit button
def submit():
    first_name = name_entry.get()
    last_name = last_name_entry.get()
    if not first_name or not last_name:
        mbox.showerror("Input Error", "Please enter both first and last names.")

win.mainloop()
