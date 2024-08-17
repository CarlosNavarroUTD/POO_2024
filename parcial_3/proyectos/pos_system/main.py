import tkinter as tk
import datetime
from tkinter import messagebox, ttk, simpledialog
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
        tk.Label(self.frame, text="Formulario para Realizar Ticket").grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        tk.Label(self.frame, text="Buscar producto:").grid(row=1, column=0, padx=10, pady=10)
        entry_busqueda = tk.Entry(self.frame)
        entry_busqueda.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(self.frame, text="Tipo de Pago:").grid(row=1, column=2, padx=10, pady=10)
        entry_tipo_pago = tk.Entry(self.frame)
        entry_tipo_pago.grid(row=1, column=3, padx=10, pady=10)

        # Crear un Treeview para mostrar los resultados de la búsqueda
        tree_busqueda = ttk.Treeview(self.frame, columns=('ID', 'Nombre', 'Precio', 'Stock'), show='headings', height=5)
        tree_busqueda.heading('ID', text='ID')
        tree_busqueda.heading('Nombre', text='Nombre')
        tree_busqueda.heading('Precio', text='Precio')
        tree_busqueda.heading('Stock', text='Stock')
        tree_busqueda.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        # Crear un Treeview para mostrar los productos seleccionados
        tree_seleccionados = ttk.Treeview(self.frame, columns=('ID', 'Nombre', 'Precio', 'Cantidad', 'Subtotal'), show='headings', height=5)
        tree_seleccionados.heading('ID', text='ID')
        tree_seleccionados.heading('Nombre', text='Nombre')
        tree_seleccionados.heading('Precio', text='Precio')
        tree_seleccionados.heading('Cantidad', text='Cantidad')
        tree_seleccionados.heading('Subtotal', text='Subtotal')
        tree_seleccionados.grid(row=2, column=2, columnspan=2, padx=10, pady=10)

        def buscar_producto(event):
            busqueda = entry_busqueda.get()
            if len(busqueda) >= 3:
                # Limpiar resultados anteriores
                for i in tree_busqueda.get_children():
                    tree_busqueda.delete(i)
                
                # Buscar por nombre
                productos = Producto.buscar_productos_por_nombre(busqueda)
                
                # Si no se encuentra por nombre, buscar por código de barras
                if not productos:
                    producto = Producto.buscar_productos_por_codigo_barras(busqueda)
                    if producto:
                        productos = [producto]
                
                # Mostrar resultados en el Treeview
                for producto in productos:
                    tree_busqueda.insert('', 'end', values=(producto.id, producto.nombre, producto.precio_venta, producto.stock))

        entry_busqueda.bind('<KeyRelease>', buscar_producto)

        def seleccionar_producto():
            seleccion = tree_busqueda.selection()
            if not seleccion:
                messagebox.showerror("Error", "Por favor, seleccione un producto")
                return
            
            producto_id, nombre, precio, _ = tree_busqueda.item(seleccion[0])['values']
            
            # Pedir cantidad
            cantidad = simpledialog.askinteger("Cantidad", f"Ingrese la cantidad para {nombre}:", parent=self.frame)
            if cantidad is None or cantidad <= 0:
                return

            subtotal = cantidad * float(precio)
            tree_seleccionados.insert('', 'end', values=(producto_id, nombre, precio, cantidad, subtotal))

        tk.Button(self.frame, text="Seleccionar Producto", command=seleccionar_producto).grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        def realizar_ticket():
            if not tree_seleccionados.get_children():
                messagebox.showerror("Error", "No hay productos seleccionados")
                return

            tipo_pago = entry_tipo_pago.get()
            if not tipo_pago:
                messagebox.showerror("Error", "Por favor, ingrese el tipo de pago")
                return

            total = sum(float(tree_seleccionados.item(item)['values'][4]) for item in tree_seleccionados.get_children())
            ticket_id = Ticket.crear_ticket(fecha=datetime.datetime.now(), total=total, tipo_pago=tipo_pago)

            for item in tree_seleccionados.get_children():
                producto_id, _, precio_unitario, cantidad, _ = tree_seleccionados.item(item)['values']
                DetalleTicket.agregar_detalle_ticket(ticket_id, producto_id, cantidad, float(precio_unitario))

            messagebox.showinfo("Éxito", "Ticket realizado exitosamente")
            self.show_main_menu()  # Volver al menú principal después de crear el ticket

        tk.Button(self.frame, text="Realizar Ticket", command=realizar_ticket).grid(row=3, column=2, padx=10, pady=10)
        tk.Button(self.frame, text="Volver", command=self.show_main_menu).grid(row=3, column=3, padx=10, pady=10)



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
