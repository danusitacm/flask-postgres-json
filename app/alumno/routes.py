from flask import request, jsonify
from app.alumno import alumno
from app.alumno.models import Alumno
from app.extensions import db
from .schemas import alumno_schema, alumnos_schema
from marshmallow  import ValidationError

@alumno.route('/',methods=['GET'])
def obtener_alumnos():
    if request.method == 'GET':
        alumno = Alumno.query.all()
        return alumnos_schema.dump(alumno)
    
@alumno.route('/<int:id>',methods=['GET'])
def obtener_alumno_id(id):
    if request.method == 'GET':
        alumno = Alumno.query.get(id)
        return alumno_schema.dump(alumno)

@alumno.route('/',methods= ['POST'])
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
            
        
    
@alumno.route('/<int:id>',methods=['PUT'])
def actualizar_alumno(id):
    if request.method == 'PUT':
        try:
            alumno = alumno.query.get(id)
            alumno_schema.load(request.json)
            puntaje_alumno = request.json['puntaje_alumno']
            usuario_pk = request.json['usuario_pk']
            nuevo_alumno = Alumno(puntaje_alumno,usuario_pk)
            return alumno_schema.dump(request.json), 200
        except ValidationError as err:
            return err.messages,400
       