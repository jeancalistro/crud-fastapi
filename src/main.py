from fastapi import Depends, FastAPI, HTTPException, Request
from sqlalchemy.orm import Session
from database import engine, get_db
from repository import Aluno_Repository
from services import Aluno_Service
import models, schemas, exceptions, utils

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_repository(session : Session = Depends(get_db)):
    return Aluno_Repository(session)


def get_service(repository : Aluno_Repository = Depends(get_repository)):
    return Aluno_Service(repository)


def get_token(request : Request):
    try:
        token : str = request.headers["Authorization"]
        if(token):
            return token.replace("Bearer ", "")
    except:
        pass
    

def valid_token(token : str = Depends(get_token)):
    try:
        return utils.verify_token(token)
    except exceptions.Invalid_Token as exception:
        raise HTTPException(status_code = exception.error_code, detail=exception.__str__())


@app.get("/alunos", response_model=list[schemas.Public_Response_Aluno], status_code = 200)
def read_all(aluno_service : Aluno_Service = Depends(get_service)):
    return aluno_service.get_alunos()
    

@app.get("/aluno", response_model=schemas.Response_Aluno, status_code = 200)
def read(aluno_service : Aluno_Service = Depends(get_service), aluno_from_token: schemas.From_Token = Depends(valid_token)):
    try:
        return aluno_service.get_aluno(aluno_from_token)
    except exceptions.Aluno_Not_Exists as exception:
        raise HTTPException(status_code = exception.error_code, detail=exception.__str__())


@app.post("/aluno/new", response_model = schemas.Response_Aluno, status_code = 201)
def create(aluno : schemas.Create_Aluno, aluno_service : Aluno_Service = Depends(get_service)):
    try:
        return aluno_service.create_aluno(aluno)
    except exceptions.Aluno_Already_Exists as exception:
        raise HTTPException(status_code = exception.error_code, detail=exception.__str__())


@app.put("/aluno/update", response_model = schemas.Response_Aluno, status_code = 201)
def update(aluno_data: schemas.Update_Aluno, aluno_service : Aluno_Service = Depends(get_service), aluno_from_token = Depends(valid_token)):
    try:
        return aluno_service.update_aluno(aluno_from_token, new_data = aluno_data)
    except (exceptions.Aluno_Not_Exists, exceptions.Email_Already_Registered) as exception:
        raise HTTPException(status_code = exception.error_code, detail = exception.__str__())


@app.delete("/aluno/delete", status_code = 204)
def delete(aluno_service : Aluno_Service = Depends(get_service), aluno_from_token = Depends(valid_token)):
    try:
        aluno_service.remove_aluno(aluno_from_token)
    except exceptions.Aluno_Not_Exists as exception:
        raise HTTPException(status_code = exception.error_code, detail = exception.__str__())


@app.post("/auth", status_code = 200, response_model = schemas.Token)
def login(aluno_data : schemas.Auth_Aluno, aluno_service : Aluno_Service = Depends(get_service)):
    try:
        return {"token" : aluno_service.auth_aluno(aluno_data)}
    except (exceptions.Aluno_Not_Exists, exceptions.Incorret_Crendials) as exception:
        raise HTTPException(status_code = exception.error_code, detail = exception.__str__())