from .models import Materia
from app.extensions import ma
from marshmallow import fields,validate

class MateriaSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Materia
        load_instance = True
        fields = ("materia_pk", "nombre", "codigo")
        ordered=True
        
    materia_pk = fields.Integer()
    #para validar tengo que haces esto
    # nombre = fields.String(required=True, validate=validate.Length(min=1, max=255),error=" el error")
    nombre =fields.String(required=True)
    codigo = fields.String(required=True)

materia_schema = MateriaSchema ()
materias_schema  = MateriaSchema(many=True)