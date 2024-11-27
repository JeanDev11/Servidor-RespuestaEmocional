from flask import Blueprint, request, jsonify
from app.services.genai_service import generar_respuesta_ai
from app.utils.mensajes import generar_respuesta_predeterminada, limpiar_respuesta
import logging

# Configurar el logger para mostrar mensajes de depuración en la consola
logging.basicConfig(level=logging.DEBUG)

main_bp = Blueprint("main", __name__)

@main_bp.route("/generar_respuesta", methods=["POST"])
def generar_respuesta():
    data = request.json
    nombre_input = data.get("nombre", "").strip()
    emociones_input  = data.get("emociones", {})

    try:
        # Filtrar emociones relevantes (> 8%)
        emociones_relevantes = {
            emocion.lower(): porcentaje
            for emocion, porcentaje in emociones_input.items()
            if porcentaje > 8.0
        }

        if emociones_relevantes:
            # Construir un mensaje basado en las emociones relevantes
            emociones_str = ", ".join(
                f"{emocion.lower()} ({porcentaje:.1f}%)"
                for emocion, porcentaje in emociones_relevantes.items()
            )
        else:
            # No hay emociones relevantes
            emociones_str = None
        
        if emociones_str:
            try:
                respuesta_ai = generar_respuesta_ai(emociones_str)
                respuesta_ai_cleaned = limpiar_respuesta(respuesta_ai)

                saludo = f"¡Hola, {nombre_input.capitalize()}! "

                return jsonify({"response": [saludo] + respuesta_ai_cleaned, "response IA": [respuesta_ai]}), 200
            except Exception as ia_error:
                logging.error(f"Error con la IA: {str(ia_error)}")
        

        logging.debug(f"Emociones relevantes: {emociones_str}")
        
        # Manejar casos sin emociones relevantes o errores de la IA (falta de creditos, etc)
        respuestas = generar_respuesta_predeterminada(emociones_relevantes.keys() if emociones_relevantes else [])
        saludo = f"¡Hola, {nombre_input.capitalize()}! "

        return jsonify({"response": [saludo] + respuestas}), 200
    
    except Exception as general_error:
        logging.error(f"Error al procesar la solicitud: {str(general_error)}")
        return jsonify({"error": "Ocurrió un error al procesar la solicitud."}), 500

