from flask import Blueprint

tutor = Blueprint('tutor', __name__)

@tutor.route("/")
def api_home():
    return "<h1>tutores Home</h1>"