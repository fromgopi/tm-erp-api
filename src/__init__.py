"""Entry point"""
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Resource, Api
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

from src.configuration.manager import setup_configuration
from src.configuration.modules.logger import setup_logger

API = Api()
DB = SQLAlchemy()
BCRYPT = Bcrypt()
JWT = JWTManager()

def register_extensions(APP)->None:
    """
    Instantiate all the extensions and make 
    available to Flask Instance

    Args:
        app (Flask Instance): Flask instance object
    
    Returns:
        None
    """
    DB.init_app(app=APP)
    BCRYPT.init_app(app=APP)
    JWT.init_app(app=APP)

def register_blueprints(app, prefix):
    """
    Register blueprints
    Args:
        app (Flask): Flask instance
        prefix (Str): Prefix route
    """
    from src.app.user.controllers.users import USER_API as user_blueprint
    app.register_blueprint(user_blueprint, url_prefix=prefix)
    

def create_app() -> Flask:
    """
    Creates instance of Flask app that can be runned from runner 
    Args:
        config (dict): Config dict

    Returns:
        Flask: Flask instance to export into runner
    """
    APP = Flask(__name__)
    API.init_app(app=APP)
    setup_configuration(APP)
    setup_logger(config=APP.config)
    register_extensions(APP=APP)
    register_blueprints(APP, os.getenv('ROUTE_PREFIX'))
    return APP