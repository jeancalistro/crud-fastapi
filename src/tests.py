from fastapi.testclient import TestClient
from main import app
import random

client = TestClient(app)


def test_get_alunos():
    response = client.get("/alunos")
    assert response.status_code == 200

def test_create_aluno():
    body = {
        "name": "nome",
        "email": f"email{random.randint(0, 1000)}@mail.com",
        "password": "secretpassword"
    }
    response = client.post("/aluno/new", json=body)
    assert response.status_code == 201

def test_create_existing_aluno():
    body = {
        "name": "nome",
        "email": "email@mail.com",
        "password": "secretpassword"
    }
    response = client.post("/aluno/new", json=body)
    assert response.status_code == 409
    assert response.json() == {"detail": "Aluno já Existe!"}

def test_incorrect_credentials():
    body = {
        "email": "email@mail.com",
        "password": "incorrectpass"
    }
    response = client.post("/auth", json=body)
    assert response.status_code == 401
    assert response.json() == {"detail": "Senha ou Email incorreto!"}

def test_invalid_token():
    header = {
        "Authorization": "Bearer INVALID_TOKEN"
    }
    response = client.get("/aluno", headers=header)
    assert response.status_code == 401
    assert response.json() == {"detail": "Token inválido!"}