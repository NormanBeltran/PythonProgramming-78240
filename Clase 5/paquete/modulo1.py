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