from usuarios.usuario import Usuario
from notas.nota import Nota
import getpass
from funciones import borrarPantalla, esperarTecla, hash_password

def menu_principal():
    while True:
        borrarPantalla()
        print("""
      .::  Menu Principal ::. 
          1.- Registro
          2.- Login
          3.- Salir 
          """)
        opcion = input("\t Elige una opción: ")

        if opcion == '1':
            borrarPantalla()
            print("\n \t ..:: Registro en el Sistema ::..")
            nombre = input("\t ¿Cuál es tu nombre?: ")
            apellidos = input("\t ¿Cuáles son tus apellidos?: ")
            email = input("\t Ingresa tu email: ")
            password = getpass.getpass("\t Ingresa tu contraseña: ")
            encrypted_password = hash_password(password)
            
            usuario = Usuario(nombre=nombre, apellidos=apellidos, email=email, password=encrypted_password)
            usuario.create()
            esperarTecla()
        elif opcion == '2':
            borrarPantalla()
            print("\n \t ..:: Inicio de Sesión ::.. ")     
            email = input("\t Ingresa tu E-mail: ")
            password = getpass.getpass("\t Ingresa tu Contraseña: ")
            encrypted_password = hash_password(password)

            usuario = Usuario(email=email, password=encrypted_password)
            result = usuario.get_by_email(email)
            
            if result:
                id, nombre, apellidos, email, password, fecha = result
                print(f"\n \t Bienvenido {nombre} {apellidos}!")
                menu_notas(id, nombre, apellidos)
            else:
                print("\n \t Usuario o contraseña incorrectos.")
            esperarTecla()
        elif opcion == '3':
            print("\n\t.. ¡Gracias! Adiós ...")
            break
        else:
            print("\n \t \t Opción no válida. Intenta de nuevo.")
            esperarTecla()

def menu_notas(usuario_id, nombre, apellidos):
    while True:
        borrarPantalla()
        print(f"\n \t \t \t Bienvenido {nombre} {apellidos}, has iniciado sesión ...")
        print("""
                  \n \t 
                      .::  Menu Notas ::. 
                  1.- Crear 
                  2.- Mostrar
                  3.- Cambiar
                  4.- Eliminar
                  5.- Salir 
                  """)
        opcion = input("\t\t Elige una opción: ")

        if opcion == '1':
            borrarPantalla()
            print(f"\n \t .:: Crear Nota ::. ")
            titulo = input("\t Titulo: ")
            descripcion = input("\t Descripción: ")
            
            nota = Nota(usuario_id=usuario_id, titulo=titulo, descripcion=descripcion)
            nota.create()
            esperarTecla()
        elif opcion == '2':
            borrarPantalla()
            print(f"\n \t .:: Mostrar Notas ::. ")
            notas = Nota.get_by_usuario_id(usuario_id)
            for nota in notas:
                print(f"\n\t Título: {nota[2]} | Descripción: {nota[3]}")
            esperarTecla()
        elif opcion == '3':
            borrarPantalla()
            print(f"\n \t .:: {nombre} {apellidos}, vamos a modificar una Nota ::. \n")
            id = input("\t ID de la nota a actualizar: ")
            nuevo_titulo = input("\t Nuevo título: ")
            nueva_descripcion = input("\t Nueva descripción: ")
            
            nota = Nota(id=id, titulo=nuevo_titulo, descripcion=nueva_descripcion)
            nota.update()
            esperarTecla()
        elif opcion == '4':
            borrarPantalla()
            print(f"\n \t .:: {nombre} {apellidos}, vamos a borrar una Nota ::. \n")
            id = input("\t ID de la nota a eliminar: ")
            
            nota = Nota(id=id)
            nota.delete()
            esperarTecla()
        elif opcion == '5':
            break
        else:
            print("\n \t \t Opción no válida. Intenta de nuevo.")
            esperarTecla()

if __name__ == "__main__":
    menu_principal()
