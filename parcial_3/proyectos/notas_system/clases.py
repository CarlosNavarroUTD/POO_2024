from conexionDB import obtener_conexion, cerrar_conexion
from mysql.connector import Error
from datetime import date

class Usuario:
    def __init__(self, id=None, nombre=None, apellidos=None, email=None, password=None, fecha=None):
        self.id = id
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.password = password
        self.fecha = fecha if fecha else date.today()

    @staticmethod
    def crear(nombre, apellidos, email, password):
        conn = obtener_conexion()
        if conn:
            try:
                cursor = conn.cursor()
                sql = "INSERT INTO usuarios (nombre, apellidos, email, password, fecha) VALUES (%s, %s, %s, %s, %s)"
                valores = (nombre, apellidos, email, password, date.today())
                cursor.execute(sql, valores)
                conn.commit()
                return cursor.lastrowid
            except Error as e:
                print(f"Error al crear usuario: {e}")
            finally:
                if cursor:
                    cursor.close()
                cerrar_conexion(conn)
        return None

    @staticmethod
    def obtener_por_id(id):
        conn = obtener_conexion()
        if conn:
            try:
                cursor = conn.cursor(dictionary=True)
                cursor.execute("SELECT * FROM usuarios WHERE id = %s", (id,))
                usuario = cursor.fetchone()
                if usuario:
                    return Usuario(**usuario)
            except Error as e:
                print(f"Error al obtener usuario: {e}")
            finally:
                if cursor:
                    cursor.close()
                cerrar_conexion(conn)
        return None

    @staticmethod
    def obtener_todos():
        conn = obtener_conexion()
        if conn:
            try:
                cursor = conn.cursor(dictionary=True)
                cursor.execute("SELECT * FROM usuarios")
                usuarios = cursor.fetchall()
                return [Usuario(**u) for u in usuarios]
            except Error as e:
                print(f"Error al obtener usuarios: {e}")
            finally:
                if cursor:
                    cursor.close()
                cerrar_conexion(conn)
        return []

    def actualizar(self):
        conn = obtener_conexion()
        if conn:
            try:
                cursor = conn.cursor()
                sql = "UPDATE usuarios SET nombre = %s, apellidos = %s, email = %s, password = %s WHERE id = %s"
                valores = (self.nombre, self.apellidos, self.email, self.password, self.id)
                cursor.execute(sql, valores)
                conn.commit()
                return True
            except Error as e:
                print(f"Error al actualizar usuario: {e}")
            finally:
                if cursor:
                    cursor.close()
                cerrar_conexion(conn)
        return False

    @staticmethod
    def eliminar(id):
        conn = obtener_conexion()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute("DELETE FROM usuarios WHERE id = %s", (id,))
                conn.commit()
                return True
            except Error as e:
                print(f"Error al eliminar usuario: {e}")
            finally:
                if cursor:
                    cursor.close()
                cerrar_conexion(conn)
        return False

class Nota:
    def __init__(self, id=None, usuario_id=None, titulo=None, descripcion=None, fecha=None):
        self.id = id
        self.usuario_id = usuario_id
        self.titulo = titulo
        self.descripcion = descripcion
        self.fecha = fecha if fecha else date.today()

    @staticmethod
    def crear(usuario_id, titulo, descripcion):
        conn = obtener_conexion()
        if conn:
            try:
                cursor = conn.cursor()
                sql = "INSERT INTO notas (usuario_id, titulo, descripcion, fecha) VALUES (%s, %s, %s, %s)"
                valores = (usuario_id, titulo, descripcion, date.today())
                cursor.execute(sql, valores)
                conn.commit()
                return cursor.lastrowid
            except Error as e:
                print(f"Error al crear nota: {e}")
            finally:
                if cursor:
                    cursor.close()
                cerrar_conexion(conn)
        return None

    @staticmethod
    def obtener_por_id(id):
        conn = obtener_conexion()
        if conn:
            try:
                cursor = conn.cursor(dictionary=True)
                cursor.execute("SELECT * FROM notas WHERE id = %s", (id,))
                nota = cursor.fetchone()
                if nota:
                    return Nota(**nota)
            except Error as e:
                print(f"Error al obtener nota: {e}")
            finally:
                if cursor:
                    cursor.close()
                cerrar_conexion(conn)
        return None

    @staticmethod
    def obtener_por_usuario(usuario_id):
        conn = obtener_conexion()
        if conn:
            try:
                cursor = conn.cursor(dictionary=True)
                cursor.execute("SELECT * FROM notas WHERE usuario_id = %s", (usuario_id,))
                notas = cursor.fetchall()
                return [Nota(**n) for n in notas]
            except Error as e:
                print(f"Error al obtener notas: {e}")
            finally:
                if cursor:
                    cursor.close()
                cerrar_conexion(conn)
        return []

    def actualizar(self):
        conn = obtener_conexion()
        if conn:
            try:
                cursor = conn.cursor()
                sql = "UPDATE notas SET titulo = %s, descripcion = %s WHERE id = %s"
                valores = (self.titulo, self.descripcion, self.id)
                cursor.execute(sql, valores)
                conn.commit()
                return True
            except Error as e:
                print(f"Error al actualizar nota: {e}")
            finally:
                if cursor:
                    cursor.close()
                cerrar_conexion(conn)
        return False

    @staticmethod
    def eliminar(id):
        conn = obtener_conexion()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute("DELETE FROM notas WHERE id = %s", (id,))
                conn.commit()
                return True
            except Error as e:
                print(f"Error al eliminar nota: {e}")
            finally:
                if cursor:
                    cursor.close()
                cerrar_conexion(conn)
        return False