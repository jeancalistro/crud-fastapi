from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

DB_URL = os.getenv("DB_URL")

SQLALCHEMY_DATABASE_URL = f"{DB_URL}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
new_session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    session = new_session()
    try:
        yield session
    finally:
        session.close()