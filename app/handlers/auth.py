from app.builder import app


@app.post
def registration():
    return 'registration'


@app.post
def login():
    return 'login'


@app.post
def logout():
    return 'logout'
