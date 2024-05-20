from flask import Flask
from flask_bootstrap import Bootstrap #cada que se inicie hay que instalar --- pip install flask-bootstrap
from app.config import Config

def create_app():
    app = Flask(__name__)
    bootstrap = Bootstrap(app)
    app.config.from_object(Config)
    return app