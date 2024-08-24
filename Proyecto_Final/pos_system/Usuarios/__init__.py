from flask import Blueprint

# Definir el blueprint
usuarios_bp = Blueprint('usuarios', __name__, url_prefix='/usuarios')

# Importar las vistas para registrar las rutas con el blueprint
from .views import *

# Este archivo debe ser autocontenido, por lo que puedes agregar cualquier otro inicializador necesario aquí.
