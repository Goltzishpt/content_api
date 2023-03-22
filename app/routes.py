from app.loader import app
from app.handlers import auth, post


app.add_url_rule('/registration', view_func=auth.registration, methods=['POST'])
app.add_url_rule('/login', view_func=auth.login, methods=['POST'])
app.add_url_rule('/logout', view_func=auth.logout, methods=['POST'])

app.add_url_rule('/post', view_func=post.create_post, methods=['POST'])
app.add_url_rule('/post', view_func=post.show_all_post, methods=['GET'])
app.add_url_rule('/post/{post_id}', view_func=post.show_post, methods=['GET'])
app.add_url_rule('/post/{post_id}', view_func=post.update_post, methods=['PUT'])
app.add_url_rule('/post/{post_id}', view_func=post.delete_post, methods=['DELETE'])
