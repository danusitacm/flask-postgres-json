from flask import request, jsonify
from app.models.alumno import Alumno
from app.extensions import db
from app.schemas.alumno import alumno_schema, alumnos_schema
from marshmallow  import ValidationError
from flask import Blueprint

alumno_bp = Blueprint('alumno', __name__,url_prefix='/alumnos')

@alumno_bp.route('/',methods=['GET'])
def obtener_alumnos():
    if request.method == 'GET':
        alumno = Alumno.query.all()
        return alumnos_schema.dump(alumno)
    
@alumno_bp.route('/<int:id>',methods=['GET'])
def obtener_alumno_id(id):
    if request.method == 'GET':
        alumno = Alumno.query.get(id)
        return alumno_schema.dump(alumno)

@alumno_bp.route('/',methods= ['POST'])
def agregar_alumno():
    if request.method == 'POST':
        try:
            # Validacion
            alumno_schema.load(request.json)
            # Obtenemos los datos del json para validar
            puntaje_alumno = request.json['puntaje_alumno']
            usuario_pk = request.json['usuario_pk']
            nuevo_alumno = Alumno(puntaje_alumno,usuario_pk)

            # agregamos el nuevo alumno en la base de datos 
            db.session.add(nuevo_alumno)
            db.session.commit()

            # Retornamos el alumno creado 
            return alumno_schema.dump(nuevo_alumno), 201
        except ValidationError as err:
            return err.messages, 400
            
        
    
@alumno_bp.route('/<int:id>',methods=['PUT'])
def actualizar_alumno(id):
    if request.method == 'PUT':
        try:
            alumno = Alumno.query.get(id)
            alumno_schema.load(request.json)
            alumno.puntaje_alumno = request.json['puntaje_alumno']
            alumno.usuario_pk = request.json['usuario_pk']
            db.session.commit()
            return alumno_schema.dump(alumno), 200
        except ValidationError as err:
            return err.messages,400
