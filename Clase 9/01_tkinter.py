import tkinter as tk 
from tkinter import ttk


def multiplicar():
    numero1 = int(caja1.get())
    numero2 = int(caja2.get())
    resultado = numero1 * numero2

    resultado = tk.Label(text=f"El resultado es: {resultado}")
    resultado.config(font=("Arial", 18))
    resultado.place(x=350, y=300)

#______________________________________ Main
ventana = tk.Tk()
ventana.title("Bienvenidos a Tkinter")
ventana.geometry("800x400")

titulo = tk.Label(ventana, text="Aplicacion para multiplicar 2 numeros", font=("Arial", 20))
titulo.place(x=180, y=50)

label1 = tk.Label(text="Ingrese el primer numero")
label1.place(x=180, y=150)

label2 = tk.Label(text="Ingrese el segundo numero")
label2.place(x=180, y=200)

caja1 = tk.Entry()
caja1.place(x=350, y=150)

caja2 = tk.Entry()
caja2.place(x=350, y=200)

boton = tk.Button(text="Multiplicar", command=multiplicar)
boton.place(x=350, y=250)

ventana.mainloop()