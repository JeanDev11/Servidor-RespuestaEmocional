from flask import Blueprint, request, jsonify
from app.services.genai_service import generar_respuesta_ai
from app.utils.mensajes import generar_respuesta_predeterminada, limpiar_respuesta

main_bp = Blueprint("main", __name__)

@main_bp.route("/generar_respuesta", methods=["POST"])
def generar_respuesta():
    data = request.json
    nombre_input = data.get("nombre", "").strip()
    emocion_input = data.get("emocion", "neutral").lower()
    emociones = [e.strip() for e in emocion_input.split(",")]

    try:
        respuesta_ai = generar_respuesta_ai(emocion_input)
        respuesta_ai_cleaned = limpiar_respuesta(respuesta_ai)
        saludo = f"¡Hola, {nombre_input.capitalize()}! "

        return jsonify({"response": [saludo] + respuesta_ai_cleaned, "response IA": [respuesta_ai]}), 200
    except Exception:
        respuestas = generar_respuesta_predeterminada(emociones)
        saludo = f"¡Hola, {nombre_input.capitalize()}! "
        respuestas_con_saludo = [saludo] + respuestas

        return jsonify({"response": respuestas_con_saludo}), 200
