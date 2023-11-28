from flask import request, jsonify
from app.models.review_tutor import ReviewTutor
from app.extensions import db
from app.schemas.review_tutor import reviewtutorschema, reviewtutoresschema
from marshmallow  import ValidationError
from flask import Blueprint

review_tutor_bp = Blueprint('review_tutor', __name__,url_prefix="/review_tutor")