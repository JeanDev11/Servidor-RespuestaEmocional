# Servidor Flask de Análisis Emocional con Google Generative AI

Este proyecto es una API RESTful desarrollada con Flask que utiliza la API de **Google Generative AI** para generar respuestas empáticas basadas en emociones proporcionadas por el usuario. Además, incluye un sistema de mensajes predeterminados para situaciones donde la IA no puede generar respuestas.

## Características

- Generación de respuestas personalizadas utilizando modelos de lenguaje de Google.
- Mensajes de apoyo predeterminados según las emociones proporcionadas.
- Manejo de excepciones para garantizar respuestas consistentes incluso si la IA falla.

## Requisitos

- Python 3.8 o superior
- Flask
- google-generativeai
- python-dotenv

## Instalación

1. **Clona este repositorio**
   ```bash
   git clone https://github.com/JeanDev11/Servidor-RespuestaEmocional.git
   cd Servidor-RespuestaEmocional
2. **Crea un entorno virtual e instala las dependencias**
   ```bash
   python -m venv env
   env\Scripts\activate
   pip install -r requirements.txt
3. **Configura las variables de entorno**
   
   Crea un archivo .env en la raíz del proyecto con el siguiente contenido:
   ```bash
   GOOGLE_API_KEY=tu_api_key_aqui
4. **Ejecuta el servidor**
   ```bash
   flask run
   
El servidor estará disponible en http://localhost:5000.


## Endpoints

POST /generar_respuesta

Descripción: Genera una respuesta empática basada en la emoción proporcionada.
  ```bash
  {
      "nombre": "******"
      "emocion": "******"
  }
  ```

## Mensajes predeterminados
Si la IA no genera una respuesta adecuada, se utilizan mensajes predeterminados basados en las siguientes emociones:

- sorprendido
- miedo
- enojado
- neutral
- tristeza
- disgustado
- feliz

## Licencia
Este proyecto está licenciado bajo la MIT License.
