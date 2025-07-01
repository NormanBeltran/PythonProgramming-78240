import os

print(os.listdir("..\Clase 4"))
print(os.getcwd())

if os.path.exists("..\Clase 4"):
    print("El directorio existe")

#os.mkdir("EJEMPLO")    
#os.rmdir("EJEMPLO") 

#os.system("calc")

os.system("cls")
print(os.name)