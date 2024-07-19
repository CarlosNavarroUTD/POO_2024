from conexion import create_connection, close_connection

class Usuario:
    def __init__(self, id=None, nombre=None, apellidos=None, email=None, password=None, fecha=None):
        self.id = id
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.password = password
        self.fecha = fecha

    def create(self):
        cursor, connection = create_connection()
        try:
            query = """
                INSERT INTO usuarios (nombre, apellidos, email, password)
                VALUES (%s, %s, %s, %s)
            """
            values = (self.nombre, self.apellidos, self.email, self.password)
            cursor.execute(query, values)
            connection.commit()
            print("Usuario creado con éxito")
        except Exception as e:
            print(f"Error al crear usuario: {e}")
        finally:
            close_connection(connection, cursor)

    def read(self):
        cursor, connection = create_connection()
        try:
            query = "SELECT * FROM usuarios WHERE id = %s"
            cursor.execute(query, (self.id,))
            result = cursor.fetchone()
            if result:
                self.id, self.nombre, self.apellidos, self.email, self.password, self.fecha = result
            return result
        except Exception as e:
            print(f"Error al leer usuario: {e}")
        finally:
            close_connection(connection, cursor)

    def update(self):
        cursor, connection = create_connection()
        try:
            query = """
                UPDATE usuarios
                SET nombre = %s, apellidos = %s, email = %s, password = %s
                WHERE id = %s
            """
            values = (self.nombre, self.apellidos, self.email, self.password, self.id)
            cursor.execute(query, values)
            connection.commit()
            print("Usuario actualizado con éxito")
        except Exception as e:
            print(f"Error al actualizar usuario: {e}")
        finally:
            close_connection(connection, cursor)

    def delete(self):
        cursor, connection = create_connection()
        try:
            query = "DELETE FROM usuarios WHERE id = %s"
            cursor.execute(query, (self.id,))
            connection.commit()
            print("Usuario eliminado con éxito")
        except Exception as e:
            print(f"Error al eliminar usuario: {e}")
        finally:
            close_connection(connection, cursor)

    @staticmethod
    def get_all():
        cursor, connection = create_connection()
        try:
            query = "SELECT * FROM usuarios"
            cursor.execute(query)
            return cursor.fetchall()
        except Exception as e:
            print(f"Error al obtener usuarios: {e}")
        finally:
            close_connection(connection, cursor)

        

    @staticmethod
    def get_by_email(email):
        cursor, connection = create_connection()
        try:
            query = "SELECT * FROM usuarios WHERE email = %s"
            cursor.execute(query, (email,))
            return cursor.fetchone()
        except Exception as e:
            print(f"Error al obtener usuario por email: {e}")
        finally:
            close_connection(connection, cursor)
