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
    data = request.get_json()
    data['password'] = get_password_hash(data['password'])
    return jsonify(data)


def logout():
    data = request.get_json()
    return jsonify(data)


