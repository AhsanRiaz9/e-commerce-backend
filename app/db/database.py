from sqlalchemy import create_engine

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv('.env')  # take environment variables from .env.


import os
SQLALCHEMY_URL_DATABASE = os.environ.get('DATABASE_URL')


engine = create_engine(SQLALCHEMY_URL_DATABASE)

SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
