from app.extensions import db 


class Usuario(db.Model):
    __tablename__='usuario'
    usuario_pk = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255))
    email = db.Column(db.String(255))
    telefono = db.Column(db.String(255))
    genero = db.Column(db.String(255))
    
    # Relaciones
    alumno = db.relationship('Alumno', back_populates='usuario', uselist=False)
    tutores = db.relationship('Tutor', back_populates='usuario',uselist=False)

    def __init__(self,nombre,email,telefono,genero) -> None:
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
        self.genero = genero
        

    def __repr__(self):
        return '<usuario_pk {}>'.format(self.usuario_pk)
    