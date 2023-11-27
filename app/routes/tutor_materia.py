from flask import jsonify, request, Blueprint
from app.extensions import db
from app.models import Tutor, Materia
from app.schemas.tutor import tutor_schema, tutors_schema
from app.schemas.materia import materia_schema, materias_schema


tutor_materia_bp = Blueprint('tutor_materia', __name__, url_prefix="/tutor_materia")

@tutor_materia_bp.route('/materias_asignadas/<int:tutor_pk>', methods=['GET'])
def obtener_materias_de_tutor(tutor_pk):
    tutor = Tutor.query.get_or_404(tutor_pk)
    materias_asignadas = tutor.materia
    return materias_schema.dump(materias_asignadas)

@tutor_materia_bp.route('/tutores_asociados/<int:materia_pk>', methods=['GET'])
def obtener_tutores_asociados_materia(materia_pk):
    materia = Materia.query.get_or_404(materia_pk)
    tutores_asociados = materia.tutor
    return tutors_schema.dump(tutores_asociados)


@tutor_materia_bp.route('/asignar_materia', methods=['POST'])
def asignar_materia_a_tutor():
    data = request.json
    tutor_id = data.get('tutor_pk')
    materia_id = data.get('materia_pk')

    tutor = Tutor.query.get_or_404(tutor_id)
    materia = Materia.query.get_or_404(materia_id)

    tutor.materia.append(materia)
    materia.tutor.append(tutor)
    db.session.commit()

    return jsonify(message=f'Materia asignada al Tutor {tutor_id} correctamente'), 201


@tutor_materia_bp.route('/desasignar_materia/<int:tutor_pk>/<int:materia_pk>', methods=['DELETE'])
def desasignar_materia_de_tutor(tutor_pk,materia_pk):
    tutor = Tutor.query.get_or_404(tutor_pk)
    materia = Materia.query.get_or_404(materia_pk)

    tutor.materia.remove(materia)
    db.session.commit()

    return jsonify(message=f'Materia desasignada del Tutor {tutor_pk} correctamente'), 200