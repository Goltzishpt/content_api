from flask import jsonify, request
from app.utils import get_password_hash
from app.loader import app


def homepage():
    return {'data': 'homepage'}


def registration():
    data = request.get_json()
    data['password'] = get_password_hash(data['password'])
    return jsonify(data)


def login():
    return 'login'


def logout():
    return 'logout'


