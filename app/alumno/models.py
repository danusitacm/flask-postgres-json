from app.extensions import db 
import json
class Alumno(db.Model):
    __tablename__='alumno'
    id_usuario = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String())
    email = db.Column(db.String())
    telefono = db.Column(db.String())
    genero = db.Column(db.String())
    alumno_pk=db.Column(db.Integer())
    puntaje_alumno=db.Column(db.Float())
    
    def __init__(self,nombre,email,telefono,genero,alumno_pk,puntaje_alumno) -> None:
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
        self.genero = genero
        self.alumno_pk =alumno_pk
        self.puntaje_alumno = puntaje_alumno
        
    def to_json (self):
        return json.dumps(dict(id_usuario=self.id_usuario,
                               nombre=self.nombre,
                               email=self.email,
                               telefono=self.telefono,
                               genero=self.genero,
                               alumno_pk=self.alumno_pk,
                               puntaje_alumno=self.puntaje_alumno))
    