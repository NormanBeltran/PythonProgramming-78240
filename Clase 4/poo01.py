class Alumno:
    def __init__(self, nombre, nota, edad=35):
        self.nombre = nombre
        self.nota = nota
        self.edad = edad

mario = Alumno("Mario", 9)
pedro = Alumno("Pedro", 8)


print(type(mario))
print(mario.nombre)
print(mario.nota)
print(mario.edad)

print(pedro.nombre)
print(pedro.nota)
print(pedro.edad)