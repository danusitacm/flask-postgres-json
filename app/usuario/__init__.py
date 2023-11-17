from flask import Blueprint

usuario = Blueprint('usuario', __name__)

@usuario.route("/")
def api_home():
    return "<h1>usuarios Home</h1>"