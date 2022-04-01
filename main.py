from tkinter import *
from tkinter import ttk


def validate_numeric_entry(text):
    return text.isdecimal()

def validate_alphanumeric(text: str) -> bool:
    return text.isalnum()

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()

ttk.Label(frm, text="Nombre de Usuario: ").grid(column=0, row=0)
ttk.Entry(frm, validate="key", validatecommand=(root.register(validate_alphanumeric),"%S" )).grid(column=1, row=0)

ttk.Label(frm, text="Nombre: ").grid(column=0, row=1)
ttk.Entry(frm, validate="key", validatecommand=(root.register(validate_alphanumeric),"%S" )).grid(column=1, row=1)

ttk.Label(frm, text="Edad: ").grid(column=0, row=2)
ttk.Entry(frm, validate="key", validatecommand=(root.register(validate_numeric_entry),"%S" )).grid(column=1, row=2)

ttk.Label(frm, text="Password: ").grid(column=0, row=3)
ttk.Entry(frm, validate="key", validatecommand=(root.register(validate_alphanumeric),"%S" )).grid(column=1, row=3)

ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=4)

root.mainloop()
