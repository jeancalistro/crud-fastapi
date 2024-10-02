from repository import Aluno_Repository
import schemas, exceptions, utils

class Aluno_Service():

    def __init__(self, aluno_repository : Aluno_Repository):
        self.aluno_repository = aluno_repository


    def aluno_data_for_token(self, aluno):
        return {
            "id": aluno.id,
            "name": aluno.name,
            "email": aluno.email
        }


    def get_aluno(self, aluno_from_token : schemas.From_Token):
        aluno = self.aluno_repository.read_aluno_by_email(aluno_from_token['email'])
        if(not aluno):
            raise exceptions.Aluno_Not_Exists()
        return aluno


    def get_alunos(self):
        return self.aluno_repository.read_alunos()


    def create_aluno(self, aluno : schemas.Create_Aluno):
        if(self.exists(email = aluno.email)):
            raise exceptions.Aluno_Already_Exists()
        aluno.password = utils.hash_password(aluno.password)
        return self.aluno_repository.add_aluno(aluno)


    def update_aluno(self, aluno_from_token : schemas.From_Token, new_data : schemas.Update_Aluno):
        aluno_db = self.get_aluno(aluno_from_token)
        
        if(aluno_db.email != new_data.email):
            if(self.exists(email = new_data.email)):
                raise exceptions.Email_Already_Registered()
        
        new_data.password = utils.hash_password(new_data.password)
        return self.aluno_repository.update_aluno(aluno_db.id, new_data)


    def remove_aluno(self, aluno_from_token : schemas.From_Token):
        aluno_db = self.get_aluno(aluno_from_token)
        return self.aluno_repository.delete_aluno(aluno_db.id)


    def auth_aluno(self, aluno_data : schemas.Auth_Aluno):
        aluno_db = self.aluno_repository.read_aluno_by_email(aluno_data.email)
        if(not aluno_db):
            raise exceptions.Aluno_Not_Exists()
        if(not utils.verify_password(aluno_data.password, aluno_db.password_hash)):
            raise exceptions.Incorret_Crendials()
    
        return utils.create_token(self.aluno_data_for_token(aluno_db))
    

    def exists(self, email : str = None, id : int = None):
        if(email):
            aluno = self.aluno_repository.read_aluno_by_email(email)
        elif(id):
            aluno = self.aluno_repository.read_aluno_by_id(id)
        if not aluno:
            return False
        return True
