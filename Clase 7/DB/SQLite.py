"""
Lanzador principal del sistema de gestión de productos.

Este script se encarga de:
- Abrir o crear la base de datos SQLite.
- Verificar y crear la estructura de tablas si es necesario.
- Ejecutar el flujo principal del módulo de productos.

Se puede invocar desde línea de comandos con un nombre opcional de base de datos:
    python SQLite.py productos.sqlite
"""
import sys
import DB as db
import Productos as main

# Obtengo el nombre de la base si fue pasado como argumento, sino uso el valor por defecto
# (omito argumento 0 que es el nombre del script)
nombre_base = sys.argv[1] if len(sys.argv) > 1 else "productos.sqlite"

# Abro la base de datos
conn = db.abrir_db(nombre_base)

# Verifico la apertura
if conn is None:
    print(f"Problemas para abrir/crear la base de datos '{nombre_base}'. Imposible continuar.")
    sys.exit()

# Verifico el estado de las tabla
if db.verificar_tablas(conn) == False:
    print("Problemas para crear/verificar estructura de tablas. Imposibe continuar.")
    sys.exit()

# Ejecuto la lógica principal
main.main_productos(conn)

# Cierro la conexión al final
conn.close()