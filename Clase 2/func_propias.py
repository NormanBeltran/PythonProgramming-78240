def sumar(a, b):
    return a + b

def potencia(b, e=2):
    return b ** e

print(sumar(2, 3))

print(potencia(2, 3))
print(potencia(2))

print("Cambio orden de argumentos:", potencia(e=3, b=2))


if __name__ == "__main__":
    pass