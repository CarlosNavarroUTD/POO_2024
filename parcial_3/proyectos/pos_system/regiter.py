import tkinter as tk
from tkinter import messagebox
from Usuarios.usuario import Usuario

class RegistroUsuario:
    def __init__(self, master):
        self.master = master
        master.title("Registro de Usuario")
        master.geometry("500x400")

        self.label_nombre = tk.Label(master, text="Nombre:")
        self.label_nombre.pack()
        self.entry_nombre = tk.Entry(master)
        self.entry_nombre.pack()

        self.label_username = tk.Label(master, text="Username:")
        self.label_username.pack()
        self.entry_username = tk.Entry(master)
        self.entry_username.pack()

        self.label_contrasena = tk.Label(master, text="Contraseña:")
        self.label_contrasena.pack()
        self.entry_contrasena = tk.Entry(master, show="*")
        self.entry_contrasena.pack()

        self.btn_registrar = tk.Button(master, text="Registrar", command=self.registrar_usuario)
        self.btn_registrar.pack()

    def registrar_usuario(self):
        nombre = self.entry_nombre.get()
        username = self.entry_username.get()
        contrasena = self.entry_contrasena.get()

        if not nombre or not username or not contrasena:
            messagebox.showerror("Error", "Por favor, complete todos los campos.")
            return

        nuevo_usuario = Usuario.registrarse(nombre, username, contrasena)
        if nuevo_usuario:
            messagebox.showinfo("Éxito", f"Usuario {username} registrado exitosamente.")
            self.master.destroy()
        else:
            messagebox.showerror("Error", "No se pudo registrar el usuario. El username podría estar ya en uso.")

if __name__ == "__main__":
    root = tk.Tk()
    app = RegistroUsuario(root)
    root.mainloop()