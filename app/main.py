from fastapi import FastAPI
from .database import SessionLocal
from .models import ProduccionLecheSacrificio

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Welcome to FedeganAPI"}


@app.get("/produccion_leche_sacrificio")
def get_produccion_leche_sacrificio():
    db = SessionLocal()
    queryResult = db.query(ProduccionLecheSacrificio).all()
    db.close()
    return queryResult