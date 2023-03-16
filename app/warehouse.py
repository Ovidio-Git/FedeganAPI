from os import getenv
from jose import jwt
from bcrypt import hashpw
from bcrypt import checkpw
from bcrypt import gensalt
from dotenv import load_dotenv
from datetime import datetime
from datetime import timedelta
from json import dumps

load_dotenv()

ACCESS_TOKEN_EXPIRE = datetime.utcnow() + timedelta(minutes=30)
ALGORITHM = "HS256"
SECRET_KEY = getenv("SERCRET_KEY")

def generateJwtToken(username:str) -> str:
    token= jwt.encode({'username': username, 'exp': ACCESS_TOKEN_EXPIRE}, SECRET_KEY, algorithm=ALGORITHM)
    return token

def convertPasswordToHash(password:str) -> str:
    passwordEncode = password.encode('utf-8')
    salt=gensalt()
    hashedPassword = hashpw(passwordEncode,salt)
    return hashedPassword.decode('utf8')

def validatePassword(passwordHash:str,passwordUser:str) -> bool:
    passwordEncode = passwordUser.encode('utf-8')
    passwordEncodeHash = passwordHash.encode('utf-8')
    if checkpw(passwordEncode, passwordEncodeHash):
        return True
    else:
        return False

def jsonResponseStructure(status:str,code:int,message:str,count:int=-1,data=None):
    dataJson={
        "status": status,
        "code": code,
        "message": message,
        "timestamp": datetime.now().isoformat()
    }
    if count != -1:
        dataJson.update({"info":{"count":count}})
    if data != None:
        dataJson.update({"data":data})
    return dataJson





