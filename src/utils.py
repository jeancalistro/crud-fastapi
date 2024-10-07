from passlib.context import CryptContext
import jwt
from exceptions import Invalid_Token
from datetime import datetime, timedelta, timezone
from fastapi import Request

secret_key = "55029740726cf6845643b86e86519f995658289718794c4465605bed42d5ed38"
algorithm = "HS256"
token_expire_time_minutes = 10

password_crypt = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(password, hashed_password):
    return password_crypt.verify(password, hashed_password)

def hash_password(password):
    return password_crypt.hash(password)

def gen_expire_time():
    return datetime.now(tz=timezone.utc) + timedelta(minutes=token_expire_time_minutes)

def create_token(data : dict):
    expire = gen_expire_time()
    data.update({"exp": expire})
    return jwt.encode(payload = data, key=secret_key, algorithm=algorithm)

def verify_token(token):
    try:
        return jwt.decode(token, key=secret_key, algorithms=[algorithm])
    except Exception as exception:
        raise Invalid_Token()
    
def get_token(request : Request):
    try:
        token : str = request.headers["Authorization"]
        if(token):
            return token.replace("Bearer ", "")
    except:
        pass