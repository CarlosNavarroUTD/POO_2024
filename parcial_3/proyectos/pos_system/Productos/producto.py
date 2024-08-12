from conexion import create_connection, close_connection

class Producto:
    def __init__(self, id, nombre, precio_venta, precio_compra=None, stock=0, codigo_barras=None, unidad_medida=None):
        self.id = id
        self.nombre = nombre
        self.precio_venta = precio_venta
        self.precio_compra = precio_compra
        self.stock = stock
        self.codigo_barras = codigo_barras
        self.unidad_medida = unidad_medida

    @staticmethod
    def obtener_producto_por_id(producto_id):
        cursor, connection = create_connection()
        query = "SELECT * FROM productos WHERE id = %s"
        cursor.execute(query, (producto_id,))
        data = cursor.fetchone()
        close_connection(connection, cursor)
        return Producto(*data) if data else None

    @staticmethod
    def buscar_productos_por_nombre(nombre):
        cursor, connection = create_connection()
        query = "SELECT * FROM productos WHERE nombre LIKE %s"
        cursor.execute(query, ('%' + nombre + '%',))
        data = cursor.fetchall()
        close_connection(connection, cursor)
        return [Producto(*item) for item in data] if data else []

    @staticmethod
    def buscar_productos_por_codigo_barras(codigo_barras):
        cursor, connection = create_connection()
        query = "SELECT * FROM productos WHERE codigo_barras = %s"
        cursor.execute(query, (codigo_barras,))
        data = cursor.fetchone()
        close_connection(connection, cursor)
        return Producto(*data) if data else None
