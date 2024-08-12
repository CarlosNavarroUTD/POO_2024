import datetime
from Usuarios.usuario import Usuario
from Clientes.cliente import Cliente
from Empleados.empleado import Empleado
from Productos.producto import Producto
from DetalleTicket.detalleticket import DetalleTicket
from Tickets.ticket import Ticket

def show_login():
    print("Iniciar sesión")
    username = input("Username: ")
    contrasena = input("Contraseña: ")
    usuario = Usuario.iniciar_sesion(username, contrasena)
    if usuario:
        print(f"Bienvenido {usuario.nombre}")
        show_main_menu()
    else:
        print("Usuario o contraseña incorrectos")
        show_login()

def show_main_menu():
    while True:
        print("\nMenú Principal")
        print("1. Realizar Ticket")
        print("2. Agregar Cliente")
        print("3. Agregar Producto")
        print("4. Cerrar Sesión")
        choice = input("Selecciona una opción: ")

        if choice == '1':
            show_ticket_form()
        elif choice == '2':
            show_add_client()
        elif choice == '3':
            show_add_product()
        elif choice == '4':
            show_login()
        else:
            print("Opción no válida")

def show_ticket_form():
    cart = []
    while True:
        # Solicitar al usuario el código de barras o nombre del producto
        identifier = input("Escribe código de barras o nombre del producto (o 'terminar' para finalizar la venta): ").strip()
        if identifier.lower() == 'terminar':
            break
        
        # Buscar el producto por nombre o código de barras
        productos = Producto.buscar_productos_por_nombre(identifier)
        if not productos:
            producto = Producto.buscar_productos_por_codigo_barras(identifier)
            if producto:
                productos = [producto]
        
        if productos:
            if len(productos) > 1:
                print("\nSe encontraron varios productos:")
                for i, p in enumerate(productos, 1):
                    print(f"{i}. {p.nombre} - Precio: {p.precio_venta} - Stock: {p.stock}")
                seleccion = int(input("Seleccione el número del producto deseado: ")) - 1
                producto = productos[seleccion]
            else:
                producto = productos[0]
            
            print(f"\nProducto encontrado:")
            print(f"Nombre: {producto.nombre}")
            print(f"Precio de venta: {producto.precio_venta}")
            print(f"Stock disponible: {producto.stock}")
            
            quantity = int(input("Escribe la cantidad (0 para no agregar): ").strip())
            
            if quantity > 0:
                if quantity <= producto.stock:
                    cart.append((producto, quantity))
                    print(f"Agregado al carrito: {quantity} x {producto.nombre}")
                else:
                    print(f"No hay suficiente stock para {producto.nombre}. Stock disponible: {producto.stock}")
        else:
            print("Producto no encontrado.")
        
        print("\n--- Continúa la búsqueda de productos ---")
    
    # Imprimir resumen de la venta
    if cart:
        print("\nResumen de la venta:")
        total_sale = 0
        for producto, quantity in cart:
            subtotal = quantity * producto.precio_venta
            total_sale += subtotal
            print(f"Producto: {producto.nombre}, Cantidad: {quantity}, Precio: {producto.precio_venta}, Subtotal: {subtotal}")
        print(f"Total de la venta: {total_sale}")
    else:
        print("No se agregaron productos al carrito.")
        


def show_add_client():
    print("\nAgregar Cliente")
    domicilio = input("Domicilio: ")
    telefono = input("Teléfono: ")
    correo = input("Correo: ")
    rfc = input("RFC: ")
    
    nuevo_cliente = Cliente.agregar_cliente(domicilio, telefono, correo, rfc)
    if nuevo_cliente:
        print("Cliente agregado exitosamente")
    else:
        print("No se pudo agregar el cliente")

def show_add_product():
    print("\nAgregar Producto")
    nombre = input("Nombre del Producto: ")
    precio_venta = float(input("Precio de Venta: "))
    precio_compra = float(input("Precio de Compra: "))
    stock = int(input("Stock: "))
    codigo_barras = input("Código de Barras: ")
    unidad_medida = input("Unidad de Medida: ")

    # Crear una instancia de Producto con los datos ingresados
    producto = Producto(id=None, nombre=nombre, precio_venta=precio_venta, 
                        precio_compra=precio_compra, stock=stock, 
                        codigo_barras=codigo_barras, unidad_medida=unidad_medida)
    
    # Insertar el nuevo producto en la base de datos
    producto.crear_producto()

    print("Producto agregado exitosamente")

if __name__ == "__main__":
    show_login()
