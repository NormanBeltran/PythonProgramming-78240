"""
Conjuntos: { }

1. No son ordenados
2. Mutables (*)
3. Elementos unicos
4. No se puede modificar un elemento, pero si agregar o eliminar

"""

conjunto = { 1, 2, 3, 4, 5, "A", "B"}
conjunto2 = { 3, 4, 5, 6, 7, 8, "D", "E"}

print(type(conjunto))

#onjunto.add(11)
#conjunto.remove("A")
#conjunto.discard("Z")

print(conjunto)

# Operaciones con conjuntos

print(conjunto | conjunto2) # Union (pipe)

# Interseccion

print(conjunto & conjunto2) # Interseccion

# Diferencia

print(conjunto - conjunto2) # Diferencia
print(conjunto2 - conjunto) # Diferencia

# Diferencia simetrica

print(conjunto ^ conjunto2) # Diferencia simetrica


