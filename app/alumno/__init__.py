from flask import Blueprint

alumno = Blueprint('alumno', __name__,url_prefix='/alumnos')

from . import routes