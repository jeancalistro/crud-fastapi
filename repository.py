from sqlalchemy.orm import Session
import models, schemas

def get_aluno(aluno_id : int, session_db : Session):
    return session_db.query(models.Aluno).filter(models.Aluno.id == aluno_id).first()

def get_alunos(limit : int, session_db : Session):
    return session_db.query(models.Aluno).limit(limit).all()

def create_aluno(aluno : schemas.Create_Aluno, session_db : Session):
    db_aluno = models.Aluno(username=aluno.username, email=aluno.email)
    session_db.add(db_aluno)
    session_db.commit()
    return db_aluno

def update_aluno(aluno_id : int, new_aluno_data : schemas.Update_Aluno, session_db : Session):
    db_aluno = session_db.query(models.Aluno).filter(models.Aluno.id == aluno_id).first()
    if(db_aluno):
        if(db_aluno.username):
            db_aluno.username = new_aluno_data.username
        if(db_aluno.email):
            db_aluno.email = new_aluno_data.email
        session_db.add(db_aluno)
        session_db.commit()
    return db_aluno

def remove_aluno(aluno_id : int, session_db : Session):
    db_aluno = session_db.query(models.Aluno).filter(models.Aluno.id == aluno_id).first()
    if(db_aluno):
        session_db.delete(db_aluno)
        session_db.commit()
    return db_aluno