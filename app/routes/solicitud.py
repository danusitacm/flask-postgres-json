from flask import request, jsonify
from app.models.solicitud import Solicitud
from app.extensions import db
from app.schemas.solicitud import solicitud_schema, solicitudes_schema
from marshmallow  import ValidationError
from flask import Blueprint

solicitud_bp = Blueprint('solicitud', __name__,url_prefix="/solicitudes")

@solicitud_bp.route('/',methods=['GET'])
def obtener_solicituds():
    if request.method == 'GET':
        solicitud = Solicitud.query.all()
        return solicitudes_schema.dump(solicitud)
    
@solicitud_bp.route('/<int:id>',methods=['GET'])
def obtener_solicitud_id(id):
    if request.method == 'GET':
        solicitud = Solicitud.query.get(id)
        return solicitud_schema.dump(solicitud)

@solicitud_bp.route('/',methods= ['POST'])
def agregar_solicitud():
    if request.method == 'POST':
        try:
            # Validacion
            solicitud_schema.load(request.json)
            # Obtenemos los datos del json para validar
            fecha_solicitud = request.json['fecha_solicitud']
            estado_solicitud = request.json['estado_solicitud']
            materia_pk = request.json['materia_pk']
            alumno_pk = request.json['alumno_pk']
            nueva_solicitud = Solicitud(fecha_solicitud,
                                        estado_solicitud,
                                        materia_pk,
                                        alumno_pk)

            # agregamos el nuevo solicitud en la base de datos 
            db.session.add(nueva_solicitud)
            db.session.commit()
            # Retornamos el solicitud creada
            return solicitud_schema.dump(nueva_solicitud), 201
        except ValidationError as err:
            return err.messages, 400
            
        
    
@solicitud_bp.route('/<int:id>',methods=['PUT'])
def actualizar_solicitud(id):
    if request.method == 'PUT':
        try:
            solicitud = solicitud.query.get(id)
            solicitud_schema.load(request.json)
            fecha_solicitud = request.json['fecha_solicitud']
            estado_solicitud = request.json['estado_solicitud']
            materia_pk = request.json['materia_pk']
            alumno_pk = request.json['alumno_pk']
            solicitud_actualizada = Solicitud(fecha_solicitud,
                                        estado_solicitud,
                                        materia_pk,
                                        alumno_pk)
            db.commit()
            return solicitud_schema.dump(solicitud_actualizada), 200
        except ValidationError as err:
            return err.messages,400
       