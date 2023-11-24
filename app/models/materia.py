from app.extensions import db 

class Materia(db.Model):
    __tablename__='materia'
    materia_pk=db.Column(db.Integer(), primary_key=True)
    nombre=db.Column(db.String(255))
    codigo=db.Column(db.String(255))
    
    #Relaciones
    solicitud = db.relationship('Solicitud', back_populates='materia')
    tutor_materia = db.relationship('TutorMateria', back_populates='materia')    
    
    def __init__(self,nombre,codigo) -> None:
        self.nombre = nombre
        self.codigo =codigo

    
    def __repr__(self):
        return '<Materia_pk {}>'.format(self.materia_pk)
    