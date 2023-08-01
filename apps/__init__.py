from pprint import pp

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Resource, Api

from apps.configuration.manager import setup_configuration

db = SQLAlchemy()
API = Api()

def register_extensions(app)->None:
    """
    Instantiate all the extensions and make 
    available to Flask Instance

    Args:
        app (Flask Instance): Flask instance object
    
    Returns:
        None
    """
    db.init_app(app=app)
    API.init_app(app=app)

def create_app() -> Flask:
    """
    Creates instance of Flask app that can be runned from runner 
    Args:
        config (dict): Config dict

    Returns:
        Flask: Flask instance to export into runner
    """
    app = Flask(__name__)
    print("calling create app frm the main method")
    setup_configuration(app)
    # register_extensions(app=app)
    pp(app.config)
    return app