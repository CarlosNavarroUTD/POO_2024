"""Crear una lista y un diccionario con el contenido de esta tabla: 

  ACCION              TERROR        DEPORTES
  MAXIMA VELOCIDAD    LA MONJA       ESPN
  ARMA MORTAL 4       EL CONJURO     MAS DEPORTE
  RAPIDO Y FURIOSO I  LA MALDICION   ACCION


  imprimir la información"""
lista=[["Acción", "MAXIMA VELOCIDAD", "ARMA MORTAL 4","RAPIDO Y FURIOSO I"],
       ["TERROR", "LA MONJA", "EL CONJURO", "LA MALDICION"],
       ["DEPORTES", "ESPN", "MAS DEPORTE", "ACCION"]]

print(lista)

accion={"MAXIMA VELOCIDAD", "ARMA MORTAL 4","RAPIDO Y FURIOSO I"}
terror={"LA MONJA", "EL CONJURO", "LA MALDICION"}
deportes={"ESPN", "MAS DEPORTE", "ACCION"}
Diccionario={"ACCION": accion,
             "TERROR": terror,
             "DEPORTES": deportes
            }
print(Diccionario)