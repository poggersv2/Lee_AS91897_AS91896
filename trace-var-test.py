import customtkinter as ctk
import tkinter.messagebox as mbox
import tkinter as tk
from PIL import Image
import os
import sys

class App(ctk.CTk):
    # Initialize class
    def __init__(self):
        # Initialize the function
        super().__init__()

        # Load resources as constant variables
        
        # Configure file directories for the font and logo
        # OS makes sure that these are customized to the operating system's path 
        self.BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        self.LOGO_PATH = os.path.join(self.BASE_DIR, "Resources", "Images", "logo.png")
        self.FONT_PATH = os.path.join(self.BASE_DIR, "Resources", "Fonts", "Outfit-Medium.ttf")
        
        # Constant variables for appearence 
        self.CORNER_RADIUS = 50
        self.ENTRY_COLOR = "#ffffff"
        self.BACKGROUND_COLOUR = "#1c1c1c"

        self.title_font = ("Outfit Medium", 24)
        self.body_font = ("Outfit Medium", 18)


        # Configure main window
        self.title("Julie's Party Hire")
        self._set_appearance_mode("light")
        
        # Load font
        ctk.FontManager.load_font(self.FONT_PATH)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)
        self.grid_columnconfigure(2, weight=0)
        self.grid_columnconfigure(3, weight=0)
        self.grid_columnconfigure(4, weight=1)

        self.grid_rowconfigure(2, weight=0)
        self.grid_columnconfigure(2, weight=10)

        # Logo image, opens logo image via PIL
        self.logo_image = ctk.CTkImage(light_image = Image.open(self.LOGO_PATH), dark_image = Image.open(self.LOGO_PATH), size=(40,40))
        self.logo_label = ctk.CTkLabel(self,text="", image = self.logo_image)
        self.logo_label.grid(row=0, column=0, padx=(10, 10), pady=20, sticky="EW")


        self.title_label = ctk.CTkLabel(self, text = "Juile's Party Hire", font = self.title_font)
        self.title_label.grid(row=0, column=1, columnspan=3, padx=(0, 0), pady=20, sticky="w")

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
        self.price = [9,3,2,1,6]

        self.quantity_vars = []
        self.checkbox_vars = []
        self.total_labels = []
        

        for i in self.headers:
            # Iterate through table headers list and places them
            self.header = ctk.CTkLabel(self.item_frame, text=i,font=self.body_font)
            self.header.grid(row=0, column=self.headers.index(i), padx=50, pady=5)

        for position, item in enumerate(self.items):
            # Set initial position to the top (1, as headers take up row 0)
            self.row_pos = position+1
            self.column_pos = 0

            ##################
            # CHECKBOX SETUP #
            ##################
            # Setup as a bool variable. Append state onto list checkbox_vars
            self.checkbox_var = ctk.BooleanVar()
            self.checkbox_vars.append(self.checkbox_var)
            print("checkbox tracevar added")
            self.checkbox_var.trace_add("write", lambda *args: on_check)
            
            self.checkbox = ctk.CTkCheckBox(
                self.item_frame,
                text="",
                font=self.body_font,
                command=lambda pos=position: on_check(pos),
                variable=self.checkbox_var  # <-- Link the BooleanVar to the checkbox!
            )
            

            self.checkbox.grid(row=self.row_pos, column=self.column_pos, padx=30, pady=(0,10))
            self.column_pos += 1

            ####################
            # ITEM LABEL SETUP #
            ####################

            item_label = ctk.CTkLabel(self.item_frame, text=f"{item}",font=self.body_font)
            item_label.grid(row=self.row_pos,  column=self.column_pos)
            self.column_pos += 1

            ########################
            # QUANTITY ENTRY SETUP #
            ########################
            self.quantity_var = ctk.StringVar(value="")
            self.quantity_vars.append(self.quantity_var)
            self.quantity_var.trace_add("write", lambda *args: check_totals()) 

            
            quantity = ctk.CTkEntry(self.item_frame, width=70, font=self.body_font, corner_radius=self.CORNER_RADIUS,
                fg_color=self.ENTRY_COLOR, text_color="black", border_color=self.ENTRY_COLOR,
                textvariable=self.quantity_var)
            quantity.grid(row=self.row_pos, column=self.column_pos, padx=50)
            self.column_pos += 1

            ##########################
            # ITEM PRICE LABEL SETUP #
            ##########################
            item_price = ctk.CTkLabel(self.item_frame, text=f"${self.price[position]}",font=self.body_font)
            item_price.grid(row=self.row_pos, column=self.column_pos, padx=50)
            self.column_pos += 1

            ##########################
            # ITEM TOTAL LABEL SETUP #
            ##########################
            item_total_label = ctk.CTkLabel(self.item_frame, text="$0.00",font=self.body_font)
            item_total_label.grid(row=self.row_pos, column=self.column_pos, padx=50)
            self.total_labels.append(item_total_label)

############################################################################################################################

        self.submit_button = ctk.CTkButton(self, text="Submit",width=100, height=35, corner_radius=10, fg_color=self.ENTRY_COLOR, text_color="#000", font=self.body_font)
        self.submit_button.grid(row=7, column = 1)

        def calculate_total():
            global total
            total = 0.00
            self.total_label = ctk.CTkLabel(self, )

        def on_check(position):
            if self.checkbox_vars[position].get():  # Only run if checked
                item = self.items[position]
                animations(item)

        def animations(item):
           print(f"Animation: {item}")


        def error_message(reason, item, index):
            if reason == "type":
                mbox.showerror("Input Error", f"Please enter a valid quantity for {item}.")
                self.quantity_vars[index].set("")
            elif reason == "negative":
                mbox.showerror("Input Error", f"Quantity for {item} cannot be negative.")
                self.quantity_vars[index].set("")
            elif reason == "too big":
                mbox.showerror("Input Error", f"Quantity for {item} is too large (max 500).")
                self.quantity_vars[index].set("")
            elif reason == "name":
                mbox.showerror("Input Error", "Please enter both first and last names.")


        def check_totals():
            print("tracevar ran")
            for i, item in enumerate(self.items):
                value_str = self.quantity_vars[i].get()
                if value_str == "":
                    self.total_labels[i].configure(text="$0.00")
                    continue
                try:
                    quantity = int(value_str)
                    if quantity < 0:
                        error_message("negative", item, i)
                        self.total_labels[i].configure(text="$0.00")
                    elif quantity > 500:
                        error_message("too big", item, i)
                        self.total_labels[i].configure(text="$0.00")
                    else:
                        total = self.price[i] * quantity
                        self.total_labels[i].configure(text=f"${total:.2f}")
                except ValueError:
                    self.total_labels[i].configure(text="$0.00")
                    error_message("type", item, i)

                



if __name__ == "__main__":
    app = App()
    app.mainloop()