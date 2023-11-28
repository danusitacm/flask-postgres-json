from app.extensions import db 

class Alumno(db.Model):
    __tablename__='alumno'
    alumno_pk=db.Column(db.Integer(), primary_key=True)
    puntaje_alumno=db.Column(db.Float())
    usuario_pk=db.Column(db.Integer, db.ForeignKey('usuario.usuario_pk'),nullable=False)
    
    # Relaciones 
    usuario = db.relationship('Usuario', back_populates='alumno', uselist=False)
    solicitud = db.relationship('Solicitud', back_populates='alumno')
    tutoria = db.relationship('Tutoria', back_populates='alumno')
    review_tutor = db.relationship('ReviewTutor', back_populates='alumno')
    review_alumno = db.relationship('ReviewAlumno', back_populates='alumno')

    def __init__(self,puntaje_alumno,usuario_pk) -> None:
        self.puntaje_alumno = puntaje_alumno
        self.usuario_pk =usuario_pk

    
    def __repr__(self):
        return '<alumno_pk {}>'.format(self.alumno_pk)
    