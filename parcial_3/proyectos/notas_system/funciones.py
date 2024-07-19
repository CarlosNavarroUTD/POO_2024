import os
import hashlib
from datetime import datetime


def esperarTecla():
  print("Oprima cualquier tecla para continuar ...")
  input()
  

def borrarPantalla():
    os.system('clear')

def hash_password(password):
    """Encripta una contraseña utilizando SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()

def obtener_fecha_actual():
    """Devuelve la fecha actual en formato YYYY-MM-DD."""
    return datetime.now().strftime("%d-%m-%Y")

def fecha_int():
    fecha_str = obtener_fecha_actual()
    fecha_int = int(fecha_str.replace("-", ""))
    return fecha_int