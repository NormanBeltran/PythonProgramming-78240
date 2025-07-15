import requests
import json

def consultar():
    r = requests.get("http://localhost:7001/student")
    print(f"Status: {r.status_code} Respuesta:{r.json()}")

def consultar_uno(id):
    r = requests.get("http://localhost:7001/student/"+str(id))
    print(f"Status: {r.status_code} Respuesta:{r.json()}")

def crear(nombre, cursos):
    r = requests.post("http://localhost:7001/student", json={"name": nombre, "courses": cursos})
    print(f"Status: {r.status_code} Respuesta:{r.json()}")

def modificar(id, nombre, cursos):
    r = requests.put("http://localhost:7001/student/"+str(id), json={"name": nombre, "courses": cursos})
    print(f"Status: {r.status_code}")    

def borrar(id):
    r = requests.delete("http://localhost:7001/student/"+str(id))
    print(f"Status: {r.status_code} ")     
#_______________________________________________

#crear("Mario Gomez", 4)
#crear("Ana Rodriguez", 5)
#crear("Jose Alvarez", 10)
#crear("Juan Perez", 11)
#crear("Maria Fernandez", 12)
#modificar(9, "Juana Garcia", 100)
#borrar(9)
consultar()
#consultar_uno(8)