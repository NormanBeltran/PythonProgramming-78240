import tkinter as tk
from tkinter import ttk


def btn_presionado():
    print("La opcion 1 es ", ckb_st1.get())
    print("La opcion 2 es ", ckb_st2.get())

ventana=tk.Tk()

ckb_st1 = tk.BooleanVar()
checkbutton = ttk.Checkbutton(ventana, text="Opción 1", variable=ckb_st1)
checkbutton.place(x=10, y=10)

ckb_st2 = tk.BooleanVar()
checkbutton2 = ttk.Checkbutton(ventana, text="Opción 2", variable=ckb_st2)
checkbutton2.place(x=10, y=30)

btn = ttk.Button(ventana, text="Presione aqui", command=btn_presionado)
btn.place(x=10, y=80)

ventana.mainloop()