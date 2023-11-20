from .models import Usuario
from app.extensions import ma
from marshmallow import fields,validate

class UsuarioSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Usuario
        load_instance = True
        fields = ("usuario_pk", "nombre", "email", "telefono", "genero")
        ordered=True
        
    usuario_pk = fields.Integer()
    #para validar tengo que haces esto
    # nombre = fields.String(required=True, validate=validate.Length(min=1, max=255),error=" el error")
    
    nombre = fields.String(required=True)
    email = fields.String(required=True)
    telefono = fields.String(required=True)
    genero = fields.String(required=True)

usuario_schema = UsuarioSchema ()
usuarios_schema  = UsuarioSchema(many=True)