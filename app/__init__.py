import os

from flask import Flask
from app.commands import create_tables,delete_tables
from app.routes.usuario import usuario_bp
from app.routes.tutor import tutor_bp
from app.routes.materia import materia_bp
from app.routes.alumno import alumno_bp
from app.routes.solicitud import solicitud_bp
from app.routes.tutor_materia import tutor_materia_bp
from app.routes.tutoria import tutoria_bp
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
    
    app.register_blueprint(usuario_bp)
    app.register_blueprint(alumno_bp)
    app.register_blueprint(tutor_bp)
    app.register_blueprint(materia_bp)
    app.register_blueprint(solicitud_bp)
    app.register_blueprint(tutor_materia_bp)
    app.register_blueprint(tutoria_bp)
    
    app.cli.add_command(create_tables)
    app.cli.add_command(delete_tables)


    # a simple page that says hello
    @app.route('/')
    def hello():
        return 'Hello, World!'

    return app