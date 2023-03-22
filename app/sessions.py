import jwt
from flask import request
import redis
from uuid import uuid4
from app import config
from app.loader import app


def __connection() -> redis.Redis:
    r = redis.Redis(host=config.REDIS_HOST, port=config.REDIS_PORT, db=config.REDIS_DB)
    return r


def set(user_id: int) -> str:
    token = uuid4().hex
    r = __connection()
    r.set(name=token, value=user_id)
    r.close()
    encode_token = jwt.encode({'token': token}, config.SECRET_KEY)
    return encode_token


def get(token: str) -> int:
    decoded_token = jwt.decode(token, config.SECRET_KEY, algorithms=['HS256'])
    r = __connection()
    user_id = r.get(name=decoded_token.get('token'))
    user_id_int = int(user_id.decode('utf-8'))
    r.close()
    return user_id_int


def delete(token: str) -> None:
    decoded_token = jwt.decode(token, config.SECRET_KEY, algorithms=['HS256'])
    r = __connection()
    r.delete(decoded_token.get('token'))
    r.close()

