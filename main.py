from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from database import engine, get_db
import repository, models, schemas

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

@app.get("/aluno/list", response_model=list[schemas.Response_Aluno])
def read(session : Session = Depends(get_db)):
    alunos = repository.get_alunos(limit = 50, session_db=session)
    return alunos

@app.post("/aluno/new", response_model = schemas.Response_Aluno)
def create(aluno : schemas.Create_Aluno, session : Session = Depends(get_db)):
    return repository.create_aluno(aluno = aluno, session_db = session)

@app.put("/aluno/update/{id}", response_model = schemas.Response_Aluno)
def update(id : int, aluno_data: schemas.Update_Aluno, session : Session = Depends(get_db)):
    return repository.update_aluno(aluno_id = id, new_aluno_data = aluno_data, session_db = session)

@app.delete("/aluno/delete/{id}", response_model=schemas.Response_Aluno)
def delete(id : int, session : Session = Depends(get_db)):
    return repository.remove_aluno(aluno_id = id, session_db = session)
        