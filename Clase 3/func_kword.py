# Key word arguments

def verArgs(**kwargs):
    print(type(kwargs))
    print(kwargs)
    for key, value in kwargs.items():
        print(f"{key} = {value}")

verArgs(nombre="Juan", apellido="Perez", edad=30, ciudad="Buenos Aires", pais="Argentina", profesion="Programador")        