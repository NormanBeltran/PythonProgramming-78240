"""
with open("canciones.txt") as f:
    texto = f.read()
    print(texto)
"""

with open("canciones.txt") as f:
    linea = f.readline()
    while linea:
        print(f"Una linea es {linea}", end="")
        linea = f.readline()
