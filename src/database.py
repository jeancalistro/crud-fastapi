from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:mysecretpassword@db/crud"

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