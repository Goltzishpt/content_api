import psycopg2
from flask import request, jsonify
from datetime import datetime
from app import session
from app.loader import app
from app.models import User, Post
from app.sessions import get


def create_post():
    data = request.get_json()
    title = data['title']
    text = data['text']

    token = request.cookies.get('token')
    if not token:
        return 'Unauthorized!'

    conn = psycopg2.connect(database="ps_db", user="test",
                            password="admin", host="localhost", port=5432)
    print(get(token))
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT id FROM "user" WHERE id =%s', (get(token),))
        user_id = cursor.fetchone()
        if not user_id:
            return 'Unauthorized!'
        else:
            cursor.execute('INSERT into post (title, text, user_id, created_at) VALUES (%s, %s, %s, %s)',
                           (title, text, user_id, datetime.utcnow()))
            conn.commit()
            return 'Post created!'
    finally:
        conn.close()



def show_all_post():
    pass


def show_post():
    pass


def update_post():
    pass


def delete_post():
    pass
