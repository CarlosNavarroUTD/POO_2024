"""
1.- 

 Hacer un programa que tenga una lista de 8 numeros enteros y realice lo siguiente: 

 a.- Recorrer la lista y mostrarla
 b.- hacer una funcion que recorra la lista de numeros y devuelva un string
 c.- ordenarla y mostrarla
 d.- mostrar su longitud
 e.- buscar algun elemento que el usuario pida por teclado
 """

#Generar lista
numeros=[8,7,6,5,4,3,2,1]

#recorrer lista
for i in numeros:
    print(str(i))

#ordenar lista
numeros.sort()
print(numeros)

#obtener longitud
longitud=len(numeros)
print(f'la longitud de la lista es: {longitud}')

#Buscar elemento del usuario
try:
    word_searched=int(input("Ingrese el número a buscar"))
    if word_searched in numeros:
        print(f'{word_searched} se encontro en la lista')
    else:
        print(f'{word_searched} no se encontro en la lista')
except:
    print("Error en ejecución")