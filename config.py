import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'una-clave-secreta-para-desarrollo'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///sgea.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False