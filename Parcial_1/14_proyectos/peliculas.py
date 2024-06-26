import os
movies=["movie1"]
def esperarTecla():
  print("Oprima cualquier tecla para continuar ...")
  input()

def addMovie(movie):
    movies.append(movie)

def delMovie(movie):
    movies.remove(movie)
    print

def readMovie(movie):
    for i in movies:
        if movie in movies:
            print(f"{movies.index(i)+1} .-{i}")

def UpdateMovie(movie):
    if movie in movies:
        actualizar_peliculas[peliculas] = peliculas
    else:
        print(f"La clave '{peliculas}' no existe en el diccionario.")

def deleteAll(movie):
    movies.clear()
    print(movies)
    esperarTecla()


i=True
while i:
    os.system("clear")
    print(f"========== \n WachaMovies \n=============")
    print("1.- Añadir")
    print("2.- Remover")
    print("3.- Buscar")
    print("4.- actualizar")
    print("5.- Vaciar")
    print("6.- Salir")
    opcion= input("Elige una opción ").upper()

    if opcion=="1" or opcion== "añadir":
        movie=input("Nombre de pelicula: ")
        addMovie(movie)
    
    if opcion=="2" or opcion== "remover":
        movie=input("Pelicula a borrar: ")
        if movie in movies:
            delMovie(movie)
            print("Pelicula Borrada")
            esperarTecla()
        else:
            print("Pelicula no encontrada")
            esperarTecla()

    if opcion=="3" or opcion== "Buscar":
        movie=input("Pelicula a buscar: ")
        readMovie(movie)
        esperarTecla()

    if opcion=="4" or opcion=="Actualizar":
        movie=input("Pelicula a actualizar: ")
        UpdateMovie(movie)
        esperarTecla()

    if opcion=="5" or opcion=="Eliminar":
        deleteAll()

print(movies)
esperarTecla()