"""
 Crear un script que tenga 4 variables, una lista, una cadena, un entero y un logico,  
  y que imprima un mensaje de acuerdo al tipo de dato de cada variable. Usar funciones

"""

def DataType(i):
    return type(i)
lista=["cadena", 1, True]
print(DataType(lista))
for i in lista:
    print(DataType(i))