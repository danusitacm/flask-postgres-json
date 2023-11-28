from app.models.review_tutor import ReviewTutor
from app.extensions import ma
from marshmallow import fields,validate

class ReviewTutorSchema(ma.SQLAlchemySchema):
    class Meta:
        model = ReviewTutor
        load_instance = True  
        fields = (
            'review_tutor_pk',
            'descripcion',
            'calificacion_tutor',
            'tutor_pk',
            'alumno_pk',
        )
    review_tutor_pk=fields.Integer()
    descripcion =fields.String(required=True)
    calificacion_tutor =fields.Float(required=True)
    tutor_pk=fields.Integer()
    alumno_pk=fields.Integer()
    
reviewtutorschema =ReviewTutorSchema()
reviewtutoresschema =ReviewTutorSchema(many=True)