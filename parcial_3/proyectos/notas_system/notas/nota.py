from conexion import create_connection, close_connection

class Nota:
    def __init__(self, id=None, usuario_id=None, titulo=None, descripcion=None, fecha=None):
        self.id = id
        self.usuario_id = usuario_id
        self.titulo = titulo
        self.descripcion = descripcion
        self.fecha = fecha

    def create(self):
        cursor, connection = create_connection()
        try:
            query = """
                INSERT INTO notas (usuario_id, titulo, descripcion)
                VALUES (%s, %s, %s)
            """
            values = (self.usuario_id, self.titulo, self.descripcion)
            cursor.execute(query, values)
            connection.commit()
            print("Nota creada con éxito")
        except Exception as e:
            print(f"Error al crear nota: {e}")
        finally:
            close_connection(connection, cursor)

    def read(self):
        cursor, connection = create_connection()
        try:
            query = "SELECT * FROM notas WHERE id = %s"
            cursor.execute(query, (self.id,))
            result = cursor.fetchone()
            if result:
                self.id, self.usuario_id, self.titulo, self.descripcion, self.fecha = result
            return result
        except Exception as e:
            print(f"Error al leer nota: {e}")
        finally:
            close_connection(connection, cursor)

    def update(self):
        cursor, connection = create_connection()
        try:
            query = """
                UPDATE notas
                SET usuario_id = %s, titulo = %s, descripcion = %s
                WHERE id = %s
            """
            values = (self.usuario_id, self.titulo, self.descripcion, self.id)
            cursor.execute(query, values)
            connection.commit()
            print("Nota actualizada con éxito")
        except Exception as e:
            print(f"Error al actualizar nota: {e}")
        finally:
            close_connection(connection, cursor)

    def delete(self):
        cursor, connection = create_connection()
        try:
            query = "DELETE FROM notas WHERE id = %s"
            cursor.execute(query, (self.id,))
            connection.commit()
            print("Nota eliminada con éxito")
        except Exception as e:
            print(f"Error al eliminar nota: {e}")
        finally:
            close_connection(connection, cursor)

    @staticmethod
    def get_all():
        cursor, connection = create_connection()
        try:
            query = "SELECT * FROM notas"
            cursor.execute(query)
            return cursor.fetchall()
        except Exception as e:
            print(f"Error al obtener notas: {e}")
        finally:
            close_connection(connection, cursor)


    @staticmethod
    def get_by_usuario_id(usuario_id):
        cursor, connection = create_connection()
        try:
            query = "SELECT * FROM notas WHERE usuario_id = %s"
            cursor.execute(query, (usuario_id,))
            return cursor.fetchall()
        except Exception as e:
            print(f"Error al obtener notas por usuario_id: {e}")
        finally:
            close_connection(connection, cursor)
