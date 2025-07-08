from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Definimos la base
Base = declarative_base()

# Definimos el modelo
class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    email = Column(String)

    def __repr__(self):
        return f"[Usuario(id={self.id}, nombre='{self.nombre}', email='{self.email}')]"

# Crear el engine y conectar a SQLite
engine = create_engine('sqlite:///ejemplo.db', echo=True)

# Crear las tablas
Base.metadata.create_all(engine)

# Crear la sesión
Session = sessionmaker(bind=engine)
session = Session()

# -----------------------------
# 🔹 INSERT (crear registros)
usuario1 = Usuario(nombre='Juan Pérez', email='juan@example.com')
usuario2 = Usuario(nombre='Ana Gómez', email='ana@example.com')
usuario3 = Usuario(nombre="Pedro Sanchez", email="pes@example.com")
usuario4 = Usuario(nombre="Maria Rodriguez", email="mar@example.com")
usuario5 = Usuario(nombre="Juana Rodriguez", email="jur@example.com")
usuario6 = Usuario(nombre="Juan Pablo Perez", email="jpr@example.com")
session.add_all([usuario1, usuario2, usuario3, usuario4, usuario5, usuario6])
session.commit()

# -----------------------------
# 🔹 SELECT (leer registros)
usuarios = session.query(Usuario).all()
print("Todos los usuarios:")
for u in usuarios:
    print(u)

# -----------------------------
# 🔹 UPDATE (actualizar registros)
usuario_a_modificar = session.query(Usuario).filter_by(nombre='Juan Pérez').first()
if usuario_a_modificar:
    usuario_a_modificar.email = 'juan.perez@example.com'
    session.commit()

# -----------------------------
# 🔹 DELETE (eliminar registros)
usuario_a_eliminar = session.query(Usuario).filter_by(nombre='Ana Gómez').first()
if usuario_a_eliminar:
    session.delete(usuario_a_eliminar)
    session.commit()

# -----------------------------
# 🔹 SELECT filtrado
usuarios = session.query(Usuario).filter(Usuario.nombre.like('%Juan%')).all()
print("Usuarios que contienen 'Juan':")
for u in usuarios:
    print(u)

# Cerrar la sesión
session.close()
