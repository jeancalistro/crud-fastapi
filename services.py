from repository import Aluno_Repository
import schemas

class Aluno_Service():

    def __init__(self, aluno_repository : Aluno_Repository):
        self.aluno_repository = aluno_repository

    def get_aluno(self, aluno_id : int):
        return self.aluno_repository.read_aluno(aluno_id)

    def get_alunos(self, limit : int):
        return self.aluno_repository.read_alunos(limit)
