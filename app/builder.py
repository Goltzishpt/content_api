from app import config
from app.routes import app


app.run(host=config.HOST, port=config.PORT, debug=True)
