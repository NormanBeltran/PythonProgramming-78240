lista = [2000, 1920, 3000, 800, 500, 3400]
lst = ['a' , 'aba' , 'asd' , 'sdsds' , 'asdasdasfasf', 'asasa']

def cantidad_letras(palabra):
    return len(palabra)

print(sorted(lst, key=cantidad_letras))