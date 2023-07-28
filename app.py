

from flask import Flask, jsonify
from models.queries import get_all_preguntas, get_preguntas_html_inicio, get_preguntas_html_medio, get_preguntas_html_experto

from flask_cors import CORS

app = Flask(__name__)
CORS(app)


# Ruta para obtener todas las preguntas
@app.route('/Preguntas', methods=['GET'])
def obtener_preguntas():
    
    preguntas = get_all_preguntas()
    return jsonify(preguntas)

# Nueva ruta para obtener preguntas de HTML Inicial
@app.route('/Preguntas/html/inicio', methods=['GET'])
def obtener_preguntas_html_inicio():
    preguntas_html_inicio = get_preguntas_html_inicio()
    return jsonify(preguntas_html_inicio)


# Nueva ruta para obtener preguntas de HTML medio
@app.route('/Preguntas/html/medio', methods=['GET'])
def obtener_preguntas_html_medio():
    preguntas_html_medio = get_preguntas_html_medio()
    return jsonify(preguntas_html_medio)

# Nueva ruta para obtener preguntas de HTML experto
@app.route('/Preguntas/html/experto', methods=['GET'])
def obtener_preguntas_html_experto():
    preguntas_html_experto = get_preguntas_html_experto()
    return jsonify(preguntas_html_experto)

# Aquí puedes definir más rutas para obtener respuestas, temarios, niveles, etc.

if __name__ == '__main__':
    app.run(debug=True)





