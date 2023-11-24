from app.extensions import db 

class TutorMateria(db.Model):
    __tablename__='tutor_materia'
    materia_pk=db.Column(db.Integer(), primary_key=True)
    alumno_pk=db.Column(db.Integer(), primary_key=True)
    
    #Relaciones
    alumno = db.relationship('Alumno', back_populates='tutor_materia')
    materia = db.relationship('Materia', back_populates='tutor_materia')
    
    def __init__(self,materia_pk,alumno_pk) -> None:
        self.materia_pk = materia_pk
        self.alumno_pk =alumno_pk

