import mysql.connector
from mysql.connector import errorcode

# Configuración de la conexión
# Configuración de la conexión
config = {
    'user': 'root',
    'password': '2014',
    'host': 'localhost',
    'database': 'bd_notas',
    'charset': 'utf8mb4',
    'collation': 'utf8mb4_general_ci'
}

# Función para obtener la conexión a la base de datos
def obtener_conexion():
    try:
        conn = mysql.connector.connect(**config)
        return conn
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error en el usuario o contraseña")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("La base de datos no existe")
        else:
            print(err)
        return None

# Función para cerrar la conexión a la base de datos
def cerrar_conexion(conn):
    if conn:
        conn.close()
