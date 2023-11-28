from app.extensions import db 


class Tutoria(db.Model):
    __tablename__='tutoria'
    tutoria_pk = db.Column(db.Integer, primary_key=True)
    fecha_inicio = db.Column(db.Date)
    fecha_fin = db.Column(db.Date)
    materia_pk = db.Column(db.Integer,db.ForeignKey('materia.materia_pk'),nullable=False)
    alumno_pk = db.Column(db.Integer,db.ForeignKey('alumno.alumno_pk'),nullable=False)
    tutor_pk = db.Column(db.Integer,db.ForeignKey('tutor.tutor_pk'),nullable=False)
    # Relaciones
    alumno = db.relationship('Alumno', back_populates='tutoria')
    materia = db.relationship('Materia', back_populates='tutoria')
    tutor= db.relationship('Tutor', back_populates='tutoria')
    
    def __init__(self,fecha_inicio,fecha_fin,materia_pk,alumno_pk,tutor_pk) -> None:
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.materia_pk = materia_pk
        self.alumno_pk = alumno_pk
        self.tutor_pk = tutor_pk
        

    def __repr__(self):
        return '<tutoria_pk {}>'.format(self.tutoria_pk)
    