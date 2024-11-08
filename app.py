from flask import Flask, request, jsonify
import google.generativeai as genai
from dotenv import load_dotenv
import os
import random

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Configura tu API Key de Google desde la variable de entorno
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    raise ValueError("API Key de Google no encontrada en las variables de entorno")

# Configura tu API Key de Google
genai.configure(api_key=GOOGLE_API_KEY)

# Diccionario de mensajes predeterminados específicos por emoción
mensajes_predeterminados = {
    "sorprendido": [
        "A veces, lo inesperado puede traernos nuevas perspectivas. Tómate tu tiempo para procesarlo.",
        "Es normal sentir sorpresa. Respira y trata de adaptarte a esta nueva información poco a poco."
    ],
    "miedo": [
        "Recuerda que eres fuerte y puedes enfrentar este miedo. Da un paso a la vez.",
        "El miedo es una respuesta natural. Intenta centrarte en tu respiración y darte tiempo."
    ],
    "enojado": [
        "Está bien sentir enojo. Tómate unos momentos para calmarte y reflexionar antes de actuar.",
        "El enojo puede ser intenso. Date permiso para sentirlo, pero también para encontrar paz."
    ],
    "neutral": [
        "Es bueno tener momentos de calma y neutralidad. Aprovéchalos para recargar energías.",
        "La tranquilidad es valiosa. Puedes usar este momento para descansar o planificar."
    ],
    "tristeza": [
        "La tristeza es natural y parte de la vida. No estás solo; permítete sentirla.",
        "A veces, permitirse estar triste ayuda a sanar. Recuerda que esta emoción también pasará."
    ],
    "disgustado": [
        "Es comprensible sentirse disgustado. Tómate un momento para procesar y recuperar la calma.",
        "Si algo te molesta, intenta expresar tus pensamientos de forma saludable y con calma."
    ],
    "feliz": [
        "¡Qué alegría que te sientas bien! Disfruta y comparte esta felicidad con los demás.",
        "Momentos de felicidad como este son para saborear. Mantén esta energía positiva."
    ]
}

# Mensaje general para combinaciones o emociones no especificadas
mensaje_general = [
    "Cualquiera que sea la emoción, permítete sentir y procesar tus sentimientos.",
    "Tus emociones son válidas. Tómate el tiempo necesario para reflexionar y hallar calma."
]

app = Flask(__name__)

@app.route("/generar_respuesta", methods=["POST"])
def generar_respuesta():
    data = request.json
    emocion_input = data.get("emocion", "neutral").lower()
    emociones = [e.strip() for e in emocion_input.split(",")]
    mensaje = f"Elimina el hilo de la conversación anterior. Hola, me siento {emocion_input}. ¿Puedes brindarme tres mensajes breves de apoyo empático, cada uno de los cuales ofrezca aliento y una sensación de calma?"

    # Lista para almacenar las respuestas
    respuestas = []

    try:
        # Intentar obtener respuesta de la IA generativa
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(mensaje)
        # Si la IA responde, añadimos la respuesta
        if response and response.text:
            respuestas.append(response.text)
        else:
            raise ValueError("La IA no generó una respuesta válida.")
        
    except Exception as e:
        # Generar respuestas predeterminadas para cada emoción
        for emocion in emociones:
            if emocion in mensajes_predeterminados:
                # Si hay mensajes predeterminados, seleccionamos algunos aleatorios
                mensajes = random.sample(mensajes_predeterminados[emocion], min(3, len(mensajes_predeterminados[emocion])))
                respuestas.extend(mensajes)
            else:
                # Si no hay mensajes predeterminados, usamos el mensaje general
                respuestas.append(random.choice(mensaje_general))

    return jsonify({"response": respuestas}), 200

if __name__ == "__main__":
    app.run(debug=True)
