from pydantic import BaseModel

class Aluno(BaseModel):
    class Config:
        orm_mode = True

class Create_Aluno(Aluno):
    name: str
    email: str
    password : str

class Update_Aluno(Aluno):
    name: str
    email: str
    password : str
    pass

class Response_Aluno(Aluno):
    id: int
    email: str
    name: str

class Public_Response_Aluno(Aluno):
    name: str

class From_Token(Aluno):
    id: int
    name: str
    email: str
    password: str

class Auth_Aluno(Aluno):
    email: str
    password: str