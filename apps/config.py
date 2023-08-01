import os

class Config:
    
    base_dir = os.path.abspath(os.path.dirname(__file__))
    SECRET_KEY = os.getenv('SECRET_KEY', 'N97GPAtmUpAQ4ysFBxRDyA==')
    SQLALCHEMY_TRACK_MODIFICATIONS = False 
    ASSETS_ROOT = os.getenv('ASSETS_ROOT', '/static/assets')
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')    
    print(SQLALCHEMY_DATABASE_URI)

    

class DevelopmentConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True
    

class ProductionConfig(Config):
    FLASK_ENV = 'production'
    DEBUG = False
    

# Load all the config
config_dict = {
    'Production': ProductionConfig,
    'Debug': DevelopmentConfig
}