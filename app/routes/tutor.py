from flask import request, jsonify
from app.models.tutor import Tutor
from app.extensions import db
from app.schemas.tutor import tutor_schema, tutors_schema
from marshmallow  import ValidationError
from flask import Blueprint

tutor_bp = Blueprint('tutor', __name__,url_prefix="/tutores")

@tutor_bp.route('/',methods=['GET'])
def obtener_tutors():
    if request.method == 'GET':
        tutor = Tutor.query.all()
        return tutors_schema.dump(tutor)
    
@tutor_bp.route('/<int:id>',methods=['GET'])
def obtener_tutor_id(id):
    if request.method == 'GET':
        tutor = Tutor.query.get(id)
        return tutor_schema.dump(tutor)

@tutor_bp.route('/',methods= ['POST'])
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
            
        
    
@tutor_bp.route('/<int:id>',methods=['PUT'])
def actualizar_tutor(id):
    if request.method == 'PUT':
        try:
            tutor = tutor.query.get(id)
            tutor_schema.load(request.json)
            tutor.puntaje_tutor = request.json['puntaje_tutor']
            tutor.usuario_pk = request.json['usuario_pk']
        
            db.session.commit()
            return tutor_schema.dump(tutor), 200
        except ValidationError as err:
            return err.messages,400
       