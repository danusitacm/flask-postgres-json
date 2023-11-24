from app.extensions import db 
from app.models.tutor_materia import tutor_materia

class Materia(db.Model):
    __tablename__='materia'
    materia_pk=db.Column(db.Integer(), primary_key=True)
    nombre=db.Column(db.String(255))
    codigo=db.Column(db.String(255))
    
    #Relaciones
    solicitud = db.relationship('Solicitud', back_populates='materia')
    tutor= db.relationship('Tutor',secondary=tutor_materia, back_populates='materia')
    
    def __init__(self,nombre,codigo) -> None:
        self.nombre = nombre
        self.codigo =codigo

    
    def __repr__(self):
        return '<Materia_pk {}>'.format(self.materia_pk)
    