from app.extensions import db 


class ReviewTutor(db.Model):
    __tablename__='review_tutor'
    review_tutor_pk = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(255))
    calificacion_tutor = db.Column(db.String(255))
    tutor_pk = db.Column(db.Integer,db.ForeignKey('tutor.tutor_pk'),nullable=False)
    alumno_pk = db.Column(db.Integer,db.ForeignKey('alumno.alumno_pk'),nullable=False)
    
    # Relaciones
    alumno = db.relationship('Alumno', back_populates='review_tutor')
    tutor = db.relationship('Tutor', back_populates='review_tutor')

    def __init__(self,descripcion ,calificacion_tutor,alumno_pk,tutor_pk) -> None:
        self.descripcion = descripcion
        self.calificacion_tutor = calificacion_tutor
        self.alumno_pk = alumno_pk
        self.tutor_pk = tutor_pk
        
        

    def __repr__(self):
        return '<review_tutor_pk {}>'.format(self.review_tutor_pk)
    