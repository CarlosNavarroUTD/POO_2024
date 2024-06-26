#Los errores de ejecución en un lenguaje de programación se presenta cuadndo existen una anomalia dentro de la ejeución del código lo cual provoca que se dentenga la ejecución del mismo, con el control y manejo de excepciones será posible minimizar o evitar la interrupción del programa debido a una excepción


#Ejemplo 1: Cuando una variable no se genera
try:
    nombre=input("Introduce el nombre completo de una persona: ")#Si no se ingresa ningun valor, la variable nombre_usuario nunca se genera
    if len(nombre)>0:
        nombre_usuario="El nombre completo del usuario es: "+nombre

    print(nombre_usuario)
except:
    print("Es necesario ingresar un nombre, verifique por favor...")
    

x=3+4
print("El valor de x es: "+ str(x))


#==============
#Ejemplo 2: cuando se solicita un número y se ingresa otra cosa
#==============


try:
    numero=int(input("Ingrese un entero: "))
    if numero > 0:
        print("Soy un numero entero positivo")

    elif numero==0:
        print("Soy un número entero neutro")

    else:
        print("Soy un nupero entero negativo")
except ValueError:
    print("Introduce un valor númerico entero")


#============
#Ejemplo 3 Genera multiples excepciones 
#=============

try:
    numero=int(input("Introduce un número: "))
    print("El cuadrado del número es: "+ str(numero*numero))
except ValueError:
    print("Introduce un valor numérico entero")
except TypeError:
    print("Se debe convertir el número a entero")
else:
    print("No se presentaron errores de ejecución")
finally:
    print("Termino la excepción")