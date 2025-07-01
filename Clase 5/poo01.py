class Alumno:

    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def __str__(self):
        return f"{self.nombre} ({self.nota})"
    
    def __eq__(self, other):
        return self.nota == other.nota and self.nombre == other.nombre
    
    def imprimir(self):
        return f"Nombre: {self.nombre} \nNota:{self.nota}"

    def resultado(self):
        if self.nota < 5:
            print("El alumno NO aprobó")
        else:
            print("El alumno ha aprobado")
            
pepe = Alumno("Pepe", 4)  
jose = Alumno("Pepe", 4)         
ana = Alumno("Ana", 8)

"""
print(f"El objeto pepe es {pepe.imprimir()}")
print(f"El objeto ana es {ana}")

pepe.resultado()
ana.resultado()

print(ana.nota, ana.nombre)
"""

if pepe == jose:
    print("Son iguales")