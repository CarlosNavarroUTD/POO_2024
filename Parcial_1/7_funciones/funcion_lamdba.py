"""
Las funciones lambda en Python son funciones anónimas, es decir, funciones que no tienen un nombre explícito. Son útiles para operaciones pequeñas y se definen utilizando la palabra clave lambda. La sintaxis general de una función lambda es:


"""

lambda argumentos: expresión

#Sumar 2 numeros
suma = lambda x, y: x + y
print(suma(3, 5))  # Salida: 8


#Filtrar una lista
lista = [1, 2, 3, 4, 5, 6]
pares = list(filter(lambda x: x % 2 == 0, lista))
print(pares)  # Salida: [2, 4, 6]

#Ordenar una lista de tuplas
lista_tuplas = [(1, 2), (3, 1), (5, 0)]
lista_tuplas.sort(key=lambda x: x[1])
print(lista_tuplas)  # Salida: [(5, 0), (3, 1), (1, 2)]
