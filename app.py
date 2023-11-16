from flask import Flask, render_template, request, redirect, session,jsonify
import sqlite3 as sql
import json
app = Flask(__name__)
app.secret_key = 'fasdgfdgdfg'
     
@app.route("/", methods=["GET"])
def index():
   return ("Hola mundo")

@app.route('/post_json', methods=['POST'])
def process_json():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.json
        return json
    else:
        return 'Content-Type not supported!'

def insert_data(query,values):
      try:
         conn = sql.connect('student_database.db')
         cursor = conn.cursor()
         cursor.execute(query,values)
         conn.commit()
         conn.close()
         msg = "Record successfully added!"
      except Exception as e:
         msg = f"Error in insert operation: {e}"
      return msg
   
@app.route('/agregaralumno',methods = ['POST', 'GET'])
def agregar_alumno():
   if request.method == 'POST':
      try:
         data=request.json
         print(data)
         values = list(data.values())
         print(values)
        # Crear y ejecutar la consulta SQL para insertar datos
         query ="INSERT INTO alumno (puntaje_alumno, nombre, email, telefono, genero) VALUES (?, ?, ?, ?, ?)"
         msg = insert_data(query,values)
      except Exception as e:
         msg = f"Error in insert operation: {e}"
      return msg

@app.route('/veralumno', methods=['GET'])
def obtener_alumnos():
    try:
        with sql.connect('student_database.db') as conn:
            conn.row_factory = sql.Row
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM alumno")
            alumno = [dict(row) for row in cursor.fetchall()]
            print(alumno)
        return jsonify({"alumno": alumno})
    except Exception as e:
        return jsonify({"error": f"Error fetching data: {e}"}), 500


if __name__ == '__main__':
   app.run(debug = True)