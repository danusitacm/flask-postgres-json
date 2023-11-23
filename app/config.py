from os import environ 
from dotenv import load_dotenv
load_dotenv()

SECRET_KEY = environ.get('SECRET_KEY')
#postgres://username:password@localhost:5432/dbname
SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL')
SQLALCHEMY_TRACK_MODIFICATIONS = False
