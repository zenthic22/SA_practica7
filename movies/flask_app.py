from flask import Flask
from config.config import config
from routes.movies_routes import movies_routes
import os

def create_app():
    app = Flask(__name__)

    app.config.from_object(config['development']())
    app.config.setdefault('PORT', int(os.getenv('PORT', 3000)))

    app.register_blueprint(movies_routes)

    @app.get("/healthz")
    def healthz():
        return "ok", 200

    print(f"Servidor corriendo en puerto {app.config['PORT']}")
    print('Microservicio movies iniciando correctamente')
    return app