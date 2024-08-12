import tkinter as tk
import datetime
from tkinter import messagebox
from Usuarios.usuario import Usuario
from Clientes.cliente import Cliente
from Empleados.empleado import Empleado
from Productos.producto import Producto 
from DetalleTicket.detalleticket import DetalleTicket 
from Tickets.ticket import Ticket


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Gestión")

        # Crear un contenedor para la pantalla de inicio de sesión
        self.frame = tk.Frame(root)
        self.frame.pack(pady=20, padx=20)

        # Pantalla de inicio de sesión
        self.show_login()

    def show_login(self):
        self.clear_content_frame()

        tk.Label(self.frame, text="Username:").grid(row=0, column=0, padx=10, pady=10)
        tk.Label(self.frame, text="Contraseña:").grid(row=1, column=0, padx=10, pady=10)

        entry_username = tk.Entry(self.frame)
        entry_password = tk.Entry(self.frame, show="*")

        entry_username.grid(row=0, column=1, padx=10, pady=10)
        entry_password.grid(row=1, column=1, padx=10, pady=10)

        def login():
            username = entry_username.get()
            contrasena = entry_password.get()
            usuario = Usuario.iniciar_sesion(username, contrasena)
            if usuario:
                messagebox.showinfo("Éxito", f"Bienvenido {usuario.nombre}")
                self.show_main_menu()  # Mostrar el menú principal tras iniciar sesión
            else:
                messagebox.showerror("Error", "Usuario o contraseña incorrectos")

        tk.Button(self.frame, text="Iniciar Sesión", command=login).grid(row=2, column=1, padx=10, pady=10)

    def show_main_menu(self):
        self.clear_content_frame()

        # Botones para las diferentes opciones del sistema
        tk.Button(self.frame, text="Realizar Ticket", command=self.show_ticket_form).grid(row=0, column=0, padx=10, pady=10)
        tk.Button(self.frame, text="Agregar Cliente", command=self.show_add_client).grid(row=0, column=1, padx=10, pady=10)
        tk.Button(self.frame, text="Agregar Producto", command=self.show_add_product).grid(row=1, column=0, padx=10, pady=10)
        tk.Button(self.frame, text="Cerrar Sesión", command=self.show_login).grid(row=1, column=1, padx=10, pady=10)

    
    def show_ticket_form(self):
        self.clear_content_frame()
        tk.Label(self.frame, text="Formulario para Realizar Ticket").grid(row=0, column=0, padx=10, pady=10)

        tk.Label(self.frame, text="Producto ID:").grid(row=1, column=0, padx=10, pady=10)
        tk.Label(self.frame, text="Cantidad:").grid(row=2, column=0, padx=10, pady=10)
        tk.Label(self.frame, text="Tipo de Pago:").grid(row=3, column=0, padx=10, pady=10)

        entry_producto_id = tk.Entry(self.frame)
        entry_cantidad = tk.Entry(self.frame)
        entry_tipo_pago = tk.Entry(self.frame)

        entry_producto_id.grid(row=1, column=1, padx=10, pady=10)
        entry_cantidad.grid(row=2, column=1, padx=10, pady=10)
        entry_tipo_pago.grid(row=3, column=1, padx=10, pady=10)

        def realizar_ticket():
            producto_id = int(entry_producto_id.get())
            cantidad = int(entry_cantidad.get())
            tipo_pago = entry_tipo_pago.get()

            producto = Producto.obtener_producto_por_id(producto_id)
            if not producto:
                messagebox.showerror("Error", "Producto no encontrado")
                return

            total = cantidad * producto.precio_venta
            ticket_id = Ticket.crear_ticket(fecha=datetime.now(), total=total, tipo_pago=tipo_pago)
            DetalleTicket.agregar_detalle_ticket(ticket_id, producto_id, cantidad, producto.precio_venta)

            messagebox.showinfo("Éxito", "Ticket realizado exitosamente")

        tk.Button(self.frame, text="Realizar Ticket", command=realizar_ticket).grid(row=4, column=1, padx=10, pady=10)
        tk.Button(self.frame, text="Volver", command=self.show_main_menu).grid(row=5, column=1, padx=10, pady=10)




    def show_add_client(self):
        self.clear_content_frame()

        tk.Label(self.frame, text="Domicilio:").grid(row=0, column=0, padx=10, pady=10)
        tk.Label(self.frame, text="Teléfono:").grid(row=1, column=0, padx=10, pady=10)
        tk.Label(self.frame, text="Correo:").grid(row=2, column=0, padx=10, pady=10)
        tk.Label(self.frame, text="RFC:").grid(row=3, column=0, padx=10, pady=10)

        entry_domicilio = tk.Entry(self.frame)
        entry_telefono = tk.Entry(self.frame)
        entry_correo = tk.Entry(self.frame)
        entry_rfc = tk.Entry(self.frame)

        entry_domicilio.grid(row=0, column=1, padx=10, pady=10)
        entry_telefono.grid(row=1, column=1, padx=10, pady=10)
        entry_correo.grid(row=2, column=1, padx=10, pady=10)
        entry_rfc.grid(row=3, column=1, padx=10, pady=10)

        def add_client():
            domicilio = entry_domicilio.get()
            telefono = entry_telefono.get()
            correo = entry_correo.get()
            rfc = entry_rfc.get()
            nuevo_cliente = Cliente.agregar_cliente(domicilio, telefono, correo, rfc)
            if nuevo_cliente:
                messagebox.showinfo("Éxito", "Cliente agregado exitosamente")
            else:
                messagebox.showerror("Error", "No se pudo agregar el cliente")

        tk.Button(self.frame, text="Agregar Cliente", command=add_client).grid(row=4, column=1, padx=10, pady=10)
        tk.Button(self.frame, text="Volver", command=self.show_main_menu).grid(row=5, column=1, padx=10, pady=10)

    def show_add_product(self):
        self.clear_content_frame()

        tk.Label(self.frame, text="Nombre del Producto:").grid(row=0, column=0, padx=10, pady=10)
        tk.Label(self.frame, text="Precio de Venta:").grid(row=1, column=0, padx=10, pady=10)
        tk.Label(self.frame, text="Precio de Compra:").grid(row=2, column=0, padx=10, pady=10)
        tk.Label(self.frame, text="Stock:").grid(row=3, column=0, padx=10, pady=10)
        tk.Label(self.frame, text="Código de Barras:").grid(row=4, column=0, padx=10, pady=10)
        tk.Label(self.frame, text="Unidad de Medida:").grid(row=5, column=0, padx=10, pady=10)

        entry_nombre = tk.Entry(self.frame)
        entry_precio_venta = tk.Entry(self.frame)
        entry_precio_compra = tk.Entry(self.frame)
        entry_stock = tk.Entry(self.frame)
        entry_codigo_barras = tk.Entry(self.frame)
        entry_unidad_medida = tk.Entry(self.frame)

        entry_nombre.grid(row=0, column=1, padx=10, pady=10)
        entry_precio_venta.grid(row=1, column=1, padx=10, pady=10)
        entry_precio_compra.grid(row=2, column=1, padx=10, pady=10)
        entry_stock.grid(row=3, column=1, padx=10, pady=10)
        entry_codigo_barras.grid(row=4, column=1, padx=10, pady=10)
        entry_unidad_medida.grid(row=5, column=1, padx=10, pady=10)

        def add_product():
            nombre = entry_nombre.get()
            precio_venta = entry_precio_venta.get()
            precio_compra = entry_precio_compra.get()
            stock = entry_stock.get()
            codigo_barras = entry_codigo_barras.get()
            unidad_medida = entry_unidad_medida.get()
            # Aquí agregarías el código para insertar el producto en la base de datos

            messagebox.showinfo("Éxito", "Producto agregado exitosamente")

        tk.Button(self.frame, text="Agregar Producto", command=add_product).grid(row=6, column=1, padx=10, pady=10)
        tk.Button(self.frame, text="Volver", command=self.show_main_menu).grid(row=7, column=1, padx=10, pady=10)

    def clear_content_frame(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
