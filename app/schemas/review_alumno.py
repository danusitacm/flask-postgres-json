from app.models.review_alumno import ReviewAlumno
from app.extensions import ma
from marshmallow import fields,validate

class ReviewAlumnoSchema(ma.SQLAlchemySchema):
    class Meta:
        model = ReviewAlumno
        load_instance = True  
        fields = (
            'review_alumno_pk',
            'descripcion',
            'calificacion_alumno',
            'tutor_pk',
            'alumno_pk',
        )
    review_alumno_pk=fields.Integer()
    descripcion =fields.String(required=True)
    calificacion_alumno =fields.Float(required=True)
    tutor_pk=fields.Integer()
    alumno_pk=fields.Integer()
    
reviewalumnoschema =ReviewAlumnoSchema()
reviewalumnosschema =ReviewAlumnoSchema(many=True)