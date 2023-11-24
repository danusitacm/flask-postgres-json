from flask import request, jsonify
from app.models.tutor_materia import TutorMateria
from app.extensions import db
from app.schemas.tutor_materia import tutor_materia_schema,tutores_materias_schema
from marshmallow  import ValidationError
from flask import Blueprint

t_m_bp = Blueprint('tutor_materia', __name__,url_prefix="/tutor_materia")

@t_m_bp.route('/',methods=['GET'])
def obtener_materias():
    if request.method == 'GET':
        t_m = TutorMateria.query.all()
        return tutores_materias_schema.dump(t_m)
    
@t_m_bp.route('/<int:id>',methods=['GET'])
def obtener_materia_id(id):
    if request.method == 'GET':
        t_m = TutorMateria.query.get(id)
        return tutor_materia_schema.dump(t_m)

@t_m_bp.route('/',methods= ['POST'])
def agregar_materia():
    if request.method == 'POST':
        try:
            # Validacion
            tutor_materia_schema.load(request.json)
            # Obtenemos los datos del json para validar
            materia_pk = request.json['materia_pk']
            alumno_pk = request.json['alumno_pk']
            nueva_tm = TutorMateria(materia_pk,alumno_pk)

            # agregamos el nuevo materia en la base de datos 
            db.session.add(nueva_tm)
            db.session.commit()

            # Retornamos el materia creado 
            return tutor_materia_schema.dump(nueva_tm), 201
        except ValidationError as err:
            return err.messages, 400
            
        
    
@t_m_bp.route('/<int:id>',methods=['PUT'])
def actualizar_materia(id):
    if request.method == 'PUT':
        try:
            t_m_actualizado = TutorMateria.query.get(id)
            tutor_materia_schema.load(request.json)
            t_m_actualizado.materia_pk = request.json['materia_pk']
            t_m_actualizado.alumno_pk = request.json['alumno_pk']
            db.session.commit()
            return tutor_materia_schema.dump(t_m_actualizado), 200
        except ValidationError as err:
            return err.messages,400
       