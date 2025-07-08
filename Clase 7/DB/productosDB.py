"""
Módulo de acceso a datos para productos.

Incluye funciones para agregar, actualizar, borrar, consultar y listar productos,
utilizando una base SQLite. Se espera una conexión abierta como argumento.
"""
from Clases import Productos
import sqlite3

def agregar(conn: sqlite3.Connection, producto: Productos) -> bool:
    """
    Agrega un nuevo producto a la base de datos.

    Args:
        conn: Conexión SQLite abierta.
        producto: Objeto Productos a insertar.

    Returns:
        True si se insertó correctamente, False si ocurrió un error.
    """
    # Defino valor a devolver
    valor = True

    # Intento grabar el registro
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO productos (nombre, precio) VALUES (?, ?);",
                       (producto.nombre, producto.precio))
        conn.commit()

    except Exception as e:
        valor = False
        print(f"Ocurrió un error al insertar el producto '{producto.nombre}' de $ {producto.precio:.2f}:\n", e)
    
    # Cargo la función
    return bool(valor)

def actualizar(conn: sqlite3.Connection, producto: Productos) -> bool:
    """
    Actualiza un producto existente.

    Args:
        conn: Conexión SQLite abierta.
        producto: Objeto Productos con ID existente.

    Returns:
        True si se actualizó correctamente, False si ocurrió un error.
    """
    # Defino valor a devolver
    valor = True

    # Intento grabar el registro
    try:
        cursor = conn.cursor()
        cursor.execute("UPDATE productos SET nombre = ?, precio = ? WHERE id = ?;",
                       (producto.nombre, producto.precio, producto.id))
        conn.commit()
        
    except Exception as e:
        valor = False
        print(f"Ocurrió un error al actualizar el producto '{producto}:'\n", e)
    
    # Cargo la función
    return bool(valor)

def borrar(conn: sqlite3.Connection, producto_id: int) -> bool:
    """
    Elimina un producto por su ID.

    Args:
        conn: Conexión SQLite abierta.
        producto_id: ID del producto a eliminar.

    Returns:
        True si se eliminó, False si ocurrió un error.
    """
    # Defino valor a devolver
    valor = True

    # Intento borrar el registro
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM productos WHERE id = ?;", 
                       (producto_id,))
        conn.commit()
        
    except Exception as e:
        valor = False
        print(f"Ocurrió un error al borrar el producto: '{producto_id}'\n", e)
    
    # Cargo la función
    return bool(valor)

def existe(conn: sqlite3.Connection, producto_id: int) -> bool:
    """
    Verifica si existe un producto por ID.

    Args:
        conn: Conexión SQLite abierta.
        producto_id: ID a verificar.

    Returns:
        True si existe, False si no.
    """
    # Cargo la función (redundante la sintaxis pero más legible)
    return True if _cargar(conn, producto_id) is not None else False

def _cargar(conn: sqlite3.Connection, producto_id: int) -> tuple | None:
    """
    Recupera un registro de producto como tupla (uso interno).

    Args:
        conn: Conexión SQLite abierta.
        producto_id: ID del producto.

    Returns:
        Tupla (id, nombre, precio) si existe, o None.
    """
    # Defino valor a devolver
    producto = None

    # Intento cargar el registro
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT id, nombre, precio FROM productos WHERE id = ?;", 
                       (producto_id,))
        fila = cursor.fetchone()

        if fila is not None:
            producto = fila
        
    except Exception as e:
        print(f"Ocurrió un error al recuperar el producto: '{producto_id}'\n", e)
    
    # Cargo la función
    return producto

def cargar(conn: sqlite3.Connection, id: int) -> Productos | None:
    """
    Carga un producto como objeto Productos.

    Args:
        conn: Conexión SQLite abierta.
        id: ID del producto.

    Returns:
        Objeto Productos o None si no existe.
    """
    # Defino valor a devolver
    producto = None

    # Intento recuperar datos
    registro = _cargar(conn, id)

    # Si recuperó datos lo cargo al registro a devolver
    if registro is not None:
        producto = Productos(id = registro[0], nombre = registro[1], precio = registro[2])

    # Devuelvo el objeto cargado
    return producto

def listar(conn: sqlite3.Connection, orden:str = "id", direccion:str = 'asc') -> list[Productos] | None:
    """
    Lista todos los productos ordenados por el campo y dirección indicados.

    Args:
        conn: Conexión SQLite abierta.
        orden: Campo por el que ordenar (id, nombre, precio).
        direccion: Dirección de ordenamiento (asc, desc).

    Returns:
        Lista de objetos Productos o None si hay error.
    """
    # Defino valor a devolver
    lista_productos = []

    # Verifico si pasé un orden válido
    if orden.lower() not in {"id", "nombre", "precio"}:
        orden = "id"

    # Verifico la dirección
    if direccion.lower() not in {"asc", "desc"}:
        direccion = "asc"  

    # Intento cargar la lista
    try:
        cursor = conn.cursor()
        cursor.execute(f"SELECT id, nombre, precio FROM productos ORDER BY {orden} {direccion};")
        filas = cursor.fetchall()

        # Recorro la lista
        for f in filas:
            # Creo el objeto
            producto = Productos(id = f[0], nombre = f[1], precio = f[2])

            # Agrego el objeto a la lista
            lista_productos.append(producto)
        
    except Exception as e:
        lista_productos = None
        print("Ocurrió un error al listar productos:\n", e)

    # Cargo la función
    return lista_productos
