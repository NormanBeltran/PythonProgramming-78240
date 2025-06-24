cuadrado = lambda x: x**2

print(cuadrado(10))

nombres = ["jUan", " ricardo", "ANA", "aLberto  ", " maria", "Juana"]

print(list(map(lambda x: x.strip().capitalize(), nombres)))


potencia = lambda x,y: x**y
print(potencia(2,3))