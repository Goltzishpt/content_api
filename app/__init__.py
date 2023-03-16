from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from config import POSTGRES_HOST, POSTGRES_PORT, POSTGRES_USER, POSTGRES_NAME, POSTGRES_PASSWORD


Base = declarative_base()
db_url = f'postgres://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_NAME}'
engine = create_engine(db_url, echo=False)
session = sessionmaker(bind=engine)
