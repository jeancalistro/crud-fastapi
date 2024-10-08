
# Documentação da API | FastAPI

## API para controle de alunos

## Requisitos

* Docker

## Tecnologias

* Python
* FastAPI
* PostgresSQL
* SQLAlchemy
* JWT

## Variáveis de Ambiente

* POSTGRES_DB
* POSTGRES_USER
* POSTGRES_PASSWORD
* POSTGRES_DOMAIN_NAME

## Inicializar API

`docker compose up -d`

## Camadas

* Controllers
* Services
* Repositories
* Models
* Schemas
* Utils
* Database
* Tests

## Rotas

### Retorna todos os Alunos

```http
  GET /alunos
```

#### Respostas

| HTTP Status Code   | Content-Type       | Response                           |
| :---------- | :--------- | :---------------------------------- |
| `200` | `application/json` | `[ {"name": "string"} ]` |

### Retorna o aluno associado ao JWT

```http
  GET /aluno
```

#### Autenticação

| Tipo   | Header Authorization      |
| :---------- | :--------- |
| `JWT` | `Bearer` |

#### Respostas

| HTTP Status Code   | Content Type       | Response                           |
| :---------- | :--------- | :---------------------------------- |
| `200` | `application/json` | `{"id": int, "email": "string", "name": "string"}` |
| `401` | `application/json` | `{"detail": "string"}` |
| `404` | `application/json` | `{"detail": "string"}` |


### Cadastra um novo aluno

```http
  POST /aluno/new
```

#### Body

| Content Type   | Request     |
| :---------- | :--------- |
| `application/json` | `{"name":"string", "email":"string", "password":"string"}` |


#### Respostas

| HTTP Status Code   | Content-Type       | Response                           |
| :---------- | :--------- | :---------------------------------- |
| `200` | `application/json` | `{"id": int, "email": "string", "name": "string"}` |
| `409` | `application/json` | `{"detail": "string"}` |


### Autenticação do aluno por meio de JWT

```http
  POST /auth
```

#### Body

| Content Type   | Request     |
| :---------- | :--------- |
| `application/json` | `{"name":"string", "email":"string", "password":"string"}` |


#### Respostas

| HTTP Status Code   | Content-Type       | Response                           |
| :---------- | :--------- | :---------------------------------- |
| `200` | `application/json` | `{"token":"string"}` |
| `404` | `application/json` | `{"detail": "string"}` |
| `401` | `application/json` | `{"detail": "string"}` |

### Atualiza dados de um aluno

```http
  PUT /aluno/update
```

#### Autenticação

| Tipo   | Header Authorization      |
| :---------- | :--------- |
| `JWT` | `Bearer` |

#### Body

| Type   | Request     |
| :---------- | :--------- |
| `application/json` | `{"name":"string", "email":"string", "password":"string"}` |

#### Respostas

| HTTP Status Code   | Content-Type       | Response                           |
| :---------- | :--------- | :---------------------------------- |
| `200` | `application/json` | `{"id": int, "email": "string", "name": "string"}` |
| `409` | `application/json` | `{"detail": "string"}` |
| `404` | `application/json` | `{"detail": "string"}` |

### Remove o cadastro de um aluno

```http
  DELETE /aluno/delete
```

#### Autenticação

| Tipo   | Header Authorization      |
| :---------- | :--------- |
| `JWT` | `Bearer` |

#### Respostas

| HTTP Status Code   | Content-Type       | Response                           |
| :---------- | :--------- | :---------------------------------- |
| `204` | `application/json` | `no content` |
| `404` | `application/json` | `{"detail": "string"}` |
