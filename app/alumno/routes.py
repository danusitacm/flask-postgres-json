from app.alumno import alumno

@alumno.route('/')
def alumno_home():
    return "<h1>alumnos Home</h1>"