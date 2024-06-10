paises=["México", "USA", "Brasil", "Japon"]
numeros=[23, 100, 3.1416, 0.1]
varios=["hola", True, 100, 10.22]
#Ordenar cadenas/elementos
print(paises)
paises.sort()
print(paises)

#Ordenar números/elementos
print(numeros)
numeros.sort()
print(numeros)

#Insertar número/elemento
numeros.insert(len(numeros), 1000)
numeros.append(200)
print(numeros)


#eliminar elementos
numeros.pop(2)
print(numeros)
numeros.remove(100)
print(numeros)

#Buscar dentor de una lista
encontrar="Brasil" in paises
print(encontrar)


#Dar la vuelta
print(varios)
varios.reverse()
print(varios)

#Unir listas
print(paises)
paises.extend(numeros)
print(paises)

#Vaciar una lista
print(varios)
varios.clear()
print(varios) 