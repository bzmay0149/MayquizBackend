from database.connect_db import create_connection

def get_all_preguntas():
    try:
        connection = create_connection()
        cursor = connection.cursor()

        query = 'SELECT p.idpregunta, p.pregunta, p.idtema, p.idnivel, r.respuesta, r.correcta FROM Preguntas p JOIN Respuestas r ON p.idpregunta = r.idpregunta'
        cursor.execute(query)

        preguntas = []
        for row in cursor.fetchall():
            idpregunta = row[0]
            pregunta = row[1]
            idtema = row[2]
            idnivel = row[3]
            respuesta = row[4]
            correcta = row[5]

            # Buscar la pregunta en la lista de preguntas
            pregunta_actual = next((p for p in preguntas if p['idpregunta'] == idpregunta), None)

            # Si la pregunta no existe en la lista, agregarla
            if not pregunta_actual:
                pregunta_actual = {
                    'idpregunta': idpregunta,
                    'pregunta': pregunta,
                    'idtema': idtema,
                    'idnivel': idnivel,
                    'respuestas': [],
                    'respuestaCorrecta': None
                }
                preguntas.append(pregunta_actual)

            # Agregar la respuesta a la lista de respuestas de la pregunta
            pregunta_actual['respuestas'].append(respuesta)

            # Si la respuesta es correcta, asignarla a la propiedad 'respuestaCorrecta'
            if correcta:
                pregunta_actual['respuestaCorrecta'] = respuesta

        cursor.close()
        connection.close()

        return preguntas

    except Exception as e:
        return {'error': str(e)}

