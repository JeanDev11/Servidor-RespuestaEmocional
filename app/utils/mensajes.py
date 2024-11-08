import random

# Diccionario de mensajes predeterminados específicos por emoción
mensajes_predeterminados = {
    "sorprendido": [
        "A veces, lo inesperado puede traernos nuevas perspectivas. Tómate tu tiempo para procesarlo.",
        "Es normal sentir sorpresa. Respira y trata de adaptarte a esta nueva información poco a poco.",
        "Las sorpresas nos recuerdan que la vida es impredecible. Encuentra lo positivo en lo inesperado.",
        "Permítete explorar la sorpresa con curiosidad en lugar de temor. Puede haber oportunidades ocultas."
    ],
    "miedo": [
        "Recuerda que eres fuerte y puedes enfrentar este miedo. Da un paso a la vez.",
        "El miedo es una respuesta natural. Intenta centrarte en tu respiración y darte tiempo.",
        "El coraje no es la ausencia de miedo, sino avanzar a pesar de él. Confía en ti mismo.",
        "Busca un lugar seguro, física o mentalmente, para recordar que este momento también pasará."
    ],
    "enojado": [
        "Está bien sentir enojo. Tómate unos momentos para calmarte y reflexionar antes de actuar.",
        "El enojo puede ser intenso. Date permiso para sentirlo, pero también para encontrar paz.",
        "Intenta canalizar tu enojo hacia algo constructivo, como ejercicio o escritura.",
        "Recuerda, la calma no llega cuando se suprime el enojo, sino cuando se comprende su causa."
    ],
    "neutral": [
        "Es bueno tener momentos de calma y neutralidad. Aprovéchalos para recargar energías.",
        "La tranquilidad es valiosa. Puedes usar este momento para descansar o planificar.",
        "Aprovecha la neutralidad para reflexionar y establecer tus próximos objetivos.",
        "Los momentos de equilibrio son ideales para practicar la gratitud por las pequeñas cosas."
    ],
    "tristeza": [
        "La tristeza es natural y parte de la vida. No estás solo; permítete sentirla.",
        "A veces, permitirse estar triste ayuda a sanar. Recuerda que esta emoción también pasará.",
        "Habla con alguien en quien confíes. Compartir lo que sientes puede aliviar tu carga.",
        "El autocuidado es esencial en momentos de tristeza. Haz algo que te brinde consuelo."
    ],
    "disgustado": [
        "Es comprensible sentirse disgustado. Tómate un momento para procesar y recuperar la calma.",
        "Si algo te molesta, intenta expresar tus pensamientos de forma saludable y con calma.",
        "El disgusto puede ser una señal para reflexionar sobre tus límites. Escucha lo que te dice.",
        "Practica la empatía: intenta entender el punto de vista contrario antes de reaccionar."
    ],
    "feliz": [
        "¡Qué alegría que te sientas bien! Disfruta y comparte esta felicidad con los demás.",
        "Momentos de felicidad como este son para saborear. Mantén esta energía positiva.",
        "Celebra tus logros, grandes o pequeños. La felicidad es más plena cuando te la permites.",
        "Comparte tu felicidad con los demás. A menudo, la alegría se multiplica al compartirla."
    ]
}

# Mensaje general para combinaciones o emociones no especificadas
mensaje_general = [
    "Cualquiera que sea la emoción, permítete sentir y procesar tus sentimientos.",
    "Tus emociones son válidas. Tómate el tiempo necesario para reflexionar y hallar calma.",
    "Recuerda que cada emoción tiene algo que enseñarte. Dale espacio para expresarse.",
    "No estás solo en lo que sientes. Hablar con alguien de confianza puede ayudarte.",
    "Las emociones son parte de ser humano. Acéptalas como vienen, sin juzgarte.",
    "Cada emoción es pasajera. Lo importante es cómo decides responder a ella.",
    "El autocuidado es clave. Dedica tiempo a lo que te ayuda a recuperar el equilibrio.",
    "Respira profundamente y date permiso para pausar. Es un acto de fortaleza, no de debilidad.",
    "Conecta con tu cuerpo: una caminata o unos estiramientos pueden ayudarte a despejar la mente.",
    "Busca pequeños momentos de gratitud, incluso en días difíciles. Pueden brindarte un respiro."
]

def generar_respuesta_predeterminada(emociones):
    respuestas = []
    
    # Generar respuestas predeterminadas para cada emoción
    for emocion in emociones:
        if emocion in mensajes_predeterminados:
            # Si hay mensajes predeterminados, seleccionamos algunos aleatorios
            print(min(3, len(mensajes_predeterminados[emocion])))
            mensajes = random.sample(mensajes_predeterminados[emocion], min(3, len(mensajes_predeterminados[emocion])))
            respuestas.extend(mensajes)
        else:
            # Si no hay mensajes predeterminados, usamos el mensaje general
            respuestas.append(random.choice(mensaje_general))
    return respuestas


def limpiar_respuesta(texto):
    # Dividir el texto por saltos de línea
    lineas = texto.strip().split("\n")
    lineas_modificadas  = []
    
    for linea in lineas:
        if ':' in linea:
            # Dividir la línea en dos partes, antes y después del ':', y tomamos lo que está después
            parte_despues_dos_puntos = linea.split(':', 1)[1].strip()  
            lineas_modificadas.append(parte_despues_dos_puntos)
        elif linea.strip():
            # Si no hay dos puntos, agregar la línea original
            lineas_modificadas.append(linea.strip())
    
    return lineas_modificadas