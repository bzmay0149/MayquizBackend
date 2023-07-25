# from flask import Flask, jsonify
# from models.queries import get_all_preguntas
# from flask_cors import CORS
# app = Flask(__name__)
# CORS(app)
# # Ruta para obtener todas las preguntas
# @app.route('/Preguntas', methods=['GET'])
# def obtener_preguntas():
#     preguntas = get_all_preguntas()
#     return jsonify(preguntas)

# # Aquí puedes definir más rutas para obtener respuestas, temarios, niveles, etc.

# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, jsonify
from models.queries import get_all_preguntas
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Ruta para obtener todas las preguntas
@app.route('/Preguntas', methods=['GET'])
def obtener_preguntas():
    
    preguntas = get_all_preguntas()
    return jsonify(preguntas)

# Aquí puedes definir más rutas para obtener respuestas, temarios, niveles, etc.

if __name__ == '__main__':
    app.run(debug=True)





