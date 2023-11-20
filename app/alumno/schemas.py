from .models import Alumno
from app.extensions import ma
from marshmallow import fields,validate

class AlumnoSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Alumno
        load_instance = True
        fields = ("alumno_pk", "puntaje_alumno", "usuario_pk")
        ordered=True
        
    alumno_pk = fields.Integer()
    #para validar tengo que haces esto
    # nombre = fields.String(required=True, validate=validate.Length(min=1, max=255),error=" el error")
    puntaje_alumno =fields.Float(required=True)
    usuario_pk = fields.Integer(required=True)

alumno_schema = AlumnoSchema ()
alumnos_schema  = AlumnoSchema(many=True)