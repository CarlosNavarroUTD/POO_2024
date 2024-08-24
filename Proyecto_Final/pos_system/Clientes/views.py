from flask import request, jsonify, render_template
from .usuario import Usuario
from . import usuarios_bp

@usuarios_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    contrasena = data.get('contrasena')
    
    usuario = Usuario.iniciar_sesion(username, contrasena)
    if usuario:
        return jsonify({"message": "Login exitoso", "usuario": usuario.username}), 200
    else:
        return jsonify({"message": "Username o contraseña incorrectos"}), 401

@usuarios_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    nombre = data.get('nombre')
    username = data.get('username')
    contrasena = data.get('contrasena')
    
    nuevo_usuario = Usuario.registrarse(nombre, username, contrasena)
    if nuevo_usuario:
        return jsonify({"message": "Registro exitoso", "usuario": nuevo_usuario.username}), 201
    else:
        return jsonify({"message": "Error en el registro"}), 400

@usuarios_bp.route('/profile/<int:id>', methods=['GET'])
def profile(id):
    # Aquí podrías implementar una lógica para mostrar el perfil de un usuario basado en su ID.
    # Por simplicidad, podríamos simularlo.
    return jsonify({"message": "Este es el perfil del usuario con ID {}".format(id)})

# Puedes añadir más rutas relacionadas con usuarios aquí.
