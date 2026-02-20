from sqlalchemy import create_engine
from config.config import url_postgres
from model.base import Base
from sqlalchemy.orm import sessionmaker

engine = create_engine(url_postgres)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()