"""
Crear un programa para comprobar si una lista esta vacia y si esta vacia llenarla con 
 palabras o frases hasta que el usuario asi lo crea conveniente, posteriormente imprimir 
 el contenido de la lista en mayusculas
"""
lista=[]
list_len = len(lista)
if list_len==0:
    print("La lista esta vacia")
    try:
        i=True
        while i:

            print("Desea agregar un elemento?")
            print("1 - si")
            print("2 - no")
            ask=input().upper()
            if ask == "SI" or ask=="1":
                wordAdd= input("Escriba para agregar: ")
                lista.append(wordAdd)
                list_len = len(lista)
                print("Total de elementos en lista: ",list_len)

            elif ask=="2" or ask=="NO":
                i=False
                list_len = len(lista)
                print("Total de elementos en lista: ",list_len)
                for a in lista:
                    print(a.upper())
            else:
                print("Intente de nuevo...")
    except:
        print("Err")