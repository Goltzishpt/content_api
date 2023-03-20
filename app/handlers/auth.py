import psycopg2
from flask import jsonify, request
from flask_login import logout_user
from app.loader import app
from app.models import User
from app.utils import get_password_hash
from app.sessions import set, delete


def homepage():
    return {'data': 'homepage'}


def registration():
    data = request.get_json()
    data['password'] = get_password_hash(data['password'])
    User(name=data.get('name'), phone=data.get('phone'), login=data.get('login'), password=data.get('password')).save()
    return jsonify(data)


def login():
    data = request.get_json()
    username = data['login']
    password = get_password_hash(data['password'])
    conn = psycopg2.connect(database="ps_db", user="test",
                            password="admin", host="localhost", port=5432)
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT id, password FROM "user" WHERE login =%s', (username,))
        cur_data = cursor.fetchone()
        if cur_data is not None:
            if cur_data[1] == password:
                out = jsonify(state=0, msg='success')
                out.set_cookie('token', set(cur_data[0]), httponly=True)
                return out
            else:
                return 'Incorrect password!'
        else:
            return 'User not found!'
    finally:
        conn.close()


def logout():
    data = request.get_json()
    username = data['login']
    password = get_password_hash(data['password'])
    conn = psycopg2.connect(database="ps_db", user="test",
                            password="admin", host="localhost", port=5432)
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT id, password FROM "user" WHERE login =%s', (username,))
        cur_data = cursor.fetchone()
        if cur_data[1] == password:
            out = jsonify(state=0, msg='delete')
            out.delete_cookie('token', set(cur_data[0]), httponly=True)
            delete(set(cur_data[0]))
            return out
    finally:
        conn.close()


