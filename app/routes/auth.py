from flask import request, jsonify
from app.extensions import db
from flask import Blueprint

auth_bp = Blueprint('auth', __name__,)
@auth_bp.route('/login')
def login():
    return 'Login'

@auth_bp.route('/signup')
def signup():
    return 'Signup'

@auth_bp.route('/logout')
def logout():
    return 'Logout'