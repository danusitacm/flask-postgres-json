import sqlite3

# Conectar a la base de datos SQLite (creará el archivo 'student_database.db' si no existe)
conn = sqlite3.connect('student_database.db')
print("Opened database successfully")

# Crear la tabla 'usuario'
conn.execute('''
    CREATE TABLE usuario (
        usuario_pk INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        email TEXT NOT NULL,
        telefono TEXT NOT NULL,
        genero TEXT NOT NULL
    )
''')

# Crear la tabla 'materia'
conn.execute('''
    CREATE TABLE materia (
        materia_pk INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        codigo TEXT NOT NULL
    )
''')

# Crear la tabla 'tutor'
conn.execute('''
    CREATE TABLE tutor (
        tutor_pk INTEGER PRIMARY KEY AUTOINCREMENT,
        puntaje_tutor REAL NOT NULL,
        nombre TEXT NOT NULL,
        email TEXT NOT NULL,
        telefono TEXT NOT NULL,
        genero TEXT NOT NULL
    )
''')

# Crear la tabla 'tutor_materia'
conn.execute('''
    CREATE TABLE tutor_materia (
        tutor_pk INTEGER NOT NULL,
        materia_pk INTEGER NOT NULL,
        PRIMARY KEY (tutor_pk, materia_pk),
        FOREIGN KEY (tutor_pk) REFERENCES tutor (tutor_pk),
        FOREIGN KEY (materia_pk) REFERENCES materia (materia_pk)
    )
''')

# Crear la tabla 'alumno'
conn.execute('''
    CREATE TABLE alumno (
        alumno_pk INTEGER PRIMARY KEY AUTOINCREMENT,
        puntaje_alumno REAL NOT NULL,
        nombre TEXT NOT NULL,
        email TEXT NOT NULL,
        telefono TEXT NOT NULL,
        genero TEXT NOT NULL
    )
''')

# Crear la tabla 'review_alumno'
conn.execute('''
    CREATE TABLE review_alumno (
        review_alumno_pk INTEGER PRIMARY KEY AUTOINCREMENT,
        descripcion TEXT NOT NULL,
        calificacion_alumno INTEGER DEFAULT 0 NOT NULL,
        tutor_pk INTEGER NOT NULL,
        alumno_pk INTEGER NOT NULL,
        FOREIGN KEY (tutor_pk) REFERENCES tutor (tutor_pk),
        FOREIGN KEY (alumno_pk) REFERENCES alumno (alumno_pk)
    )
''')

# Crear la tabla 'review_tutor'
conn.execute('''
    CREATE TABLE review_tutor (
        review_tutor_pk INTEGER PRIMARY KEY AUTOINCREMENT,
        descripcion TEXT NOT NULL,
        calificacion_tutor INTEGER DEFAULT 0 NOT NULL,
        tutor_pk INTEGER NOT NULL,
        alumno_pk INTEGER NOT NULL,
        FOREIGN KEY (tutor_pk) REFERENCES tutor (tutor_pk),
        FOREIGN KEY (alumno_pk) REFERENCES alumno (alumno_pk)
    )
''')

# Crear la tabla 'tutoria'
conn.execute('''
    CREATE TABLE tutoria (
        tutoria_pk INTEGER PRIMARY KEY AUTOINCREMENT,
        fecha_inicio DATE NOT NULL,
        alumno_pk INTEGER NOT NULL,
        fecha_fin DATE NOT NULL,
        tutor_pk INTEGER NOT NULL,
        materia_pk INTEGER NOT NULL,
        FOREIGN KEY (alumno_pk) REFERENCES alumno (alumno_pk),
        FOREIGN KEY (tutor_pk) REFERENCES tutor (tutor_pk),
        FOREIGN KEY (materia_pk) REFERENCES materia (materia_pk)
    )
''')

# Crear la tabla 'solicitud'
conn.execute('''
    CREATE TABLE solicitud (
        solicitud_pk INTEGER PRIMARY KEY AUTOINCREMENT,
        fecha_solicitud DATE NOT NULL,
        estado_solicitud TEXT NOT NULL,
        alumno_pk INTEGER NOT NULL,
        materia_pk INTEGER NOT NULL,
        FOREIGN KEY (alumno_pk) REFERENCES alumno (alumno_pk),
        FOREIGN KEY (materia_pk) REFERENCES materia (materia_pk)
    )
''')

print("Tables created successfully")
conn.close()
