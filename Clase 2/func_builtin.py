nombres = ["Ana", "Juan", "María", "Pedro", "Luis", "Sofía", "Carlos"]
apellidos = ["Perez", "Gomez", "Alvarez", "Rodriguez", "Fernandez", "Artigas", "Bach"]
edades = [20, 25, 30, 35, 40, 45, 50]

for idx, nombre in enumerate(nombres, start=1):
    print(f"{idx}: {nombre}")

for nombre, apellido, edad in zip(nombres, apellidos, edades):
    print(f"{nombre} {apellido} {edad}")    