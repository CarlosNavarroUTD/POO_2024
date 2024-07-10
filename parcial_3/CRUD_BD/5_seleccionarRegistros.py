from conexionBD import *
try:
    micursor=conexion.cursor()

    sql="select nombre,direccion,tel from clientes"
    micursor.execute(sql)
    resultado=micursor.fetchall()

    if len(resultado)>0:
        print(f"Registros de la tabla: {len(resultado)}")
        for x in resultado:
            print(x)
except:
    print("Ocurrio un problema con el servidor, por favor intenté más tarde.")
else:
    print("Registros consultados correctamemte")