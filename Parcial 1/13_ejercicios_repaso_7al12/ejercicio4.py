"""
 Crear un script que tenga 4 variables, una lista, una cadena, un entero y un logico,  
  y que imprima un mensaje de acuerdo al tipo de dato de cada variable. Usar funciones

"""

def DataType(i):
    return type(i)
cadena="cadena"
entero=1
logico=True
lista2=[cadena, entero, logico]
#print(lista2)
#lista=["cadena", 1, True]
print(DataType(lista2))
for i in lista2:
    print(DataType(i))