from flask import Flask, jsonify
from database.connect_db import create_connection
from models.queries import get_preguntas
from flask_cors import CORS





app = Flask(__name__)
CORS(app)

@app.route('/Preguntas', methods=['GET'])
def preguntas():
    try:
        preguntas = get_preguntas()
        return jsonify(preguntas)

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)


