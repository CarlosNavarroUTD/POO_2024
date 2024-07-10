import mysql.connector

try:
    #Conecctar con la BS mySQL

    conexion=mysql.connector.connect(
        host='localhost',
        user='root',
        password='2014'
    )


    
except:
    print("Ocurrio un problema con el servidor, por favor intenté más tarde.")

else:
    #verificar conexión

    if conexion.is_connected():
        print(f"Se creo la conexion con la DB exitosamente")
    else:
        print(f'Fallo la conexión con la BD')


    #Objeto para ejecutar instrucciones
    cursor=conexion.cursor()

    #Crear la BD desde python
    sql="Create database bd_python"
    cursor.execute(sql)

    #Verificar que se creo la DB
    if cursor:
        print("Se creo la BD exitosamente")


    #Mostrar las BD que ecosten en mi servidor
    cursor.execute("show databases")
    for x in cursor:
        print(x)