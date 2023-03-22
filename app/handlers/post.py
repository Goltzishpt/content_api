from flask import request, jsonify
from datetime import datetime
from app import sessions
from app.loader import app
from app.models import User, Post


def create_post():
    data = request.get_json()
    title = data['title']
    text = data['text']

    token = request.cookies.get('token')

    try:
        user_id = sessions.get(token)

    except:
        return jsonify(success=False)
    Post(title=title, text=text, user_id=user_id, created_at=datetime.utcnow()).save()
    return jsonify(success=True)


def show_all_post():
    objects = Post.objects
    if request.args.get('user_id'):
        user_id = int(request.args.get('user_id'))
        objects = objects.filter(Post.user_id==user_id)

    if request.args.get('order_by') == 'asc':
        objects = objects.order_by(Post.created_at.asc())
    elif request.args.get('order_by') == 'desc':
        objects = objects.order_by(Post.created_at.desc())

    if request.args.get('limit') and request.args.get('offset'):
        limit = int(request.args.get('limit'))
        offset = int(request.args.get('offset'))
        objects = objects.limit(limit).offset(offset)

    posts = [post.to_dict() for post in objects.all()]
    return jsonify(posts=posts)


def show_post(post_id):
    post = Post.objects.filter(Post.id==int(post_id)).one()
    return jsonify(post=post.to_dict())


def update_post(post_id):
    token = request.cookies.get('token')
    try:
        user_id = sessions.get(token)
    except:
        return jsonify(success=False)

    post = Post.objects.filter(Post.id == int(post_id)).one()

    if post.user_id != user_id:
        return jsonify(success=False)

    data = request.get_json()
    title = data['title']
    text = data['text']

    post.update_post(title=title, text=text)
    return jsonify(success=True)


def delete_post(post_id):
    token = request.cookies.get('token')
    try:
        user_id = sessions.get(token)
    except:
        return jsonify(success=False)

    post = Post.objects.filter(Post.id==int(post_id)).first()

    if post.user_id != user_id:
        return jsonify(success=False)
    post.delete()
    return jsonify(success=True)


