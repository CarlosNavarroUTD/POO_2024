import mysql.connector

#Conecctar con la BS mySQL
try:
    conexion=mysql.connector.connect(
        host='localhost',
        user='root',
        password='2014',
        database='bd_python'
    )

except:
    print("Ocurrio un problema con el servidor, por favor intenté más tarde.")
#verificar conexión

else:

    #Crear Tabla 
    sql='create table clientes (id int primary key auto_increment, name varchar(50), direccion varchar(50), telefono varchar (20));'

    micursor=conexion.cursor()
    micursor.execute(sql)
    if micursor:
        print(f"Tabla dentro de DB creada exitosamente")




