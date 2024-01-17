"""Module containing app instantiation."""
from flask import Flask

from config import Config


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions here
    from app.main import bp as main_bp
    # register this main blueprint for Flask
    # to treat as part of the application.
    app.register_blueprint(main_bp)

    # Register blueprints here

    @app.route('/test/')
    def test_page():
        return '<h1>Testing the Flask Application Factory Pattern</h1>'

    return app