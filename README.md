
# FLASK-POTSGRES-JSON

Hay que crear la base de datos 
El script de la base de datos esta en 
flask-postgres-json/app/tutoria-sos.sql

## Variables de entorno 
Para ejecutar este proyecto, deberá agregar las siguientes variables de entorno a su archivo .env

`POSTGRES_USER`= "Nombre_usuario"

`POSTGRES_PWD`= "Contraseña"

`POSTGRES_DB`= "Nombre_base_datos"

`DATABASE_URL`= "postgresql://${POSTGRES_USER}:${POSTGRES_PWD}@localhost:5432/${POSTGRES_DB}"


## Run Locally

Clonar el proyecto
```bash
  git clone https://github.com/danusitacm/flask-postgres-json
```
Ir al archivo del proyecto
```bash
  cd flask-postgres-json
```
Crear el entorno virtual
```bash
python -m venv .venv
```
Instalar las dependencias 
```bash
pip install -r requirements.txt
```
Iniciar el servidor 
```bash
python run.py
```

