import customtkinter
from CTkTable import *

root = customtkinter.CTk()

value = [["Name","Test123","no. 3",4,5],
         [1,2,3,4,5],
         [1,2,3,4,5],
         [1,2,3,4,5],
         [1,2,3,4,5]]

table = CTkTable(master=root, row=5, column=5, values=value)
table.pack(expand=False, fill="both", padx=20, pady=20)

root.mainloop()