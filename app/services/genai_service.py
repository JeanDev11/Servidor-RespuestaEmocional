import google.generativeai as genai
from flask import current_app

def generar_respuesta_ai(emociones_str):
    genai.configure(api_key=current_app.config["GOOGLE_API_KEY"])
    model = genai.GenerativeModel("gemini-1.5-flash")
    prompt = (
        "Elimina el hilo de la conversación anterior."
        f"\nHola, me siento {emociones_str}."
        "Genera cuatro mensajes de apoyo empático siguiendo estas reglas:"
        "\n1. Los mensajes deben ser afirmativos, nunca en forma de pregunta."
        "\n2. Cada mensaje debe mostrar comprensión, validación o apoyo."
        "\n3. Usa un tono cálido y reconfortante."
        "\n4. Evita dar consejos no solicitados."
        "\n5. Cada mensaje deben tener entre 30 a 60 palabras."
        "\n6. Proporciona solo los mensajes, uno por línea, sin numeración ni formato adicional."
    )
    
    response = model.generate_content(prompt)
    
    # Si la IA responde, añadimos la respuesta
    if response and response.text:
        return response.text
    raise ValueError("La IA no generó una respuesta válida.")
