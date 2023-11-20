from flask import Blueprint

tutor = Blueprint('tutor', __name__,url_prefix="/tutores")

from . import routes