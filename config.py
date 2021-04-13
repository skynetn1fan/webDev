from os import environ, path
from dotenv import load_dotenv


basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

class Config:

    TESTING = False
    DEBUG = True
    FLASK_ENV = 'development'
    SECRET_KEY = environ.get('SECRET_KEY')
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = environ.get("SES_USERNAME")
    MAIL_PASSWORD = environ.get("SES_PASSWORD")
    MAIL_DEFAULT_SENDER = environ.get("SES_USERNAME")
    MAIL_SUPPRESS_SEND = False
