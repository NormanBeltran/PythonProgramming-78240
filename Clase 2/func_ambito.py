def funcion():
    a = 10
    b = 20

    x = 888
    y = 999
    print(f"Dentro de la funcion a = {a}  b = {b}")
    print(f"Dentro de la funcion x = {x}  y = {y}")
    return "Fin de funcion"

# Variables globales

x = 100
y = 200

print(funcion())
print(f"En el programa x = {x}  y = {y}")
