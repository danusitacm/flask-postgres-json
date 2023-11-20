from flask import request, jsonify
from app.tutor import tutor
from app.tutor.models import Tutor
from app.extensions import db
from .schemas import tutor_schema, tutors_schema
from marshmallow  import ValidationError

@tutor.route('/',methods=['GET'])
def obtener_tutors():
    if request.method == 'GET':
        tutor = Tutor.query.all()
        return tutors_schema.dump(tutor)
    
@tutor.route('/<int:id>',methods=['GET'])
def obtener_tutor_id(id):
    if request.method == 'GET':
        tutor = Tutor.query.get(id)
        return tutor_schema.dump(tutor)

@tutor.route('/',methods= ['POST'])
def agregar_tutor():
    if request.method == 'POST':
        try:
            # Validacion
            tutor_schema.load(request.json)
            # Obtenemos los datos del json para validar
            puntaje_tutor = request.json['puntaje_tutor']
            usuario_pk = request.json['usuario_pk']
            nuevo_tutor = Tutor(puntaje_tutor,usuario_pk)

            # agregamos el nuevo tutor en la base de datos 
            db.session.add(nuevo_tutor)
            db.session.commit()

            # Retornamos el tutor creado 
            return tutor_schema.dump(nuevo_tutor), 201
        except ValidationError as err:
            return err.messages, 400
            
        
    
@tutor.route('/<int:id>',methods=['PUT'])
def actualizar_tutor(id):
    if request.method == 'PUT':
        try:
            tutor = tutor.query.get(id)
            tutor_schema.load(request.json)
            puntaje_tutor = request.json['puntaje_tutor']
            usuario_pk = request.json['usuario_pk']
            nuevo_tutor = Tutor(puntaje_tutor,usuario_pk)
            return tutor_schema.dump(request.json), 200
        except ValidationError as err:
            return err.messages,400
       