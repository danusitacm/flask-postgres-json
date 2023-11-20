from .models import Tutor
from app.extensions import ma
from marshmallow import fields,validate

class TutorSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Tutor
        load_instance = True
        fields = ("tutor_pk", "puntaje_tutor", "usuario_pk")
        ordered=True
        
    tutor_pk = fields.Integer()
    #para validar tengo que haces esto
    # nombre = fields.String(required=True, validate=validate.Length(min=1, max=255),error=" el error")
    puntaje_tutor =fields.Float(required=True)
    usuario_pk = fields.Integer(required=True)

tutor_schema = TutorSchema ()
tutors_schema  = TutorSchema(many=True)