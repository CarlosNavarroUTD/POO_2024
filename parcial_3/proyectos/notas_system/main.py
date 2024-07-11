from clases import Usuario, Nota

def menu_principal():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Gestionar Usuarios")
        print("2. Gestionar Notas")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            menu_usuarios()
        elif opcion == "2":
            menu_notas()
        elif opcion == "3":
            print("Gracias por usar el sistema. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def menu_usuarios():
    while True:
        print("\n--- Gestión de Usuarios ---")
        print("1. Crear Usuario")
        print("2. Ver Usuario")
        print("3. Ver Todos los Usuarios")
        print("4. Actualizar Usuario")
        print("5. Eliminar Usuario")
        print("6. Volver al Menú Principal")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            crear_usuario()
        elif opcion == "2":
            ver_usuario()
        elif opcion == "3":
            ver_todos_usuarios()
        elif opcion == "4":
            actualizar_usuario()
        elif opcion == "5":
            eliminar_usuario()
        elif opcion == "6":
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def menu_notas():
    while True:
        print("\n--- Gestión de Notas ---")
        print("1. Crear Nota")
        print("2. Ver Nota")
        print("3. Ver Notas de Usuario")
        print("4. Actualizar Nota")
        print("5. Eliminar Nota")
        print("6. Volver al Menú Principal")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            crear_nota()
        elif opcion == "2":
            ver_nota()
        elif opcion == "3":
            ver_notas_usuario()
        elif opcion == "4":
            actualizar_nota()
        elif opcion == "5":
            eliminar_nota()
        elif opcion == "6":
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def crear_usuario():
    nombre = input("Ingrese el nombre: ")
    apellidos = input("Ingrese los apellidos: ")
    email = input("Ingrese el email: ")
    password = input("Ingrese la contraseña: ")
    
    id = Usuario.crear(nombre, apellidos, email, password)
    if id:
        print(f"Usuario creado con éxito. ID: {id}")
    else:
        print("Error al crear el usuario.")

def ver_usuario():
    id = int(input("Ingrese el ID del usuario: "))
    usuario = Usuario.obtener_por_id(id)
    if usuario:
        print(f"ID: {usuario.id}")
        print(f"Nombre: {usuario.nombre}")
        print(f"Apellidos: {usuario.apellidos}")
        print(f"Email: {usuario.email}")
        print(f"Fecha: {usuario.fecha}")
    else:
        print("Usuario no encontrado.")

def ver_todos_usuarios():
    usuarios = Usuario.obtener_todos()
    if usuarios:
        for usuario in usuarios:
            print(f"ID: {usuario.id}, Nombre: {usuario.nombre} {usuario.apellidos}, Email: {usuario.email}")
    else:
        print("No hay usuarios registrados.")

def actualizar_usuario():
    id = int(input("Ingrese el ID del usuario a actualizar: "))
    usuario = Usuario.obtener_por_id(id)
    if usuario:
        usuario.nombre = input(f"Nuevo nombre ({usuario.nombre}): ") or usuario.nombre
        usuario.apellidos = input(f"Nuevos apellidos ({usuario.apellidos}): ") or usuario.apellidos
        usuario.email = input(f"Nuevo email ({usuario.email}): ") or usuario.email
        nueva_password = input("Nueva contraseña (dejar en blanco para no cambiar): ")
        if nueva_password:
            usuario.password = nueva_password
        
        if usuario.actualizar():
            print("Usuario actualizado con éxito.")
        else:
            print("Error al actualizar el usuario.")
    else:
        print("Usuario no encontrado.")

def eliminar_usuario():
    id = int(input("Ingrese el ID del usuario a eliminar: "))
    if Usuario.eliminar(id):
        print("Usuario eliminado con éxito.")
    else:
        print("Error al eliminar el usuario.")

def crear_nota():
    usuario_id = int(input("Ingrese el ID del usuario: "))
    titulo = input("Ingrese el título de la nota: ")
    descripcion = input("Ingrese la descripción de la nota: ")
    
    id = Nota.crear(usuario_id, titulo, descripcion)
    if id:
        print(f"Nota creada con éxito. ID: {id}")
    else:
        print("Error al crear la nota.")

def ver_nota():
    id = int(input("Ingrese el ID de la nota: "))
    nota = Nota.obtener_por_id(id)
    if nota:
        print(f"ID: {nota.id}")
        print(f"Usuario ID: {nota.usuario_id}")
        print(f"Título: {nota.titulo}")
        print(f"Descripción: {nota.descripcion}")
        print(f"Fecha: {nota.fecha}")
    else:
        print("Nota no encontrada.")

def ver_notas_usuario():
    usuario_id = int(input("Ingrese el ID del usuario: "))
    notas = Nota.obtener_por_usuario(usuario_id)
    if notas:
        for nota in notas:
            print(f"ID: {nota.id}, Título: {nota.titulo}, Fecha: {nota.fecha}")
    else:
        print("No hay notas para este usuario.")

def actualizar_nota():
    id = int(input("Ingrese el ID de la nota a actualizar: "))
    nota = Nota.obtener_por_id(id)
    if nota:
        nota.titulo = input(f"Nuevo título ({nota.titulo}): ") or nota.titulo
        nota.descripcion = input(f"Nueva descripción ({nota.descripcion}): ") or nota.descripcion
        
        if nota.actualizar():
            print("Nota actualizada con éxito.")
        else:
            print("Error al actualizar la nota.")
    else:
        print("Nota no encontrada.")

def eliminar_nota():
    id = int(input("Ingrese el ID de la nota a eliminar: "))
    if Nota.eliminar(id):
        print("Nota eliminada con éxito.")
    else:
        print("Error al eliminar la nota.")

if __name__ == "__main__":
    menu_principal()