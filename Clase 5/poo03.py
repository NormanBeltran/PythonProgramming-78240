class ClaseA:
    def __init__(self):
        self.a = 1

    def imprimir(self):
        print("ClaseA")

class ClaseB(ClaseA):
    def __init__(self):
        super().__init__()
        self.b = 2

    def imprimir(self):
        print("Estoy en ClaseB")

mi_obj = ClaseB()                
print(mi_obj.a, mi_obj.b)

mi_obj.imprimir()