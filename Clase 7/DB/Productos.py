"""
Módulo principal para gestión de productos.

Ofrece una interfaz de línea de comandos para:
- Agregar productos a la base.
- Consultar productos por ID.
- Listar todos los productos.

Puede ser usado como módulo importable o ejecutado como script principal.
"""
import sqlite3, os, sys
import DB as db, productosDB as pdb
from Clases import Productos

def main_productos(conn: sqlite3.Connection):
    """
    Menú principal para interactuar con la base de productos.
    """
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("1. Agregar productos")
        print("2. Consultar")
        print("3. Ver productos")
        print("4. Salir")

        opcion = input("Ingrese su opción: ")

        if opcion == "1":
            agregar_producto(conn)

        elif opcion == "2":
            consultar_producto(conn)

        elif opcion == "3":
            listar_productos(conn)

        elif opcion == "4" or opcion == "0":
            print("Saliendo...")
            break

def agregar_producto(conn: sqlite3.Connection):
    """
    Permite ingresar un nuevo producto a la base.
    """    
    while True:
        os.system("cls" if os.name == "nt" else "clear")

        nombre = input("Ingrese el nombre del producto (vacio cancelar): ").strip()
        if nombre == "":
            break

        precio = input("Ingrese el precio del producto (0 para cancelar): ")
        try:
            precio = float(precio)
            if precio == 0:
                break

        except ValueError:
            print("El precio debe ser un número.")
            input("Presione Enter para continuar...")
            continue

        producto = Productos(nombre = nombre, precio = precio)

        if pdb.agregar(conn, producto):
            print("Se grabó el nuevo producto.")
            input("Presione Enter para continuar...")

def consultar_producto(conn: sqlite3.Connection):
    """
    Consulta un producto por su ID.
    """
    while True:
        os.system("cls" if os.name == "nt" else "clear")

        id = input("Ingrese el id del producto a consultar (0 para cancelar): ")
        try:
            id = int(id)
            if id == 0:
                break

        except ValueError:
            print("El id debe ser un número.")
            input("Presione Enter para continuar...")
            continue

        producto = pdb.cargar(conn, id)

        if producto is None:
            print("No se encontró el producto.")
            input("Presione Enter para continuar...")
            continue

        print(f"ID: {producto.id:05d}")
        print(f"Nombre: {producto.nombre}")
        print(f"Precio: {producto.precio:2f}")
        input("Presione Enter para continuar...")

def listar_productos(conn: sqlite3.Connection):
    """
    Lista todos los productos ordenados por ID (por defecto).
    """
    os.system("cls" if os.name == "nt" else "clear")
    print("ID".ljust(6), "Nombre".ljust(30), "Precio".rjust(15))

    for producto in pdb.listar(conn):
        print(f"{producto.id:05d}".ljust(6), producto.nombre.ljust(30), f"{producto.precio:.2f}".rjust(15))

    input("Presione Enter para continuar...")

# Verifico si viene de un principal o es el principal
if __name__ == "__main__":
    # Obtengo el nombre de la base si fue pasado como argumento, sino uso el valor por defecto
    # (omito argumento 0 que es el nombre del script)
    nombre_base = sys.argv[1] if len(sys.argv) > 1 else "productos.sqlite"
    conn = db.abrir_db(nombre_base)
    main_productos(conn)
    conn.close()
