"""
Este módulo contiene las definiciones de todas las clases que representan
entidades del sistema, como productos, clientes, ventas, etc. Actualmente,
incluye la clase Productos, utilizada para almacenar y manipular información
básica de los artículos registrados.

Las clases definidas aquí son utilizadas por los módulos de acceso a datos
y la lógica de aplicación.
"""
class Productos:
    """
    Representa un producto con ID, nombre y precio.

    Attributes:
        id (int): Identificador único del producto.
        nombre (str): Nombre del producto (en mayúsculas y sin espacios).
        precio (float): Precio del producto.
    """
    def __init__(self,
                 id: int = 0,
                 nombre:str = "",
                 precio:float = 0.00
                ):
    
        self.id = int(id) if isinstance(id, int) else 0
        self.nombre = str(nombre).strip().upper() if nombre else ""
        self.precio = float(precio) if isinstance(precio, (int, float)) else 0.00

    def __str__(self):
        return f"Código {self.id:05d} - {self.nombre} $ {self.precio:.2f}"
