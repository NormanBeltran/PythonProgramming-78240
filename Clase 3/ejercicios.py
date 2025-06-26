""""
Resolver:

1. Data una lista de ausentes del mes, crear un diccionario por comprension, que tenga
como clave la persona ausente, y como valor la cantidad de ausencias que tuvo

Ej: ["ANA", "MARIA", "JOSE, "PEDRO", "LUCAS", "ANA", "ANA", "MARIA","MARIA","MARIA","MARIA","MARIA",]

{"ANA": 3, "MARIA": 5, "JOSE": 1, "PEDRO": 1, "LUCAS": 1}

2. Crear una lista por comprension con la serie de Fibonacci de n numeros

n = 10
[0,1,1,2,3,5,8,13,21,34]



nombres = ["ANA", "JOSE", "PEDRO", "LUCAS", "ANA", "ANA", "MARIA", "MARIA", "MARIA", "MARIA", "MARIA", "MARIA"]
resumen = {nombre: nombres.count(nombre) for nombre in set(nombres)}

print(resumen)
"""

fibo = [0, 1]
cantidad = 10
[fibo.append(fibo[-1] + fibo[-2]) for _ in range(cantidad - 2)]

print(fibo)