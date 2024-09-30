class Aluno_Already_Exists(Exception):
    def __init__(self):
        super()
        self.error_code = 409

    def __str__(self):
        return "Aluno já Existe!"
    
class Aluno_Not_Exists(Exception):
    def __init__(self):
        super()
        self.error_code = 404

    def __str__(self):
        return "Aluno Não Existe!"
    
class Incorret_Crendials(Exception):
    def __init__(self):
        super()
        self.error_code = 401

    def __str__(self):
        return "Senha ou Email incorreto!"
    
class Invalid_Token(Exception):
    def __init__(self):
        super()
        self.error_code = 401

    def __str__(self):
        return "Token inválido!"
    
class Email_Already_Registered(Exception):
    def __init__(self):
        super()
        self.error_code = 409

    def __str__(self):
        return "Email já cadastrado!"