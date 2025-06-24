anios = [1800,1840,1871,1999,2000,2020,2021]

def bisiesto(anio):
    if (anio%400==0) or (anio%4==0 and anio%100!=0):
        return True
    return False

print(tuple(filter(bisiesto, anios)))