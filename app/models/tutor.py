from app.extensions import db 
from app.models.tutor_materia import tutor_materia
class Tutor(db.Model):
    __tablename__='tutor'
    tutor_pk=db.Column(db.Integer(), primary_key=True)
    puntaje_tutor=db.Column(db.Float())
    usuario_pk=db.Column(db.Integer, db.ForeignKey('usuario.usuario_pk'),nullable=False)
    
    # Relaciones 
    usuario = db.relationship('Usuario', back_populates='tutores', uselist=False)
    materia= db.relationship('Materia',secondary=tutor_materia, back_populates='tutor')

    
    def __init__(self,puntaje_tutor,usuario_pk) -> None:
        self.puntaje_tutor = puntaje_tutor
        self.usuario_pk =usuario_pk

    
    def __repr__(self):
        return '<Tutor_pk {}>'.format(self.tutor_pk)
    