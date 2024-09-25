from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from database import engine, get_db
from repository import Aluno_Repository
from services import Aluno_Service
import models, schemas

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

def get_repository(session : Session = Depends(get_db)):
    return Aluno_Repository(session)

def get_service(repository : Aluno_Repository = Depends(get_repository)):
    return Aluno_Service(repository)

@app.get("/aluno/list", response_model=list[schemas.Response_Aluno])
def read(aluno_service : Aluno_Service = Depends(get_service)):
    alunos = aluno_service.get_alunos(limit = 50)
    return alunos

@app.post("/aluno/new", response_model = schemas.Response_Aluno)
def create(aluno : schemas.Create_Aluno, session : Session = Depends(get_db)):
    return Aluno_Repository.add_aluno(aluno = aluno, session_db = session)

@app.put("/aluno/update/{id}", response_model = schemas.Response_Aluno)
def update(id : int, aluno_data: schemas.Update_Aluno, session : Session = Depends(get_db)):
    return Aluno_Repository.update_aluno(aluno_id = id, new_aluno_data = aluno_data, session_db = session)

@app.delete("/aluno/delete/{id}", response_model=schemas.Response_Aluno)
def delete(id : int, session : Session = Depends(get_db)):
    return Aluno_Repository.delete_aluno(aluno_id = id, session_db = session)
        