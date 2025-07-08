from peewee import *

# Conexión a la base SQLite (archivo local)
#db = SqliteDatabase('usuarios.db')

db = MySQLDatabase('movies', host='localhost', port=3306, user='root', password='EducacionIT')

# Definir el modelo
class Usuario(Model):
    nombre = CharField()
    email = CharField()

    class Meta:
        database = db

# Crear la tabla
db.connect()
db.create_tables([Usuario])

# ------------------------
# INSERT
Usuario.create(nombre="Juan Pérez", email="juan@example.com")
Usuario.create(nombre="Ana Gómez", email="ana@example.com")
Usuario.create(nombre="Pedro Sanchez", email="pes@example.com")
Usuario.create(nombre="Maria Rodriguez", email="mar@example.com")
Usuario.create(nombre="Juana Rodriguez", email="jur@example.com")
Usuario.create(nombre="Juan Pablo Perez", email="jpr@example.com")

# ------------------------
# SELECT (todos)
print("\n📋 Todos los usuarios:")
for u in Usuario.select():
    print(f"{u.id}: {u.nombre} <{u.email}>")

# ------------------------
# UPDATE
juan = Usuario.get(Usuario.nombre == "Juan Pérez")
juan.email = "juan.perez@nuevo.com"
juan.save()

# ------------------------
# SELECT con filtro
print("\n🔍 Usuarios que contienen 'Juan':")
query = Usuario.select().where(Usuario.nombre.contains("Juan"))
for u in query:
    print(f"{u.id}: {u.nombre} <{u.email}>")

# ------------------------
# DELETE
ana = Usuario.get(Usuario.nombre == "Ana Gómez")
ana.delete_instance()

# ------------------------
# SELECT final
print("\n📋 Usuarios después de eliminar a Ana:")
for u in Usuario.select():
    print(f"{u.id}: {u.nombre} <{u.email}>")

# Cerrar la conexión
db.close()
