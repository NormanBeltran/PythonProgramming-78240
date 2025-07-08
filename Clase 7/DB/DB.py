"""
Módulo de conexión y preparación de base de datos SQLite.

Funciones:
- abrir_db(base): Abre o crea una base de datos SQLite.
- verificar_tablas(conn): Verifica la existencia de las tablas necesarias y las crea si no existen.

Usado por el lanzador principal y los módulos funcionales para acceder a la base.
"""
import sqlite3

def abrir_db(base: str = "datos.db") -> sqlite3.Connection | None:
    """
    Abre una conexión a una base de datos SQLite.

    Si el archivo no existe, lo crea automáticamente.

    Args:
        base (str): Nombre del archivo de base de datos.

    Returns:
        sqlite3.Connection | None: Conexión a la base de datos o None si hubo error.
    """
    # Valor a devolver
    conn = None

    # Inteno abrir/crear la base de datos
    try:
        conn = sqlite3.connect(base)

    except Exception as e:
        print(f"Ocurrió un error al intentar abrir/crear la base de datos '{base}':\n", e)

    # Cargo la función
    return conn

def verificar_tablas(conn: sqlite3.Connection) -> bool:
    """
    Verifica si existen las tablas necesarias y las crea si no están presentes.

    Actualmente solo crea la tabla 'productos'. 
    Si falla en algún paso, devuelve False.

    Args:
        conn (sqlite3.Connection): Conexión abierta a la base de datos.

    Returns:
        bool: True si la operación fue exitosa, False si hubo error.
    """
    # Valor a devolver
    valor = True

    # Complemento de mensajes de error
    tabla = ""

    # Creo cursor
    cursor = conn.cursor()

    # Inteno crear las tablas si no existen
    try:
        # Creo las tablas
        tabla = "productos"
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS productos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                precio REAL NOT NULL
            )
            """)
    
        # Acá irían más execute si necesitase
        
        # Fuerzo a impactar los cambios
        conn.commit()
        
    except Exception as e:
        valor = False
        print(f"Ocurrió un error intentar crear la tabla '{tabla}':\n", e)

    # Cargo la función
    return bool(valor)