from app.loader import app
from app.handlers import auth


@app.route('/')
def get_homepage():
    return 'homepage'


@app.route('/registration')
def get_registration():
    return auth.registration()


@app.route('/login')
def get_login():
    return auth.login()


@app.route('/logout')
def deg_logout():
    return auth.logout()


