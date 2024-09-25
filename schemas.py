from pydantic import BaseModel

class Aluno(BaseModel):
    name: str
    email: str

    class Config:
        orm_mode = True

class Create_Aluno(Aluno):
    pass

class Update_Aluno(Aluno):
    pass

class Delete_Aluno(Aluno):
    pass

class Response_Aluno(Aluno):
    id: int