from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import Query
from fastapi import Path
from .database import SessionLocal
from .models import ProduccionLecheSacrificio
from .baseModels import produccionLecheSacrificioBModel
from .warehouse import jsonResponseStructure

app = FastAPI()


@app.get("/")
def home():
    return jsonResponseStructure(status="success",code=200,message="Welcome to FedeganAPI")

@app.get("/api/produccionLecheSacrificio")
def getAllProduccionLecheSacrificio():
    db = SessionLocal()
    queryResult = db.query(ProduccionLecheSacrificio).filter(ProduccionLecheSacrificio.estado==True).all()
    db.close()
    return jsonResponseStructure(status="success",code=200,data=queryResult,count=len(queryResult),message="Request processed successfully")

@app.get("/api/produccionLecheSacrificio/")
def getByParametersProduccionLecheSacrificio(
        minLimit:int= Query(default=1,ge=1,description="Limit Initial"), 
        maxLimit:int= Query(default=2,ge=1, description="Limit Final")
    ):
    if (minLimit>maxLimit or minLimit==maxLimit):
        raise HTTPException(status_code=500, detail="Initial limit can't be less or equal to final limit")
    db = SessionLocal()
    queryResult = db.query(ProduccionLecheSacrificio).filter(ProduccionLecheSacrificio.id.between(minLimit,maxLimit)).filter(ProduccionLecheSacrificio.estado==True).all()
    db.close()
    return jsonResponseStructure(status="success",code=200,data=queryResult,message="Request processed successfully")


@app.get("/api/produccionLecheSacrificio/{idData}")
def getByIdProduccionLecheSacrificio(idData:int = Path(default=1,ge=1,description="This is the ProduccionLecheSacrificio ID",example=1)):
    db = SessionLocal()
    queryResult = db.query(ProduccionLecheSacrificio).filter(ProduccionLecheSacrificio.id==idData).filter(ProduccionLecheSacrificio.estado==True).all()
    db.close()
    if len(queryResult)==0 or queryResult is None:
        queryResult=f"the id {idData} is not valid, try again with other id"
    return jsonResponseStructure(status="success",code=200,data=queryResult,message="Request processed successfully")

@app.post("/api/produccionLecheSacrificio/")
def postProduccionLecheSacrificio(data:produccionLecheSacrificioBModel):
    db = SessionLocal()
    dataTarget = ProduccionLecheSacrificio(id=data.id,
                                            anio=data.anio,
                                            sacrificio_bovino_milesxcab=data.sacrificio_bovino_milesxcab,
                                            produccion_carne_ton=data.produccion_carne_ton,
                                            tasa_extraccion_porcentage=data.tasa_extraccion_porcentage,
                                            produccion_leche_cruda_millonesxlts=data.produccion_leche_cruda_millonesxlts,
                                            acopio_industrial_millonesxlts=data.acopio_industrial_millonesxlts,
                                            estado=data.estado)
    db.add(dataTarget)
    db.commit()
    db.refresh(dataTarget)
    db.close()
    return jsonResponseStructure(status="success",code=200,data=dataTarget,message="Data inserted successfully")


@app.put("/api/produccionLecheSacrificio/{idData}")
def putByIdProduccionLecheSacrificio(idData,data:produccionLecheSacrificioBModel):
    db = SessionLocal()
    queryResult = db.query(ProduccionLecheSacrificio).get(idData)
    if queryResult is None:
        raise HTTPException(status_code=500, detail="Id out range")
    queryResult.id=data.id
    queryResult.anio=data.anio
    queryResult.sacrificio_bovino_milesxcab=data.sacrificio_bovino_milesxcab
    queryResult.produccion_carne_ton=data.produccion_carne_ton
    queryResult.tasa_extraccion_porcentage=data.tasa_extraccion_porcentage
    queryResult.produccion_leche_cruda_millonesxlts=data.produccion_leche_cruda_millonesxlts
    queryResult.acopio_industrial_millonesxlts=data.acopio_industrial_millonesxlts
    queryResult.estado=data.estado
    db.commit()
    db.refresh(queryResult)
    db.close()
    return jsonResponseStructure(status="success",code=200,data=queryResult,message="Data updated successfully")

@app.delete("/api/produccionLecheSacrificio/{idData}")
def deleteByIdProduccionLecheSacrificio(idData:int = Path(default=None,ge=1,description="This is the ProduccionLecheSacrificio ID",example=1)):
    db = SessionLocal()
    queryResult = db.query(ProduccionLecheSacrificio).get(idData)
    if queryResult is None:
        raise HTTPException(status_code=500, detail="Id out range")
    queryResult.estado=False
    db.commit()
    db.refresh(queryResult)
    db.close()
    return jsonResponseStructure(status="success",code=200,data=queryResult,message="Data deleted successfully")

