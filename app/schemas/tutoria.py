from app.models.tutoria import Tutoria
from app.extensions import ma
from marshmallow import fields,validate

class TutoriaSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Tutoria
        load_instance = True
        fields = ("tutoria_pk", 
                  "fecha_inicio",
                  "fecha_fin", 
                  "materia_pk",
                  "alumno_pk",
                  "tutor_pk")
        ordered=True
    
    tutoria_pk=fields.Integer()
    fecha_inicio=fields.Date(required=True)
    fecha_fin=fields.Date(required=True)
    materia_pk=fields.Integer(required=True)
    alumno_pk=fields.Integer(required=True)
    tutor_pk=fields.Integer(required=True)
    

tutoria_schema = TutoriaSchema ()
tutorias_schema  = TutoriaSchema(many=True)