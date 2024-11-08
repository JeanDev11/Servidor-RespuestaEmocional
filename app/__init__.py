from flask import Flask
from dotenv import load_dotenv
import os

def create_app():
    # Cargar variables de entorno desde el archivo .env
    load_dotenv()
    
    app = Flask(__name__)
    
    # Configurar API Key de Google
    app.config["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
    if not app.config["GOOGLE_API_KEY"]:
        raise ValueError("API Key de Google no encontrada en las variables de entorno")
    
    # Registrar rutas
    with app.app_context():
        from .routes.response import main_bp
        app.register_blueprint(main_bp)
    
    return app
