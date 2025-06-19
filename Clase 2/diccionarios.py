"""
Diccionarios: { }

Elementos: clave: valor

1. No son ordenados
2. Mutables
3. Claves no se repiten / Valores podrian repetirse

"""

paises = {"Colombia": "Bogota", "Argentina": "Buenos Aires", "Peru": "Lima", "Chile": "Santiago"}

#print(paises["Chile"])

# Agregar elementos

paises["Brasil"] = "Brasilia"

# Modificar elementos

paises["Brasil"] = "Rio de Janeiro"

# Eliminar elementos

del paises["Chile"]
paises.pop("Argentina")

if "Ecuador" not in paises:
    print("El diccionario no contiene a Ecuador")
    
print(paises)