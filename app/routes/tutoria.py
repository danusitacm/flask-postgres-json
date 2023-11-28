from flask import request, jsonify
from app.models.tutoria import Tutoria
from app.extensions import db
from app.schemas.tutoria import tutoria_schema, tutorias_schema
from marshmallow  import ValidationError
from flask import Blueprint

tutoria_bp = Blueprint('tutoria', __name__, url_prefix="/tutorias")