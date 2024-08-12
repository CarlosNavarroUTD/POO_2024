import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Lista para almacenar los productos añadidos
productos = []

def vincular_cliente():
    nombre_codigo = entry_nombre_codigo.get()
    cantidad = entry_cantidad.get()
    tipo_pago = combo_tipo_pago.get()
    
    # Aquí puedes agregar el código para manejar la vinculación del cliente
    print(f"Nombre o Código de Barras: {nombre_codigo}")
    print(f"Cantidad: {cantidad}")
    print(f"Tipo de Pago: {tipo_pago}")

def agregar_ticket():
    # Mostrar el mensaje de venta concretada
    messagebox.showinfo("Información", "Venta Concretada")

def añadir_producto():
    nombre_codigo = entry_nombre_codigo.get()
    cantidad = entry_cantidad.get()
    tipo_pago = combo_tipo_pago.get()
    
    # Agregar el producto a la lista y actualizar la tabla
    if nombre_codigo and cantidad:
        productos.append((nombre_codigo, cantidad, tipo_pago))
        actualizar_tabla()
    else:
        messagebox.showwarning("Advertencia", "Debe completar todos los campos")

def actualizar_tabla():
    # Limpiar la tabla
    for row in tabla.get_children():
        tabla.delete(row)
    
    # Insertar los productos en la tabla
    for producto in productos:
        tabla.insert("", tk.END, values=producto)

# Crear la ventana principal
root = tk.Tk()
root.title("Formulario de Vinculación de Cliente")

# Crear y ubicar los widgets en la ventana
tk.Label(root, text="Nombre o Código de Barras:").grid(row=0, column=0, padx=10, pady=10, sticky=tk.E)
entry_nombre_codigo = tk.Entry(root)
entry_nombre_codigo.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Cantidad:").grid(row=1, column=0, padx=10, pady=10, sticky=tk.E)
entry_cantidad = tk.Entry(root)
entry_cantidad.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Tipo de Pago:").grid(row=2, column=0, padx=10, pady=10, sticky=tk.E)
combo_tipo_pago = ttk.Combobox(root, values=["Efectivo", "Tarjeta de Crédito", "Tarjeta de Débito", "Transferencia"])
combo_tipo_pago.grid(row=2, column=1, padx=10, pady=10)
combo_tipo_pago.set("Efectivo")  # Valor predeterminado

# Botón para vincular cliente
btn_vincular_cliente = tk.Button(root, text="Vincular Cliente", command=vincular_cliente)
btn_vincular_cliente.grid(row=3, columnspan=2, padx=10, pady=10)

# Botón para añadir producto
btn_añadir_producto = tk.Button(root, text="Añadir Producto", command=añadir_producto)
btn_añadir_producto.grid(row=4, columnspan=2, padx=10, pady=10)

# Botón para terminar venta
btn_agregar_ticket = tk.Button(root, text="Terminar Venta", command=agregar_ticket)
btn_agregar_ticket.grid(row=5, columnspan=2, padx=10, pady=20)

# Crear la tabla para mostrar los productos
columnas = ("Nombre/Código", "Cantidad", "Tipo de Pago")
tabla = ttk.Treeview(root, columns=columnas, show='headings')
tabla.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

# Configurar las cabeceras de la tabla
for col in columnas:
    tabla.heading(col, text=col)

# Iniciar el bucle principal de eventos
root.mainloop()
