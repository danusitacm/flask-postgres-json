import os

SECRET_KEY = os.environ.get('SECRET_KEY')
#postgres://username:password@localhost:5432/dbname
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://postgres:password@localhost:5432/cars_api'
SQLALCHEMY_TRACK_MODIFICATIONS = False
