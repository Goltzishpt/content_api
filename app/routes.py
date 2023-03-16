from app.loader import app
from app.handlers import auth


app.add_url_rule('/', view_func=auth.homepage)

app.add_url_rule('/registration', view_func=auth.registration, methods=['POST', 'GET'])
app.add_url_rule('/login', view_func=auth.login, methods=['POST', 'GET'])
app.add_url_rule('/logout', view_func=auth.logout, methods=['POST', 'GET'])



