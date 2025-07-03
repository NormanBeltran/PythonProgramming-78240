import   sqlite3

def crear_tabla():
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS empleados (
            id INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL,
            salario REAL NOT NULL,
            depto TEXT NOT NULL,
            posicion TEXT NOT NULL,
            ingreso TEXT NOT NULL,
            edad NUMERIC NOT NULL
        )
        """
    )
    conn.commit()


def insertar():
    personas = ((1, "Jose",     50000, "Finanzas",     "Jefe", "2010-01-01", 30),
                (2, "Antonia", 100000, "RRHH",         "Empleado", "2012-01-01", 10),
                (3, "Pedro",   150000, "Sistemas",     "Supervisor", "2015-01-01", 40),
                (4, "Mariana",  75000, "Legales",      "Analista", "2013-01-01", 25),
                (5, "Marina",  200000, "Contabilidad", "Director", "2011-01-01", 45),
                (6, "Lucas",   125000, "Presidencia",  "Secretaria", "2012-01-01", 21))
    
    for nid, nombre, salario, depto, posicion, ingreso, edad in personas:
        cursor.execute(
            """
            INSERT INTO empleados (id, nombre, salario, depto, posicion, ingreso, edad)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (nid, nombre, salario, depto, posicion, ingreso, edad)
        )

    conn.commit()

def insertar_uno(nid, nombre, salario, depto, posicion, ingreso, edad):
    cursor.execute(
            """
            INSERT INTO empleados (id, nombre, salario, depto, posicion, ingreso, edad)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (nid, nombre, salario, depto, posicion, ingreso, edad)
        )

    conn.commit()    


def consultar():
    cursor.execute(
            """
            SELECT * FROM empleados
            """
        )    
    
    filas = cursor.fetchall()
    for fila in filas:
        print(fila)

def consultar_uno(nid):
    cursor.execute(
            """
            SELECT * FROM empleados WHERE id = ?;
            """,
            (nid,)
        )    
    
    fila = cursor.fetchone()
    print(fila)

def consultar_like(busqueda):
    cursor.execute(
            """
            SELECT * FROM empleados WHERE nombre LIKE ?;
            """,
            (f"%{busqueda}%",)
        )    
    
    filas = cursor.fetchall()
    for fila in filas:
        print(fila)

def borrar_uno(nid):
    cursor.execute(
            """
            DELETE FROM empleados WHERE id = ?;
            """,
            (nid,)
        )

    conn.commit()        


def actualizar(nid, salario):
    cursor.execute(
            f"""
            UPDATE empleados SET salario = {salario} WHERE id = {nid};
            """
        )

    conn.commit()
#___________________________________ Código Principal

# Conexión
conn = sqlite3.connect('empleados.db')

# Cursor
cursor = conn.cursor()

crear_tabla()
#insertar()
#insertar_uno(7, "Juan", 50000, "Finanzas", "Jefe", "2010-01-01", 30)

#consultar()
#consultar_uno(5)

#consultar_like("a")

#borrar_uno(7)
actualizar(1, 500000)
consultar()

# Cerrar la conexión
conn.close()