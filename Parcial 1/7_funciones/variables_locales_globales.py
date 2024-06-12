""" n Python, las variables pueden ser locales o globales dependiendo de dónde se declaran y se usan. Comprender la diferencia entre estas dos es fundamental para el manejo correcto del estado y el flujo de un programa.

"""
# Variable global
x = 10  

def imprimir_x():
    print(x)  # Accede a la variable global

def modificar_x():
    global x
    x = 5  # Modifica la variable global

imprimir_x()  # Salida: 10
modificar_x()
imprimir_x()  # Salida: 5



#Variables locales
def funcion():
    y = 5  # Variable local
    print(y)  # Accede a la variable local

funcion()  # Salida: 5
# print(y)  # Esto causará un error porque y no está definida fuera de la función


#Ejemplo ambas
x = 10  # Variable global

def funcion():
    x = 5  # Variable local
    print(x)  # Salida: 5 (se accede a la variable local)

funcion()
print(x)  # Salida: 10 (se accede a la variable global)
