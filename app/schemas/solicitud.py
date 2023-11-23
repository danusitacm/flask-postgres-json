from app.models.solicitud import Solicitud
from app.extensions import ma
from marshmallow import fields,validate

class SolicitudSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Solicitud
        load_instance = True
        fields = ("solicitud_pk", 
                  "fecha_solicitud",
                  "estado_solicitud", 
                  "materia_pk",
                  "alumno_pk")
        ordered=True
        
    solicitud_pk = fields.Integer()
    #para validar tengo que haces esto
    # nombre = fields.String(required=True, validate=validate.Length(min=1, max=255),error=" el error")
    fecha_solicitud =fields.Date(required=True)
    estado_solicitud = fields.String(required=True)
    materia_pk = fields.Integer(required=True)
    alumno_pk = fields.Integers(required=True)

solicitud_schema = SolicitudSchema ()
solicitudes_schema  = SolicitudSchema(many=True)