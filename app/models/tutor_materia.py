from app.extensions import db 


# Tabla de unión para la relación muchos a muchos
tutor_materia = db.Table('tutor_materia',
                        db.Column('materia_pk', db.Integer, db.ForeignKey('materia.materia_pk'), primary_key=True),
                        db.Column('tutor_pk', db.Integer, db.ForeignKey('tutor.tutor_pk'), primary_key=True))