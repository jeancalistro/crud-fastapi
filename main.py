from fastapi import Depends, FastAPI, HTTPException
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

@app.get("/aluno/list", response_model=list[schemas.Response_Aluno], status_code = 200)
def read(aluno_service : Aluno_Service = Depends(get_service)):
    return aluno_service.get_alunos()

@app.post("/aluno/new", response_model = schemas.Response_Aluno, status_code = 201)
def create(aluno : schemas.Create_Aluno, aluno_service : Aluno_Service = Depends(get_service)):
    try:
        return aluno_service.create_aluno(aluno)
    except Exception as exception:
        raise HTTPException(status_code=409, detail=exception.__str__())

@app.put("/aluno/update/{id}", response_model = schemas.Response_Aluno)
def update(id : int, aluno_data: schemas.Update_Aluno, aluno_service : Aluno_Service = Depends(get_service)):
    try:
        return aluno_service.update_aluno(id, new_data = aluno_data)
    except Exception as exception:
        raise HTTPException(status_code = 400, detail = exception.__str__())

@app.delete("/aluno/delete/{id}", status_code = 204)
def delete(id : int, aluno_service : Aluno_Service = Depends(get_service)):
    try:
        aluno_service.remove_aluno(id)
    except Exception as exception:
        raise HTTPException(status_code = 400, detail = exception.__str__())
        