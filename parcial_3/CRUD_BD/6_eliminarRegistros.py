from conexionBD import *
try:
    micursor=conexion.cursor()
    sql="delete from clientes where id=1"

    micursor.execute(sql)
    conexion.commit()

except:
    print("Ocurrio un problema con el servidor, por favor intenté más tarde.")
else:
    print("Registros eliminados correctamemte")