import mysql.connector

#Conecctar con la BS mySQL
try:
    conexion=mysql.connector.connect(
        host='localhost',
        user='root',
        password='2014',
        database='bd_python'
    )
except Exception as e:
    #print(f"Error: {e}")
    #print(f"Tipo de error: {type(e).__name__}")
    print("Ocurrio un problema con el servidor, por favor intenté más tarde.")

#Confirmar conexión exitosa
#else:
 #   print(f"Se creo la conexion con la DB exitosamente")