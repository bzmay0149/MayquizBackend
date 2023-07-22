from database.connect_db import create_connection

def get_preguntas():
    try:
        # Crear la conexión a la base de datos
        con = create_connection()
        cur = con.cursor()

        # Consulta SQL para obtener todas las preguntas con sus respuestas
        cur.execute("""
                     SELECT P.pregunta, R.respuesta
                     FROM Preguntas P
                     JOIN Respuestas R ON P.idpregunta = R.idpregunta
                     ORDER BY P.idpregunta, R.idrespuesta
           
        """)

        # Obtener todas las filas de la tabla Preguntas con sus respuestas como una lista de diccionarios
        preguntas = []
        pregunta_actual = {}
        for row in cur.fetchall():
            if not pregunta_actual or pregunta_actual['idpregunta'] != row[0]:
                pregunta_actual = {
                    'idpregunta': row[0],
                    'pregunta': row[1],
                    'tema': row[2],
                    'nivel': row[3],
                    'respuestas': []
                }
                preguntas.append(pregunta_actual)

            pregunta_actual['respuestas'].append({
                'idrespuesta': row[4],
                'respuesta': row[5],  # Actualizar aquí para obtener el texto de la respuesta
                'correcta': bool(row[6])
            })

        # Cerrar la conexión a la base de datos
        con.close()

        # Filtrar los campos no deseados en las preguntas y respuestas antes de devolver los datos
        for pregunta in preguntas:
            pregunta.pop('idpregunta')
            pregunta.pop('tema')
            pregunta.pop('nivel')
            for respuesta in pregunta['respuestas']:
                respuesta.pop('idrespuesta')

        return preguntas

    except Exception as e:
        return {'error': str(e)}

