def cuadrado(x):
    return x**2

def cubo(x):
    return x**3

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(list(map(cubo, numeros)))    