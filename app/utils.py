from hashlib import sha256


def get_password_hash(password: str) -> str:
    return sha256(password.encode('utf-8')).hexdigest()

