import psycopg2
from flask import jsonify, request, make_response
from flask_login import logout_user
from app.loader import app
from app.models import User
from app.utils import get_password_hash
from app import sessions
import sqlalchemy


def homepage():
    return {'data': 'homepage'}


def registration():
    data = request.get_json()
    data['password'] = get_password_hash(data['password'])
    try:
        User(name=data.get('name'), phone=data.get('phone'), login=data.get('login'), password=data.get('password')).save()
    except:
        return jsonify(success=False)
    return jsonify(success=True)


def login():
    data = request.get_json()
    username = data['login']
    password = get_password_hash(data['password'])
    
    try:
        user: User = User.objects.filter(User.login==username, User.password==password).one()
        out = jsonify(success=True)
        out.set_cookie('token', sessions.set(user.id), httponly=True)
        return out
    except:
        return jsonify(success=False)


def logout():
    data = request.get_json()
    username = data['login']
    password = get_password_hash(data['password'])

    try:

    except:
        return jsonify(success=False)


