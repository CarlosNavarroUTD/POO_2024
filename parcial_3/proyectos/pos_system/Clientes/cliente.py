from conexion import create_connection, close_connection

class Cliente:
    def __init__(self, id, domicilio, telefono, correo, rfc):
        self.id = id
        self.domicilio = domicilio
        self.telefono = telefono
        self.correo = correo
        self.rfc = rfc

    @staticmethod
    def agregar_cliente(domicilio, telefono, correo, rfc):
        cursor, connection = create_connection()
        if cursor and connection:
            query = """
            INSERT INTO clientes (domicilio, telefono, correo, rfc)
            VALUES (%s, %s, %s, %s)
            """
            cursor.execute(query, (domicilio, telefono, correo, rfc))
            connection.commit()

            id_cliente = cursor.lastrowid
            nuevo_cliente = Cliente(id_cliente, domicilio, telefono, correo, rfc)
            print("Cliente agregado exitosamente.")
            close_connection(connection, cursor)
            return nuevo_cliente
        else:
            print("No se pudo establecer la conexión con la base de datos.")
            return None

    @staticmethod
    def obtener_cliente_por_id(id_cliente):
        cursor, connection = create_connection()
        if cursor and connection:
            query = "SELECT id, domicilio, telefono, correo, rfc FROM clientes WHERE id = %s"
            cursor.execute(query, (id_cliente,))
            cliente_data = cursor.fetchone()
            close_connection(connection, cursor)
            if cliente_data:
                return Cliente(*cliente_data)
            else:
                print("Cliente no encontrado.")
                return None
        else:
            print("No se pudo establecer la conexión con la base de datos.")
            return None
