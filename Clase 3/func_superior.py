def cuadrado(x):
    return x**2

def cubo(x):
    return x**3

def funcion(f, lista):
    for i in lista:
        print(f(i))

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

funcion(cubo, numeros)