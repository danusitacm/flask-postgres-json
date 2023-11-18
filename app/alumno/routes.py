from flask import request, jsonify
from app.alumno import alumno
from app.alumno.models import Alumno
from app.extensions import db

@alumno.route('/',methods=['GET','POST'])
def obtener_alumnos():
    if request.method == 'GET':
        alumno = Alumno.query.all()
        # Convertir los alumnos a JSON
        return jsonify([a.to_json() for a in alumno])
    elif request.method == 'POST':
        nombre=request.json['nombre']
        email=request.json['email']
        telefono=request.json['telefono']
        genero=request.json['genero']
        puntaje_alumno=request.json['puntaje_alumno']
        nuevo_alumno = Alumno(nombre,email,telefono,genero,puntaje_alumno)
        db.session.add(nuevo_alumno)
        db.session.commit()
        return 200
        