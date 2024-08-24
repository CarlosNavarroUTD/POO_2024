from flask import request, jsonify, render_template, redirect, url_for
from flask_login import login_user, login_required, logout_user
from .usuario import Usuario
from . import usuarios_bp

@usuarios_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.form
        username = data.get('username')
        contrasena = data.get('contrasena')
        
        usuario = Usuario.iniciar_sesion(username, contrasena)
        if usuario:
            login_user(usuario)
            return redirect(url_for('main.index'))
        else:
            return render_template('usuarios/login.html', error="Username o contraseña incorrectos")
    return render_template('usuarios/login.html')

@usuarios_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('usuarios.login'))
@usuarios_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        data = request.form
        nombre = data.get('nombre')
        username = data.get('username')
        contrasena = data.get('contrasena')
        
        nuevo_usuario = Usuario.registrarse(nombre, username, contrasena)
        if nuevo_usuario:
            return redirect(url_for('usuarios.login'))
        else:
            return render_template('Usuarios/registro.html', error="Error en el registro")
    return render_template('Usuarios/registro.html')

@usuarios_bp.route('/profile/<int:id>', methods=['GET'])
def profile(id):
    usuario = Usuario.obtener_por_id(id)  # Asume que tienes un método para obtener un usuario por ID
    if usuario:
        return render_template('usuarios/profile.html', usuario=usuario)
    else:
        return render_template('usuarios/profile.html', error="Usuario no encontrado")

# Puedes añadir más rutas relacionadas con usuarios aquí.