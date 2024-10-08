from sqlalchemy import Column, Integer, String
from database import Base

class Aluno(Base):
    __tablename__ = "alunos"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=False)
    email = Column(String, unique=True)
    password_hash = Column(String, unique=False)