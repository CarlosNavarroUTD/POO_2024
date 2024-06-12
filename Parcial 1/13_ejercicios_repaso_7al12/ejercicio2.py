"""
Escribir un programa  que añada valores a una lista mientras que su longitud sea menor a 120, y luego mostrar la lista: Usar un while y for
"""

lista=[]
#ItemtoAdd=input("Escriba algo para agregar a la lista")
#lista.append(ItemtoAdd)
contador=0
while len(lista) < 120:
    contador+=1
    lista.append(contador)
for i in lista:
    print(i)