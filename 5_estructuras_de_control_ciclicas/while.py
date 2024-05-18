#El while es una estructura de control repetitiva o ciclica que funciona con interaciones x veces siempre y cuando la condicion sea true

#sintaxis

#while condicion
#    bloque instrucciones


#Ejemplo 1 Crear un programa que imprima 5 veces el caracter @

contador=0
while contador <=5: 
    print("@")
    i+=1

#Ejemplo 2 Crear un programa que imprima los numeros del 1 al 5, los suma y los imprima al final

suma=0
contador=1
while contador<=5:
    print(contador)
    suma+=contador
    contador+=1
print(f"la suma es: {suma}")

#Ejamplo 3 crear un programa que solicite un numero entero y apartir 

numero=int(input("Ingrese un numero:"))


multi=0
i=1
while i<=10:
   multi=numero*i
   print(f"{numero} x{i} = {multi}")
   i+=1
