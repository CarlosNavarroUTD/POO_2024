import os
movies=[]
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



print(movies)

i=True
while i:
    os.system("Clear")
    print(f"========== \n WachaMovies \n=============")
    print("1.- Añadir")
    print("2.- Remover")
    print("3.- Consultar")
    print("5.- Salir")
    opcion= input("Elige una opción ").upper()

    if opcion=="1" or opcion== "añadir":
        addMovie(movie)
movie=input("Nombre de pelicula: ")

