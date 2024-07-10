from conexionBD import *
try:
    micursor=conexion.cursor()
    sql='"update clientes set tel="6632058150" where id="3"'

    micursor.execute(sql)
    conexion.commit()

except:
    print("Ocurrio un problema con el servidor, por favor intenté más tarde.")
else:
    print("Registros actualizados correctamemte")