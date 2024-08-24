from flask import Flask
from Usuarios import usuarios_bp

app = Flask(__name__)

# Registrar el blueprint
app.register_blueprint(usuarios_bp)

if __name__ == '__main__':
    app.run(debug=True)
s