from flask import Blueprint

alumno = Blueprint('alumno', __name__)

from . import routes