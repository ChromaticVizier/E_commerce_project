# This package is used to initialize the application.
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config_map
from flask_cors import CORS


db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    cors = CORS(app)
    obj = config_map.get(config_name)
    app.config.from_object(obj)
    db.init_app(app)

    from flask_api.user import user
    from flask_api.menu import menu

    app.register_blueprint(user)
    app.register_blueprint(menu)

    return app
