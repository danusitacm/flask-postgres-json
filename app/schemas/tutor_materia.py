from app.models.tutor_materia import TutorMateria
from app.extensions import ma
from marshmallow import fields,validate

class TutorMateriaSchema(ma.SQLAlchemySchema):
    class Meta:
        model = TutorMateria
        load_instance = True
        fields = ("materia_pk", "tutor_pk")
        ordered=True
        
    materia_pk = fields.Integer()
    alumno_pk = fields.Integer()
    #para validar tengo que haces esto
    # nombre = fields.String(required=True, validate=validate.Length(min=1, max=255),error=" el error")

tutor_materia_schema = TutorMateriaSchema ()
tutores_materias_schema  = TutorMateriaSchema(many=True)