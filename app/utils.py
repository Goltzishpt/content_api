from hashlib import sha256


def get_password_hash(password: str) -> str:
    return sha256(password.encode('utf-8')).hexdigest()


class Validator:
    username: str = False
    phone: str = False
    login: str = False
    password: str = False

    def validator_login(self):
        pass
