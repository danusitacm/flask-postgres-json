from flask import request, jsonify
from app.models.review_alumno import ReviewAlumno
from app.extensions import db
from app.schemas.review_alumno import reviewalumnoschema, reviewalumnosschema
from marshmallow  import ValidationError
from flask import Blueprint

review_alumno_bp = Blueprint('review_alumno', __name__,url_prefix="/review_alumno")