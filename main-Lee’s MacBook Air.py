import customtkinter as ctk
import tkinter.messagebox as mbox
import tkinter as tk
from PIL import Image
import os
import sys

class App(ctk.CTk):
    #initialize class
    def __init__(self):
        #initialize the function
        super().__init__()

        #load resources as constant variables
        
        # configure file directories for the font and logo
        # OS makes sure that these are customized to the operating system's path 
        self.BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        self.LOGO_PATH = os.path.join(self.BASE_DIR, "Resources", "Images", "logo.png")
        self.FONT_PATH = os.path.join(self.BASE_DIR, "Resources", "Fonts", "Outfit-Medium.ttf")
        
        #constant variables for appearence 
        self.CORNER_RADIUS = 50
        self.ENTRY_COLOR = "#ffffff" # hex code for white
        self.BACKGROUND_COLOUR = "#1c1c1c"

        self.title_font = ("Outfit Medium", 24)
        self.body_font = ("Outfit Medium", 18)


        # configure main window
        self.title("Julie's Party Hire")
        self._set_appearance_mode("dark")
        
        #load font
        ctk.FontManager.load_font(self.FONT_PATH)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)
        self.grid_columnconfigure(2, weight=0)
        self.grid_columnconfigure(3, weight=0)
        self.grid_columnconfigure(4, weight=1)

        self.grid_rowconfigure(2, weight=0)
        self.grid_columnconfigure(2, weight=10)

        #logo images and text
        self.logo_image = ctk.CTkImage(light_image = Image.open(self.LOGO_PATH), dark_image = Image.open(self.LOGO_PATH), size=(40,40))
        
        self.header_label = ctk.CTkLabel(
            self,
            text="Julie's Party Hire",
            image=self.logo_image,
            compound="left",
            font=self.title_font
        )
        self.header_label.grid(
            row=0,
            column=0,
            columnspan=5,
            pady=20,
            sticky="ew"
        )

        self.name_label = ctk.CTkLabel(self, text = "First Name:", font=self.body_font)
        self.name_label.grid(row=1, column=1, padx=(0, 10), pady=10, sticky="e")

        self.name_entry = ctk.CTkEntry(self, width=200, font=self.body_font, corner_radius=self.CORNER_RADIUS, fg_color=self.ENTRY_COLOR, text_color="black", border_color=self.ENTRY_COLOR)
        self.name_entry.grid(row=1, column=2, padx=(0, 10), pady=10, sticky="w")

        self.last_name_label = ctk.CTkLabel(self, text="Last Name:", font=self.body_font)
        self.last_name_label.grid(row=1, column=3, padx=(10, 10), pady=10, sticky="e")
        
        self.last_name_entry = ctk.CTkEntry(self, width=200, font=self.body_font, corner_radius=self.CORNER_RADIUS, fg_color=self.ENTRY_COLOR, text_color="black", border_color=self.ENTRY_COLOR)
        self.last_name_entry.grid(row=1, column=4, padx=(0, 40), pady=10, sticky="w")

        self.item_frame = ctk.CTkFrame(self,corner_radius=20)
        self.item_frame.grid(row=6, column=0, columnspan=10, padx=40, pady=(30,10), sticky="nsew")

        self.headers = ["", "Items", "Quantity", "Price", "Total"]
        self.items = ["Balloons", "Party Hats", "Streamers", "Confetti", "Glitter"]
        self.price = [1,2,3,4,5]


        

        self.quantity_vars = []
        self.checkbox_vars = []
        self.total_labels = []
        

        for i in self.headers:
            self.header = ctk.CTkLabel(self.item_frame, text=i,font=self.body_font)
            self.header.grid(row=0, column=self.headers.index(i), padx=50, pady=5)

        for position, item in enumerate(self.items):
            self.row_pos = position+1
            self.column_pos = 0

            self.checkbox_var = ctk.BooleanVar()
            self.checkbox_vars.append(self.checkbox_var)

            self.checkbox = ctk.CTkCheckBox(self.item_frame, text="", font=self.body_font)
            self.checkbox.grid(row=self.row_pos, column=self.column_pos, padx=30, pady=(0,10))
            self.column_pos += 1

            item_label = ctk.CTkLabel(self.item_frame, text=f"{item}",font=self.body_font)
            item_label.grid(row=self.row_pos,  column=self.column_pos)
            self.column_pos += 1

            self.quantity_var = ctk.StringVar(value="")
            self.quantity_vars.append(self.quantity_var)
            self.quantity_var.trace_add("write", lambda *args: check_totals())  # <-- FIXED

            
            quantity = ctk.CTkEntry(self.item_frame, width=70, font=self.body_font, corner_radius=self.CORNER_RADIUS,
                fg_color=self.ENTRY_COLOR, text_color="black", border_color=self.ENTRY_COLOR,
                textvariable=self.quantity_var)
            quantity.grid(row=self.row_pos, column=self.column_pos, padx=50)
            self.column_pos += 1

            item_price = ctk.CTkLabel(self.item_frame, text=f"${self.price[position]}",font=self.body_font)
            item_price.grid(row=self.row_pos, column=self.column_pos, padx=50)
            self.column_pos += 1

            item_total_label = ctk.CTkLabel(self.item_frame, text="$0.00",font=self.body_font)
            item_total_label.grid(row=self.row_pos, column=self.column_pos, padx=50)
            self.total_labels.append(item_total_label)
############################################################################################################################
        self.submit_button = ctk.CTkButton(self)

        def check_totals():
            print("tracevar ran")


if __name__ == "__main__":
    app = App()
    app.mainloop()