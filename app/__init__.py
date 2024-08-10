from flask import Flask
from app.models import db
from app.controllers.controllers import auth_bp

class AppFactory:
    @staticmethod
    def create_app():
        flask_app = Flask(__name__, template_folder='views')
        flask_app.config.from_object('config')

        db.init_app(flask_app)

        flask_app.register_blueprint(auth_bp)

        return flask_app