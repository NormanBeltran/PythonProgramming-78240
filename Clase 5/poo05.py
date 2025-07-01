class Figura:
    tipo = "Figura"
    __atributo_privado = "Soy un atributo inalcanzable desde fuera."
    def area(self):
        pass
    def perímetro(self):
        pass
    def __str__(self):
        pass

class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return (self.base * 2) + (self.altura * 2)

    def __str__(self):
        nombre =  "Rectangulo de base " + str(self.base) + " y altura " + str(self.altura)
        return nombre

class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado * self.lado

    def perimetro(self):
        return self.lado * 4

    def __str__(self):
        nombre = "Cuadrado de lado " + str(self.lado)
        return nombre
    
cua1 = Cuadrado(5)    
cua2 = Cuadrado(6)    
cua3 = Cuadrado(7)    
rec1 = Rectangulo(2, 3)
rec2 = Rectangulo(2, 4)
rec3 = Rectangulo(2, 5)

lista = [cua1, cua2, cua3, rec1, rec2, rec3]

for figura in lista:
    print(figura)
    print("Area: ", figura.area())
    print("Perimetro: ", figura.perimetro())
    print()