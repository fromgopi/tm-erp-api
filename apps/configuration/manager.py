"""Configuration Manager"""
import os
import sys
import logging
from dotenv import load_dotenv, find_dotenv
from apps.common.constants import ENV_PATH

from apps.common.exceptions import ConfigurationError
import apps.resources.strings.configuration as strings


def get_configuration(logger):
    try:
        def configuration():
            return None
        if not find_dotenv(ENV_PATH):
            raise ConfigurationError(strings.ENV_FILE_NOT_FOUND)
        loading_env = load_dotenv(ENV_PATH, verbose=True)
        configuration.NAME = os.getenv('NAME')
        configuration.PORT = os.getenv('PORT')
        configuration.AUTH_TOKEN_EXPIRY = os.getenv('AUTH_TOKEN_EXPIRY')
        configuration.SECRET_KEY = os.getenv('SECRET_KEY')
        # Flask Debug and Testing
        configuration.FLASK_ENV = os.getenv('FLASK_ENV')
        configuration.FLASK_DEBUG = (os.getenv('FLASK_DEBUG') == 'True')
        # Logging
        configuration.LOG_CONSOLE_LEVEL = os.getenv('LOG_CONSOLE_LEVEL')
        configuration.LOG_DEBUG_FILE_LEVEL = os.getenv('LOG_DEBUG_FILE_LEVEL')
        configuration.LOG_DEBUG_FILE_TO = os.getenv('LOG_DEBUG_FILE_TO')
        configuration.LOG_ERROR_FILE_LEVEL = os.getenv('LOG_ERROR_FILE_LEVEL')
        configuration.LOG_ERROR_FILE_TO = os.getenv('LOG_ERROR_FILE_TO')
        
        # SQL Alchemy
        configuration.SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
        configuration.SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')
        
        return configuration
    except ConfigurationError as error:
        logger.fatal('[Boot] ' + getattr(error, 'message', str(error)))
        sys.exit(1)

def setup_configuration(app):
    """
    Configures the app
    Args:
        app (Flask): Flask App instance
    """
    logger = logging.getLogger(__name__)
    configuration = get_configuration(logger)
    app.config.from_object(configuration)