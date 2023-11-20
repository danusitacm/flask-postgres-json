import os

from flask import Flask
from app.alumno import alumno
from app.usuario import usuario
from app.extensions import db,migrate,ma
def create_app():
    # create and configure the app
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    
    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)
    
    app.register_blueprint(usuario)
    app.register_blueprint(alumno)
    
    
    #app.cli.add_command(create_tables)
    
    # a simple page that says hello
    @app.route('/')
    def hello():
        return 'Hello, World!'

    return app