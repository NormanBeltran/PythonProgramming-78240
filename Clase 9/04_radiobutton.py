import tkinter as tk
from tkinter import ttk

def prueba():
    print("Se ha elegido la opcion", variable.get())

root = tk.Tk()
variable = tk.IntVar()

radiobutton1 = tk.Radiobutton(text="Opcion 1", variable=variable, value=1, command=prueba)
radiobutton2 = tk.Radiobutton(text="Opcion 2", variable=variable, value=2, command=prueba)
radiobutton3 = tk.Radiobutton(text="Opcion 3", variable=variable, value=3, command=prueba)
radiobutton4 = tk.Radiobutton(text="Opcion 4", variable=variable, value=4, command=prueba)
radiobutton5 = tk.Radiobutton(text="Opcion 5", variable=variable, value=5, command=prueba)
radiobutton6 = tk.Radiobutton(text="Opcion 6", variable=variable, value=6, command=prueba)

radiobutton1.place(x=10, y=10)
radiobutton2.place(x=10, y=30)
radiobutton3.place(x=10, y=50)
radiobutton4.place(x=10, y=70)
radiobutton5.place(x=10, y=90)
radiobutton6.place(x=10, y=110)

root.mainloop()