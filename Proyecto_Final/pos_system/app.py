from flask import Flask, render_template, request, redirect, url_for, session
from Usuarios.usuario import Usuario

app = Flask(__name__)
app.secret_key = 'super_secret_key'  # Cambia esto por una clave segura

@app.route('/')
def index():
    if 'user_id' in session:
        return f"Bienvenido, {session['username']}!"
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        contrasena = request.form['contrasena']
        usuario = Usuario.iniciar_sesion(username, contrasena)
        
        if usuario:
            session['user_id'] = usuario.id
            session['username'] = usuario.username
            return redirect(url_for('index'))
        else:
            return "Nombre de usuario o contraseña incorrectos", 401

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
