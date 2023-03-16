from app import config
import redis
from uuid import uuid4


def __connection() -> redis.Redis:
    r = redis.Redis(host=config.REDIS_HOST, port=config.REDIS_PORT, db=config.REDIS_DB)
    return r


def set(user_id: int) -> str:
    token = uuid4().hex
    r = __connection()
    r.set(name=token, value=user_id)
    r.close()
    return token


def get(token: str) -> int:
    r = __connection()
    user_id = r.get(name=token)
    r.close()
    return user_id


def delete(token: str) -> None:
    r = __connection()
    r.delete(token)
    r.close()
