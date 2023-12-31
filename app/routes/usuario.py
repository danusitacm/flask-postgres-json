from flask import request, jsonify
from app.models.usuario import Usuario
from app.extensions import db
from app.schemas.usuario import usuario_schema , usuarios_schema
from marshmallow import ValidationError
from flask import Blueprint

usuario_bp = Blueprint('usuario',__name__,url_prefix='/usuarios')

@usuario_bp.route('/',methods=['GET'])
def obtener_usuarios():
    if request.method == 'GET':
        usuario = Usuario.query.all()
        return usuarios_schema.dump(usuario)
    
@usuario_bp.route('/<int:id>',methods=['GET'])
def obtener_usuario_id(id):
    if request.method == 'GET':
        usuario = Usuario.query.get(id)
        return usuario_schema.dump(usuario)

@usuario_bp.route('/',methods= ['POST'])
def agregar_usuario():
    if request.method == 'POST':
        try:
            # Validacion
            usuario_schema.load(request.json)
            # Obtenemos los datos del json para validar
            nombre = request.json['nombre']
            email = request.json['email']
            telefono = request.json['telefono']
            genero = request.json['genero']
            nuevo_usuario = Usuario(nombre, email, telefono, genero)

            # agregamos el nuevo usuario en la base de datos 
            db.session.add(nuevo_usuario)
            db.session.commit()

            # Retornamos el usuario creado 
            return usuario_schema.dump(nuevo_usuario), 201
        except ValidationError as err:
            return err.messages, 400
            
        
    
@usuario_bp.route('/<int:id>',methods=['PUT'])
def actualizar_usuario(id):
    if request.method == 'PUT':
        try:
            usuario = Usuario.query.get(id)
            usuario_schema.load(request.json)
            usuario.nombre=request.json['nombre']
            usuario.email=request.json['email']
            usuario.telefono=request.json['telefono']
            usuario.genero=request.json['genero']
            db.session.commit()
            return usuario_schema.dump(usuario), 200
        except ValidationError as err:
            return err.messages,400
       