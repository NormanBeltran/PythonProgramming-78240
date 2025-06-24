"""
try:
    numero = int(input("Digite un número entero: "))
    print("El número es: ", numero)
except ValueError:
    print("Error: Debe ingresar un número entero válido.")   
"""

try:     
    a = int("AAA")
except Exception as e:
    print("Error: ", e)    