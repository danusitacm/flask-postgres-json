from app.extensions import db 


class ReviewAlumno(db.Model):
    __tablename__='review_alumno'
    review_alumno_pk = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(255))
    calificacion_alumno= db.Column(db.Float())
    tutor_pk = db.Column(db.Integer,db.ForeignKey('tutor.tutor_pk'),nullable=False)
    alumno_pk = db.Column(db.Integer,db.ForeignKey('alumno.alumno_pk'),nullable=False)
    
    # Relaciones
    alumno = db.relationship('Alumno', back_populates='review_alumno')
    tutor = db.relationship('Tutor', back_populates='review_alumno')

    def __init__(self,descripcion ,calificacion_alumno,alumno_pk,tutor_pk) -> None:
        self.descripcion = descripcion
        self.calificacion_alumno = calificacion_alumno
        self.alumno_pk = alumno_pk
        self.tutor_pk = tutor_pk
        
        

    def __repr__(self):
        return '<review_alumno_pk {}>'.format(self.review_alumno_pk)
    