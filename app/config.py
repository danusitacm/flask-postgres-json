import os

SECRET_KEY = os.environ.get('SECRET_KEY')
#postgres://username:password@localhost:5432/dbname
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:12345@localhost:5432/testdb'
SQLALCHEMY_TRACK_MODIFICATIONS = False
