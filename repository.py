from sqlalchemy.orm import Session
import models, schemas

class Aluno_Repository():

    def __init__(self, session : Session):
        self.session = session

    def read_aluno(self, aluno_id : int):
        return self.session.query(models.Aluno).filter(models.Aluno.id == aluno_id).first()

    def read_alunos(self, limit : int):
        return self.session.query(models.Aluno).limit(limit).all()

    def add_aluno(self, aluno : schemas.Create_Aluno):
        db_aluno = models.Aluno(name=aluno.name, email=aluno.email)
        self.session.add(db_aluno)
        self.session.commit()
        return db_aluno

    def update_aluno(self, aluno_id : int, new_aluno_data : schemas.Update_Aluno):
        db_aluno = self.session.query(models.Aluno).filter(models.Aluno.id == aluno_id).first()
        if(db_aluno):
            if(db_aluno.name):
                db_aluno.name = new_aluno_data.name
            if(db_aluno.email):
                db_aluno.email = new_aluno_data.email
            self.session.add(db_aluno)
            self.session.commit()
        return db_aluno

    def delete_aluno(self, aluno_id : int):
        db_aluno = self.session.query(models.Aluno).filter(models.Aluno.id == aluno_id).first()
        if(db_aluno):
            self.session.delete(db_aluno)
            self.session.commit()
        return db_aluno