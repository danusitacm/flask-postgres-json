from flask import Blueprint

materia = Blueprint('materia', __name__,url_prefix="/materias")

from . import routes