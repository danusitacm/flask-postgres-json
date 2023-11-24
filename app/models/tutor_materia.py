from app.extensions import db 

class TutorMateria(db.Model):
    __tablename__='tutor_materia'
    materia_pk=db.Column("materia_pk",db.Integer(),db.ForeignKey("materia.materia_pk"), primary_key=True)
    tutor_pk=db.Column("tutor_pk",db.Integer(),db.ForeignKey("tutor.tutor_pk"),primary_key=True)
    
    #Relaciones
    tutor = db.relationship('Tutor', back_populates='materias')
    materia = db.relationship('Materia', back_populates='tutores')
    
    def __init__(self,materia_pk,alumno_pk) -> None:
        self.materia_pk = materia_pk
        self.alumno_pk =alumno_pk

