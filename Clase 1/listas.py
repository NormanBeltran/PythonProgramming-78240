"""

Listas:

1. Orden (si hay indice)
2. Mutables 
3. Pueden tener repetidos


"""

lista = [1, ["A", "B", "C", "D"], 2, 3, 4, 5, 6, 7, 8, 99, 9, 10, 99]

"""
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
print(lista[4])
print(lista[5])
print(lista[6])
print(lista[7])
print(lista[8])
print(lista[9])

print(lista[-1])
print(lista[-2])
print(lista[-3])
print(lista[-4])
print(lista[-5])
print(lista[-6])
print(lista[-7])
print(lista[-8])
print(lista[-9])
print(lista[-10])
"""

# Agregar elementos a la lista
lista.append("Juan")
lista.insert(3, 99)

# Modificar elementos de la lista
lista[0] = "Hola"

# Eliminar elementos de la lista
lista.remove(99)
del lista[6] # elimina el elemento en el indice 6

print(lista)
print(lista[1][1])
