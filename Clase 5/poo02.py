class Empleado:

    tipo = "Empleado"

    def __init__(self, nombre, cargo, salario):
        self.__nombre = nombre
        self.__cargo = cargo
        self.__salario = salario

    def getSalario(self):
        return self.__salario

    def setSalario(self, nuevo_salario):
        self.__salario = nuevo_salario

    def __str__(self):
        return f"{self.__nombre} que trabaja como {self.__cargo} tiene un salario de {self.__salario}"
    

pepe = Empleado("Pepe", "Jefe", 1000000)    
mario = Empleado("Mario", "Administrativo", 2000000)  


pepe.setSalario(3000000)
print(pepe.getSalario())