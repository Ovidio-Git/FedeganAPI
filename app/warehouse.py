from datetime import datetime
from dotenv import load_dotenv
from os import getenv

load_dotenv()

ACCESS_TOKEN_EXPIRE_MINUTES = 30
ALGORITHM = "HS256"
SECRET_KEY = getenv("SERCRET_KEY")

def jsonResponseStructure(status:str,code:int,message:str,count:int=-1,data=None):
    dataJson={
        "status": status,
        "code": code,
        "message": message,
        "timestamp": datetime.now()
    }
    if count != -1:
        dataJson.update({"info":{"count":count}})
    if data != None:
        dataJson.update({"data":data})
    return dataJson
