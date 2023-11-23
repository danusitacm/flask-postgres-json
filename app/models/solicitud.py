from app.extensions import db 


class Solicitud(db.Model):
    __tablename__='solicitud'
    solicitud_pk = db.Column(db.Integer, primary_key=True)
    fecha_solicitud = db.Column(db.Date)
    estado_solicitud = db.Column(db.String(255))
    materia_pk = db.Column(db.Integer,db.ForeignKey('materia.materia_pk'),nullable=False)
    alumno_pk = db.Column(db.Integer,db.ForeignKey('alumno.alumno_pk'),nullable=False)
    
    # Relaciones
    alumno = db.relationship('Alumno', back_populates='solicitud')
    materia = db.relationship('Materia', back_populates='solicitud')

    def __init__(self,fecha_solicitud,estado_solicitud,materia_pk,alumno_pk) -> None:
        self.fecha_solicitud = fecha_solicitud
        self.estado_solicitud = estado_solicitud
        self.materia_pk = materia_pk
        self.alumno_pk = alumno_pk
        

    def __repr__(self):
        return '<solicitud_pk {}>'.format(self.solicitud_pk)
    