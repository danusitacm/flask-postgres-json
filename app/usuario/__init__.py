from flask import Blueprint

usuario = Blueprint('usuario',__name__,url_prefix='/usuarios')

from . import routes