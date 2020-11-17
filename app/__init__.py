import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from db.db_settings import *

engine = sqlalchemy.create_engine(
    f'mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}',
    echo=True
)

Base = declarative_base()
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()
