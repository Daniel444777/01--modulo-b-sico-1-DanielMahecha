# ejercicio22.py - Web con Flask
# Requiere: pip install flask
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>¡Hola desde mi servidor Flask!</h1><p>Esta es mi primera web con Python.</p>"

if __name__ == '__main__':
    print("Servidor corriendo en http://127.0.0.1:5000")
    # debug=True permite ver errores en vivo, no usar en producción
    app.run(debug=True, port=5000)