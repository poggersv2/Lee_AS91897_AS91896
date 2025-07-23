<<<<<<< HEAD
<<<<<<< Updated upstream
=======
>>>>>>> origin/main
import customtkinter as ctk

class App(ctk.CTk):
    # Initialize class
    def __init__(self):
        # Initialize the function
        super().__init__()
        self.title("Animation Test")
        self.geometry("1000x700")

        self.items = [f"Item {i}" for i in range(1, 11)]

        for idx, item in enumerate(self.items):
            var = ctk.BooleanVar()
            def on_check(idx=idx, var=var):
                if var.get():
                    print(f"{self.items[idx]} checked")
            ctk.CTkCheckBox(
                self,
                text=item,
                variable=var,
                command=on_check
            ).grid(row=1, column=idx)

if __name__ == "__main__":
    app = App()
    app.mainloop()
<<<<<<< HEAD
=======
import customtkinter as ctk

class App(ctk.CTk):
    # Initialize class
    def __init__(self):
        # Initialize the function
        super().__init__()
        self.title("Animation Test")
        self.geometry("1000x700")

        self.items = [f"Item {i}" for i in range(1, 11)]

        for idx, item in enumerate(self.items):
            var = ctk.BooleanVar()
            def on_check(idx=idx, var=var):
                if var.get():
                    print(f"{self.items[idx]} checked")
            ctk.CTkCheckBox(
                self,
                text=item,
                variable=var,
                command=on_check
            ).grid(row=1, column=idx)

if __name__ == "__main__":
    app = App()
    app.mainloop()
>>>>>>> Stashed changes
=======
>>>>>>> origin/main
