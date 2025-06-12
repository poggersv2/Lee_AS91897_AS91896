import customtkinter as ctk
import tkinter.messagebox as mbox
import tkinter as tk
from PIL import Image
import os
import sys

class App(ctk.CTk):
    #initialize class
    def __init__(self):
        super().__init__()

        #load resources as constant variables
        
        # configure file directories for the font and logo
        # OS makes sure that these are customized to the operating system's path 
        self.BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        self.LOGO_PATH = os.path.join(self.BASE_DIR, "Resources", "Images", "logo.png")
        self.FONT_PATH = os.path.join(self.BASE_DIR, "Resources", "Fonts", "Outfit-Medium.ttf")
        
        #constant variables for appearence 
        self.ENTRY_CORNER_RADIUS = 50
        self.ENTRY_COLOR = "#ffffff" # hex code for white
        self.BACKGROUND_COLOUR = "#1c1c1c"

        self.title_font = ("Outfit Medium", 24)
        self.body_font = ("Outfit Medium", 18)


        # configure main window
        self.title("Julie's Party Hire")
        self._set_appearance_mode("light")
        
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
        self.logo_label = ctk.CTkLabel(self,text="", image = self.logo_image)
        self.logo_label.grid(row=0, column=0, padx=(10, 10), pady=20, sticky="EW")

        self.title_label = ctk.CTkLabel(self, text = "Juile's Party Hire", font = self.title_font)
        self.title_label.grid(row=0, column=1, columnspan=3, padx=(0, 0), pady=20, sticky="w")

        self.name_label = ctk.CTkLabel(self, text = "First Name:", font=self.body_font)
        self.name_label.grid(row=1, column=1, padx=(0, 10), pady=10, sticky="e")

        self.name_entry = ctk.CTkEntry(self, width=200, font=self.body_font, corner_radius=self.ENTRY_CORNER_RADIUS, fg_color=self.ENTRY_COLOR, text_color="black", border_color=self.ENTRY_COLOR)
        self.name_entry.grid(row=1, column=2, padx=(0, 10), pady=10, sticky="w")

        self.last_name_label = ctk.CTkLabel(self, text="Last Name:", font=self.body_font)
        self.last_name_label.grid(row=1, column=3, padx=(10, 10), pady=10, sticky="e")
        
        self.last_name_entry = ctk.CTkEntry(self, width=200, font=self.body_font, corner_radius=self.ENTRY_CORNER_RADIUS, fg_color=self.ENTRY_COLOR, text_color="black", border_color=self.ENTRY_COLOR)
        self.last_name_entry.grid(row=1, column=4, padx=(0, 40), pady=10, sticky="w")

        self.order_frame = ctk.CTkFrame(self,corner_radius=20)
        self.order_frame.grid(row=6, column=0, columnspan=10, padx=40, pady=20, sticky="nsew")

        self.headers = ["", "Items", "Quantity", "Price", "Total"]
        self.items = ["Balloons", "Party Hats", "Streamers", "Confetti", "Glitter"]
        self.item_prices = [5.0, 7.0, 3.0, 1.0, 2.0]

        for i in self.headers:
            self.header = ctk.CTkLabel(self.order_frame, text=i,font=self.body_font)
            self.header.grid(row=0, column=self.headers.index(i), padx=10, pady=5)
            
if __name__ == "__main__":
    app = App()
    app.mainloop()