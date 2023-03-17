from app import config
from app.routes import app
from app import engine
from app.models import Base


Base.metadata.create_all(engine)

app.run(host=config.HOST, port=config.PORT, debug=True)


