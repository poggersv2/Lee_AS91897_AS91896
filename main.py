import customtkinter as ctk
import tkinter.messagebox as mbox
import tkinter as tk
from PIL import Image
import os
import sys
import json
import random

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

        self.title_font = ("Outfit Medium", 24)
        self.body_font = ("Outfit Medium", 18)

        # Configure main window
        self.title("Julie's Party Hire")
        ctk.set_appearance_mode("dark")
        self.attributes("-alpha", 0.9)

        # Load font
        ctk.FontManager.load_font(self.FONT_PATH)

        # Logo image, opens logo image via PIL
        self.logo_image = ctk.CTkImage(light_image = Image.open(self.LOGO_PATH), dark_image = Image.open(self.LOGO_PATH), size=(40,40))
        self.logo_label = ctk.CTkLabel(self,text="", image = self.logo_image)
        self.logo_label.grid(row=0, column=0, padx=(10, 10), pady=20, sticky="EW")


        self.title_label = ctk.CTkLabel(self, text = "Juile's Party Hire", font = self.title_font)
        self.title_label.grid(row=0, column=1, columnspan=3, padx=(0, 0), pady=20, sticky="w")

        self.name_label = ctk.CTkLabel(self, text = "First Name:", font=self.body_font)
        self.name_label.grid(row=1, column=1, padx=(0, 10), pady=10, sticky="e")

        # Name entry setup
        self.first_name_var = tk.StringVar()
        self.name_entry = ctk.CTkEntry(self, width=200, font=self.body_font, corner_radius=self.CORNER_RADIUS, textvariable=self.first_name_var)
        self.name_entry.grid(row=1, column=2, padx=(0, 10), pady=10, sticky="w")
        self.first_name_var.trace_add(
            "write",
            lambda *args, name=self.first_name_var: self.check_name(name)
        )

        self.last_name_label = ctk.CTkLabel(self, text="Last Name:", font=self.body_font)
        self.last_name_label.grid(row=1, column=3, padx=(10, 10), pady=10, sticky="e")
        
        # Last name entry setup
        self.last_name_var = tk.StringVar()
        self.last_name_entry = ctk.CTkEntry(self, width=200, font=self.body_font, corner_radius=self.CORNER_RADIUS, textvariable=self.last_name_var)
        self.last_name_entry.grid(row=1, column=4, padx=(0, 40), pady=10, sticky="w")
        self.last_name_var.trace_add(
            "write",
            lambda *args, name=self.last_name_var: self.check_name(name)
        )

        self.display_items()
        
        self.submit_button = ctk.CTkButton(
            self, text="Submit", width=100, height=35, corner_radius=10,
            font=self.body_font, command=self.submit
        )
        self.submit_button.grid(row=7, column=1)
        
        self.receipt_frame = ctk.CTkFrame(self, corner_radius=20)
        self.receipt_frame.grid(row=8, column=0, columnspan=10, padx=40, pady=10, sticky="nsew")

        self.display_receipts()
        

    def display_items(self):
        self.item_frame = ctk.CTkFrame(self, corner_radius=20)
        self.item_frame.grid(row=6, column=0, columnspan=10, padx=40, pady=(30,10), sticky="nsew")

        self.headers = ["Items", "Quantity", "Price", "Total"]
        self.items = ["Balloons", "Party Hats", "Streamers", "Confetti", "Glitter"]
        self.price = [9,3,2,1,6]

        self.quantity_vars = []
        self.checkbox_vars = []
        self.total_labels = []
        

        for i in self.headers:
            # Iterate through table headers list and places them
            self.header = ctk.CTkLabel(self.item_frame, text=i,font=self.body_font)
            self.header.grid(row=0, column=self.headers.index(i)+1, padx=50, pady=5)

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
            self.checkbox_var.trace_add("write", lambda *args: self.on_check)
            
            self.checkbox = ctk.CTkCheckBox(
                self.item_frame,
                text="",
                font=self.body_font,
                command=lambda pos=position: self.on_check(pos),
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
            self.quantity_var.trace_add("write", lambda *args: self.check_totals()) 

            
            quantity = ctk.CTkEntry(self.item_frame, width=70, font=self.body_font, corner_radius=self.CORNER_RADIUS, textvariable=self.quantity_var)
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
            
    def display_receipts(self):
        # Clear previous widgets in receipt_frame
        for widget in self.receipt_frame.winfo_children():
            widget.destroy()

        receipts = os.path.join(self.BASE_DIR, "receipts.json")
        try:
            with open(receipts, "r") as f:
                all_receipts = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            all_receipts = []

        receipts_header = ["","Reciept No", "Name", "Items", "Total Price"]

        # Headers
        #for i in receipts_header:
         #   self.header = ctk.CTkLabel(self.item_frame, text=i,font=self.body_font)
          #  self.header.grid(row=0, column=self.headers.index(i)+1, padx=50, pady=5)

        row = 1
        for receipt in all_receipts:
            # Receipt Info
            info_label = ctk.CTkLabel(
                self.receipt_frame,
                text=f"{receipt['receipt_no']}",
                font=self.body_font
            )
            info_label.grid(row=row, column=0, sticky="w")

            name_label = ctk.CTkLabel(
                self.receipt_frame,
                text=f"{receipt['first_name']} {receipt['last_name']}",
                font=self.body_font
            )
            name_label.grid(row=row, column=1, sticky="w")

            # Items (combine names and quantities for display)
            items_str = ", ".join([f"{item['name']} x{item['quantity']}" for item in receipt["items"]])
            items_label = ctk.CTkLabel(self.receipt_frame, text=items_str, font=self.body_font)
            items_label.grid(row=row, column=2, sticky="w")

            price_label = ctk.CTkLabel(self.receipt_frame, text=f"${receipt['total']:.2f}", font=self.body_font)
            price_label.grid(row=row, column=3, sticky="w")

            total_label = ctk.CTkLabel(self.receipt_frame, text=f"${receipt['total']:.2f}", font=self.body_font)
            total_label.grid(row=row, column=4, sticky="w")

            row += 1
        
    def calculate_total(self):
        global total
        total = 0.00
        #self.total_label = ctk.CTkLabel(self, )

    def on_check(self,position):
        if self.checkbox_vars[position].get():  # Only run if checked
            item = self.items[position]
            self.animations(item)

    def animations(self, item):
        print(f"Animation: {item}")

    # args[0] = reason, args[1] = item, args[2] = index
    def error_message(self, *args):
        if args[0] == "type":
            mbox.showerror("Input Error", f"Please enter a valid quantity for {args[1]}.")
            self.quantity_vars[args[2]].set("")
        elif args[0] == "negative":
            mbox.showerror("Input Error", f"Quantity for {args[1]} cannot be negative.")
            self.quantity_vars[args[2]].set("")
        elif args[0] == "too big":
            mbox.showerror("Input Error", f"Quantity for {args[1]} is too large (max 500).")
            self.quantity_vars[args[2]].set("")
        elif args[0] == "names empty":
            mbox.showerror("Input Error", "Please enter both first and last names.")
        elif args[0] == "name type":
            mbox.showerror("Input Error", f"Please enter a valid input for {args[1]}.")
            self.name_var.set("")



    def check_totals(self):
        print("tracevar ran")
        for i, item in enumerate(self.items):
            value_str = self.quantity_vars[i].get()
            if value_str == "":
                self.total_labels[i].configure(text="$0.00")
                continue
            try:
                quantity = int(value_str)
                if quantity < 0:
                    self.error_message("negative", item, i)
                    self.total_labels[i].configure(text="$0.00")
                elif quantity > 500:
                    self.error_message("too big", item, i)
                    self.total_labels[i].configure(text="$0.00")
                else:
                    total = self.price[i] * quantity
                    self.total_labels[i].configure(text=f"${total:.2f}")
            except ValueError:
                self.total_labels[i].configure(text="$0.00")
                self.error_message("type", item, i)

                

    def check_name(self, var):
        value = var.get()
        filtered = ''.join(ch for ch in value if ch.isalpha())
        if filtered != value:
            var.set(filtered)

    def submit(self):
        if self.first_name_var.get() == "" or self.last_name_var.get() == "":
            self.error_message("names empty")
            return 
            
        #if not self.name_var
        receipt_no = random.randint(100000, 999999)
        items = []
        total = 0

        for item, unit_price, qty_var, cb_var in zip(self.items, self.price, self.quantity_vars, self.checkbox_vars):
            try:
                quantity = int(qty_var.get())
            except ValueError:
                quantity = 0
            if cb_var.get() and quantity > 0:
                item_total = unit_price * quantity
                items.append({
                    "name": item,
                    "quantity": quantity,
                    "unit_price": unit_price,
                    "total": item_total
                })
                total += item_total

        customer = {
            "receipt_no": receipt_no,
            "first_name": self.first_name_var.get(),
            "last_name": self.last_name_var.get(),
            "items": items,
            "total": total
        }

        receipts_file = os.path.join(self.BASE_DIR, "receipts.json")
        try:
            with open(receipts_file, "r") as f:
                all_receipts = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            all_receipts = []

        all_receipts.append(customer)
        with open(receipts_file, "w") as f:
            json.dump(all_receipts, f, indent=4)

        mbox.showinfo("Saved", f"Receipt #{receipt_no} saved.")




if __name__ == "__main__":
    app = App()
    app.mainloop()