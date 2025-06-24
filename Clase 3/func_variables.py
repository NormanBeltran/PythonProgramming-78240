def sumar(multiplo, *args):
    print(type(args))
    print(args)
    for idx, i in enumerate(args):
        print(f"el elemento en la posicion {idx} es {i}")


print(sumar(10, 2, 3, 4, 5, 6, 7, 8, 9, 10))
