from app import config
from app.routes import app
from app import Base, engine


app.run(host=config.HOST, port=config.PORT, debug=True)

Base.metadata.create_all(engine)
