from flask import Flask
from flask_graphql import GraphQLView
from config.config import config
from schema import schema
import os

def create_app():
    app = Flask(__name__)
    app.config.from_object(config['development']())
    app.config.setdefault('PORT', int(os.getenv('PORT', 5002)))

    app.add_url_rule(
        '/reviews',
        view_func=GraphQLView.as_view(
            'graphql',
            schema=schema,
            graphiql=True
        )
    )

    @app.get("/healthz")
    def healthz():
        return "ok", 200

    print(f"reviews corriendo en puerto {app.config['PORT']}")
    return app