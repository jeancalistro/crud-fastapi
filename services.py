from repository import Aluno_Repository
import schemas

class Aluno_Service():

    def __init__(self, aluno_repository : Aluno_Repository):
        self.aluno_repository = aluno_repository

    def get_aluno(self, aluno_id : int):
        return self.aluno_repository.read_aluno_by_id(aluno_id)
        
    def get_alunos(self):
        return self.aluno_repository.read_alunos()

    def create_aluno(self, aluno : schemas.Create_Aluno):
        if(self.exists(email = aluno.email)):
            raise Exception("Aluno já Existe!")
        return self.aluno_repository.add_aluno(aluno)
    
    def update_aluno(self, aluno_id : int, new_data : schemas.Update_Aluno):
        if(not self.exists(id = aluno_id)):
            raise Exception("Aluno não Existe!")
        return self.aluno_repository.update_aluno(aluno_id, new_data)
    
    def remove_aluno(self, aluno_id : int):
        if(not self.exists(id = aluno_id)):
            raise Exception("Aluno não Existe!")
        return self.aluno_repository.delete_aluno(aluno_id)
    
    def exists(self, email : str = None, id : int = None):
        if(email):
            aluno = self.aluno_repository.read_aluno_by_email(email)
        elif(id):
            aluno = self.aluno_repository.read_aluno_by_id(id)
        if not aluno:
            return False
        return True
