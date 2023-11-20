from flask import request, jsonify
from app.materia import materia
from app.materia.models import Materia
from app.extensions import db
from .schemas import materia_schema, materias_schema
from marshmallow  import ValidationError

@materia.route('/',methods=['GET'])
def obtener_materias():
    if request.method == 'GET':
        materia = Materia.query.all()
        return materias_schema.dump(materia)
    
@materia.route('/<int:id>',methods=['GET'])
def obtener_materia_id(id):
    if request.method == 'GET':
        materia = Materia.query.get(id)
        return materia_schema.dump(materia)

@materia.route('/',methods= ['POST'])
def agregar_materia():
    if request.method == 'POST':
        try:
            # Validacion
            materia_schema.load(request.json)
            # Obtenemos los datos del json para validar
            nombre = request.json['nombre']
            codigo = request.json['codigo']
            nueva_materia = Materia(nombre,codigo)

            # agregamos el nuevo materia en la base de datos 
            db.session.add(nueva_materia)
            db.session.commit()

            # Retornamos el materia creado 
            return materia_schema.dump(nueva_materia), 201
        except ValidationError as err:
            return err.messages, 400
            
        
    
@materia.route('/<int:id>',methods=['PUT'])
def actualizar_materia(id):
    if request.method == 'PUT':
        try:
            materia = materia.query.get(id)
            materia_schema.load(request.json)
            nombre = request.json['nombre']
            codigo = request.json['codigo']
            materia = Materia(nombre,codigo)
            db.commit()
            return materia_schema.dump(request.json), 200
        except ValidationError as err:
            return err.messages,400
       