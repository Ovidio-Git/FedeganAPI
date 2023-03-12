from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import Query
from fastapi import Path
from .database import SessionLocal
from .warehouse import jsonResponseStructure
from .models import ProduccionLecheSacrificio
from .models import PrecioUSDnovilloGordopie
from .models import PrecioLecheCrudaUSDxL
from .models import Costosproduccion
from .models import ConsumosAnualCarne
from .models import ConsumosAnualesLeche
from .models import LitroLechepagado
from .models import ProduccionCarne
from .models import ProduccionAcopioLeche
from .models import SacrificioMensualBovino
from .models import HembrasEnSacrificio
from .models import GanadoGordoEnpie
from .models import HembrasFlacaEnpie
from .models import MachoCebaGordopie
from .baseModels import produccionLecheSacrificioBModel
from .baseModels import precioUSDnovilloGordopieBModel
from .baseModels import precioLecheCrudaUSDxLBModel
from .baseModels import costosproduccionBModel
from .baseModels import consumosAnualCarneBModel
from .baseModels import consumosAnualesLecheBModel
from .baseModels import litroLechepagadoBModel
from .baseModels import produccionCarneBModel
from .baseModels import produccionAcopioLecheBModel
from .baseModels import sacrificioMensualBovinoBModel
from .baseModels import hembrasEnSacrificioBModel
from .baseModels import ganadoGordoEnpieBModel
from .baseModels import hembrasFlacaEnpieBModel
from .baseModels import machoCebaGordopieBModel

app = FastAPI()


@app.get("/")
def home():
    return jsonResponseStructure(status="success",code=200,message="Welcome to FedeganAPI")



## ## ## ## produccioneslechesacrificio006  ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##   
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
def putByIdProduccionLecheSacrificio(data:produccionLecheSacrificioBModel,idData:int = Path(default=1,ge=1,description="This is the ProduccionLecheSacrificio ID",example=1)):
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




## ## ## ## preciousdnovillogordopie014  ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##   
@app.get("/api/precioUSDnovilloGordopie")
def getAllPrecioUSDnovilloGordopie():
    db = SessionLocal()
    queryResult = db.query(PrecioUSDnovilloGordopie).filter(PrecioUSDnovilloGordopie.estado==True).all()
    db.close()
    return jsonResponseStructure(status="success",code=200,data=queryResult,count=len(queryResult),message="Request processed successfully")

@app.get("/api/precioUSDnovilloGordopie/")
def getByParametersPrecioUSDnovilloGordopie(
        minLimit:int= Query(default=1,ge=1,description="Limit Initial"), 
        maxLimit:int= Query(default=2,ge=1, description="Limit Final")
    ):
    if (minLimit>maxLimit or minLimit==maxLimit):
        raise HTTPException(status_code=500, detail="Initial limit can't be less or equal to final limit")
    db = SessionLocal()
    queryResult = db.query(PrecioUSDnovilloGordopie).filter(PrecioUSDnovilloGordopie.id.between(minLimit,maxLimit)).filter(PrecioUSDnovilloGordopie.estado==True).all()
    db.close()
    return jsonResponseStructure(status="success",code=200,data=queryResult,message="Request processed successfully")


@app.get("/api/precioUSDnovilloGordopie/{idData}")
def getByIdPrecioUSDnovilloGordopie(idData:int = Path(default=1,ge=1,description="This is the PrecioUSDnovilloGordopie ID",example=1)):
    db = SessionLocal()
    queryResult = db.query(PrecioUSDnovilloGordopie).filter(PrecioUSDnovilloGordopie.id==idData).filter(PrecioUSDnovilloGordopie.estado==True).all()
    db.close()
    if len(queryResult)==0 or queryResult is None:
        queryResult=f"the id {idData} is not valid, try again with other id"
    return jsonResponseStructure(status="success",code=200,data=queryResult,message="Request processed successfully")

@app.post("/api/precioUSDnovilloGordopie/")
def postPrecioUSDnovilloGordopie(data:precioUSDnovilloGordopieBModel):
    db = SessionLocal()
    dataTarget = PrecioUSDnovilloGordopie(id=data.id,
                                            pais=data.pais,
                                            fecha=data.fecha,
                                            precio=data.precio,
                                            estado=data.estado)
    db.add(dataTarget)
    db.commit()
    db.refresh(dataTarget)
    db.close()
    return jsonResponseStructure(status="success",code=200,data=dataTarget,message="Data inserted successfully")


@app.put("/api/precioUSDnovilloGordopie/{idData}")
def putByIdPrecioUSDnovilloGordopie(data:precioUSDnovilloGordopieBModel,idData:int = Path(default=1,ge=1,description="This is the PrecioUSDnovilloGordopie ID",example=1)):
    db = SessionLocal()
    queryResult = db.query(PrecioUSDnovilloGordopie).get(idData)
    if queryResult is None:
        raise HTTPException(status_code=500, detail="Id out range")
    queryResult.id=data.id
    queryResult.pais=data.pais
    queryResult.fecha=data.fecha
    queryResult.precio=data.precio
    queryResult.estado=data.estado
    db.commit()
    db.refresh(queryResult)
    db.close()
    return jsonResponseStructure(status="success",code=200,data=queryResult,message="Data updated successfully")

@app.delete("/api/precioUSDnovilloGordopie/{idData}")
def deleteByIdPrecioUSDnovilloGordopie(idData:int = Path(default=None,ge=1,description="This is the PrecioUSDnovilloGordopie ID",example=1)):
    db = SessionLocal()
    queryResult = db.query(PrecioUSDnovilloGordopie).get(idData)
    if queryResult is None:
        raise HTTPException(status_code=500, detail="Id out range")
    queryResult.estado=False
    db.commit()
    db.refresh(queryResult)
    db.close()
    return jsonResponseStructure(status="success",code=200,data=queryResult,message="Data deleted successfully")




## ## ## ## PrecioLecheCrudaUSDxL  ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##   
@app.get("/api/precioLecheCrudaUSDxL")
def getAllPrecioLecheCrudaUSDxL():
    db = SessionLocal()
    queryResult = db.query(PrecioLecheCrudaUSDxL).filter(PrecioLecheCrudaUSDxL.estado==True).all()
    db.close()
    return jsonResponseStructure(status="success",code=200,data=queryResult,count=len(queryResult),message="Request processed successfully")

@app.get("/api/precioLecheCrudaUSDxL/")
def getByParametersPrecioLecheCrudaUSDxL(
        minLimit:int= Query(default=1,ge=1,description="Limit Initial"), 
        maxLimit:int= Query(default=2,ge=1, description="Limit Final")
    ):
    if (minLimit>maxLimit or minLimit==maxLimit):
        raise HTTPException(status_code=500, detail="Initial limit can't be less or equal to final limit")
    db = SessionLocal()
    queryResult = db.query(PrecioLecheCrudaUSDxL).filter(PrecioLecheCrudaUSDxL.id.between(minLimit,maxLimit)).filter(PrecioLecheCrudaUSDxL.estado==True).all()
    db.close()
    return jsonResponseStructure(status="success",code=200,data=queryResult,message="Request processed successfully")


@app.get("/api/precioLecheCrudaUSDxL/{idData}")
def getByIdPrecioLecheCrudaUSDxL(idData:int = Path(default=1,ge=1,description="This is the PrecioLecheCrudaUSDxL ID",example=1)):
    db = SessionLocal()
    queryResult = db.query(PrecioLecheCrudaUSDxL).filter(PrecioLecheCrudaUSDxL.id==idData).filter(PrecioLecheCrudaUSDxL.estado==True).all()
    db.close()
    if len(queryResult)==0 or queryResult is None:
        queryResult=f"the id {idData} is not valid, try again with other id"
    return jsonResponseStructure(status="success",code=200,data=queryResult,message="Request processed successfully")

@app.post("/api/precioLecheCrudaUSDxL/")
def postPrecioLecheCrudaUSDxL(data:precioLecheCrudaUSDxLBModel):
    db = SessionLocal()
    dataTarget = PrecioLecheCrudaUSDxL(id=data.id,
                                        fecha=data.fecha,
                                        argentina=data.argentina,
                                        brasil=data.brasil,
                                        chile=data.chile,
                                        colombia=data.colombia,
                                        estados_unidos=data.estados_unidos,
                                        union_europea=data.union_europea,
                                        uruguay=data.uruguay,
                                        mexico=data.mexico,
                                        nueva_zelanda=data.nueva_zelanda,
                                        china=data.china,
                                        estado=data.estado)
    db.add(dataTarget)
    db.commit()
    db.refresh(dataTarget)
    db.close()
    return jsonResponseStructure(status="success",code=200,data=dataTarget,message="Data inserted successfully")


@app.put("/api/precioLecheCrudaUSDxL/{idData}")
def putByIdPrecioLecheCrudaUSDxL(data:precioLecheCrudaUSDxLBModel,idData:int = Path(default=1,ge=1,description="This is the PrecioLecheCrudaUSDxL ID",example=1)):
    db = SessionLocal()
    queryResult = db.query(PrecioLecheCrudaUSDxL).get(idData)
    if queryResult is None:
        raise HTTPException(status_code=500, detail="Id out range")
    queryResult.id=data.id
    queryResult.fecha=data.fecha
    queryResult.argentina=data.argentina
    queryResult.brasil=data.brasil
    queryResult.chile=data.chile
    queryResult.colombia=data.colombia
    queryResult.estados_unidos=data.estados_unidos
    queryResult.union_europea=data.union_europea
    queryResult.uruguay=data.uruguay
    queryResult.mexico=data.mexico
    queryResult.nueva_zelanda=data.nueva_zelanda
    queryResult.china=data.china
    queryResult.estado=data.estado
    db.commit()
    db.refresh(queryResult)
    db.close()
    return jsonResponseStructure(status="success",code=200,data=queryResult,message="Data updated successfully")

@app.delete("/api/precioLecheCrudaUSDxL/{idData}")
def deleteByIdPrecioLecheCrudaUSDxL(idData:int = Path(default=None,ge=1,description="This is the PrecioLecheCrudaUSDxL ID",example=1)):
    db = SessionLocal()
    queryResult = db.query(PrecioLecheCrudaUSDxL).get(idData)
    if queryResult is None:
        raise HTTPException(status_code=500, detail="Id out range")
    queryResult.estado=False
    db.commit()
    db.refresh(queryResult)
    db.close()
    return jsonResponseStructure(status="success",code=200,data=queryResult,message="Data deleted successfully")




## ## ## ## Costosproduccion  ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##   
@app.get("/api/costosproduccion")
def getAllCostosproduccion():
    db = SessionLocal()
    queryResult = db.query(Costosproduccion).filter(Costosproduccion.estado==True).all()
    db.close()
    return jsonResponseStructure(status="success",code=200,data=queryResult,count=len(queryResult),message="Request processed successfully")

@app.get("/api/costosproduccion/")
def getByParametersCostosproduccion(
        minLimit:int= Query(default=1,ge=1,description="Limit Initial"), 
        maxLimit:int= Query(default=2,ge=1, description="Limit Final")
    ):
    if (minLimit>maxLimit or minLimit==maxLimit):
        raise HTTPException(status_code=500, detail="Initial limit can't be less or equal to final limit")
    db = SessionLocal()
    queryResult = db.query(Costosproduccion).filter(Costosproduccion.id.between(minLimit,maxLimit)).filter(Costosproduccion.estado==True).all()
    db.close()
    return jsonResponseStructure(status="success",code=200,data=queryResult,message="Request processed successfully")


@app.get("/api/costosproduccion/{idData}")
def getByIdCostosproduccion(idData:int = Path(default=1,ge=1,description="This is the Costosproduccion ID",example=1)):
    db = SessionLocal()
    queryResult = db.query(Costosproduccion).filter(Costosproduccion.id==idData).filter(Costosproduccion.estado==True).all()
    db.close()
    if len(queryResult)==0 or queryResult is None:
        queryResult=f"the id {idData} is not valid, try again with other id"
    return jsonResponseStructure(status="success",code=200,data=queryResult,message="Request processed successfully")

@app.post("/api/costosproduccion/")
def postCostosproduccion(data:costosproduccionBModel):
    db = SessionLocal()
    dataTarget = Costosproduccion(id=data.id,
                                    indice=data.indice,
                                    anio=data.anio,
                                    valor=data.valor,
                                    estado=data.estado)
    db.add(dataTarget)
    db.commit()
    db.refresh(dataTarget)
    db.close()
    return jsonResponseStructure(status="success",code=200,data=dataTarget,message="Data inserted successfully")


@app.put("/api/costosproduccion/{idData}")
def putByIdCostosproduccion(data:costosproduccionBModel,idData:int = Path(default=1,ge=1,description="This is the Costosproduccion ID",example=1)):
    db = SessionLocal()
    queryResult = db.query(Costosproduccion).get(idData)
    if queryResult is None:
        raise HTTPException(status_code=500, detail="Id out range")
    queryResult.id=data.id
    queryResult.indice=data.indice
    queryResult.anio=data.anio
    queryResult.valor=data.valor
    queryResult.estado=data.estado
    db.commit()
    db.refresh(queryResult)
    db.close()
    return jsonResponseStructure(status="success",code=200,data=queryResult,message="Data updated successfully")

@app.delete("/api/costosproduccion/{idData}")
def deleteByIdCostosproduccion(idData:int = Path(default=None,ge=1,description="This is the Costosproduccion ID",example=1)):
    db = SessionLocal()
    queryResult = db.query(Costosproduccion).get(idData)
    if queryResult is None:
        raise HTTPException(status_code=500, detail="Id out range")
    queryResult.estado=False
    db.commit()
    db.refresh(queryResult)
    db.close()
    return jsonResponseStructure(status="success",code=200,data=queryResult,message="Data deleted successfully")




## ## ## ## ConsumosAnualCarne  ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##   
@app.get("/api/consumosAnualCarne")
def getAllConsumosAnualCarne():
    db = SessionLocal()
    queryResult = db.query(ConsumosAnualCarne).filter(ConsumosAnualCarne.estado==True).all()
    db.close()
    return jsonResponseStructure(status="success",code=200,data=queryResult,count=len(queryResult),message="Request processed successfully")

@app.get("/api/consumosAnualCarne/")
def getByParametersConsumosAnualCarne(
        minLimit:int= Query(default=1,ge=1,description="Limit Initial"), 
        maxLimit:int= Query(default=2,ge=1, description="Limit Final")
    ):
    if (minLimit>maxLimit or minLimit==maxLimit):
        raise HTTPException(status_code=500, detail="Initial limit can't be less or equal to final limit")
    db = SessionLocal()
    queryResult = db.query(ConsumosAnualCarne).filter(ConsumosAnualCarne.id.between(minLimit,maxLimit)).filter(ConsumosAnualCarne.estado==True).all()
    db.close()
    return jsonResponseStructure(status="success",code=200,data=queryResult,message="Request processed successfully")


@app.get("/api/consumosAnualCarne/{idData}")
def getByIdConsumosAnualCarne(idData:int = Path(default=1,ge=1,description="This is the ConsumosAnualCarne ID",example=1)):
    db = SessionLocal()
    queryResult = db.query(ConsumosAnualCarne).filter(ConsumosAnualCarne.id==idData).filter(ConsumosAnualCarne.estado==True).all()
    db.close()
    if len(queryResult)==0 or queryResult is None:
        queryResult=f"the id {idData} is not valid, try again with other id"
    return jsonResponseStructure(status="success",code=200,data=queryResult,message="Request processed successfully")

@app.post("/api/consumosAnualCarne/")
def postConsumosAnualCarne(data:consumosAnualCarneBModel):
    db = SessionLocal()
    dataTarget = ConsumosAnualCarne(id=data.id,
                                    anio=data.anio,
                                    consumo_proteina_animal=data.consumo_proteina_animal,
                                    carne_res_kgxhab=data.carne_res_kgxhab,
                                    carne_pollo_kgxhab=data.carne_pollo_kgxhab,
                                    carne_cerdo_kgxhab=data.carne_cerdo_kgxhab,
                                    leche_ltxhab=data.leche_ltxhab,
                                    pescado_kgxhab=data.pescado_kgxhab,
                                    estado=data.estado)
    db.add(dataTarget)
    db.commit()
    db.refresh(dataTarget)
    db.close()
    return jsonResponseStructure(status="success",code=200,data=dataTarget,message="Data inserted successfully")


@app.put("/api/consumosAnualCarne/{idData}")
def putByIdConsumosAnualCarne(data:consumosAnualCarneBModel,idData:int = Path(default=1,ge=1,description="This is the ConsumosAnualCarne ID",example=1)):
    db = SessionLocal()
    queryResult = db.query(ConsumosAnualCarne).get(idData)
    if queryResult is None:
        raise HTTPException(status_code=500, detail="Id out range")
    queryResult.id=data.id
    queryResult.anio=data.anio,
    queryResult.consumo_proteina_animal=data.consumo_proteina_animal
    queryResult.carne_res_kgxhab=data.carne_res_kgxhab
    queryResult.carne_pollo_kgxhab=data.carne_pollo_kgxhab
    queryResult.carne_cerdo_kgxhab=data.carne_cerdo_kgxhab
    queryResult.leche_ltxhab=data.leche_ltxhab
    queryResult.pescado_kgxhab=data.pescado_kgxhab
    queryResult.estado=data.estado
    db.commit()
    db.refresh(queryResult)
    db.close()
    return jsonResponseStructure(status="success",code=200,data=queryResult,message="Data updated successfully")

@app.delete("/api/consumosAnualCarne/{idData}")
def deleteByIdConsumosAnualCarne(idData:int = Path(default=None,ge=1,description="This is the ConsumosAnualCarne ID",example=1)):
    db = SessionLocal()
    queryResult = db.query(ConsumosAnualCarne).get(idData)
    if queryResult is None:
        raise HTTPException(status_code=500, detail="Id out range")
    queryResult.estado=False
    db.commit()
    db.refresh(queryResult)
    db.close()
    return jsonResponseStructure(status="success",code=200,data=queryResult,message="Data deleted successfully")




## ## ## ## ConsumosAnualesLeche  ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##   
@app.get("/api/consumosAnualesLeche")
def getAllConsumosAnualesLeche():
    db = SessionLocal()
    queryResult = db.query(ConsumosAnualesLeche).filter(ConsumosAnualesLeche.estado==True).all()
    db.close()
    return jsonResponseStructure(status="success",code=200,data=queryResult,count=len(queryResult),message="Request processed successfully")

@app.get("/api/consumosAnualesLeche/")
def getByParametersConsumosAnualesLeche(
        minLimit:int= Query(default=1,ge=1,description="Limit Initial"), 
        maxLimit:int= Query(default=2,ge=1, description="Limit Final")
    ):
    if (minLimit>maxLimit or minLimit==maxLimit):
        raise HTTPException(status_code=500, detail="Initial limit can't be less or equal to final limit")
    db = SessionLocal()
    queryResult = db.query(ConsumosAnualesLeche).filter(ConsumosAnualesLeche.id.between(minLimit,maxLimit)).filter(ConsumosAnualesLeche.estado==True).all()
    db.close()
    return jsonResponseStructure(status="success",code=200,data=queryResult,message="Request processed successfully")


@app.get("/api/consumosAnualesLeche/{idData}")
def getByIdConsumosAnualesLeche(idData:int = Path(default=1,ge=1,description="This is the ConsumosAnualesLeche ID",example=1)):
    db = SessionLocal()
    queryResult = db.query(ConsumosAnualesLeche).filter(ConsumosAnualesLeche.id==idData).filter(ConsumosAnualesLeche.estado==True).all()
    db.close()
    if len(queryResult)==0 or queryResult is None:
        queryResult=f"the id {idData} is not valid, try again with other id"
    return jsonResponseStructure(status="success",code=200,data=queryResult,message="Request processed successfully")

@app.post("/api/consumosAnualesLeche/")
def postConsumosAnualesLeche(data:consumosAnualesLecheBModel):
    db = SessionLocal()
    dataTarget = ConsumosAnualesLeche(id=data.id,
                                    anio=data.anio,
                                    leche_ltxhab=data.consumo_proteina_animal,
                                    estado=data.estado)
    db.add(dataTarget)
    db.commit()
    db.refresh(dataTarget)
    db.close()
    return jsonResponseStructure(status="success",code=200,data=dataTarget,message="Data inserted successfully")


@app.put("/api/consumosAnualesLeche/{idData}")
def putByIdConsumosAnualesLeche(data:consumosAnualesLecheBModel,idData:int = Path(default=1,ge=1,description="This is the ConsumosAnualesLeche ID",example=1)):
    db = SessionLocal()
    queryResult = db.query(ConsumosAnualesLeche).get(idData)
    if queryResult is None:
        raise HTTPException(status_code=500, detail="Id out range")
    queryResult.id=data.id
    queryResult.anio=data.anio
    queryResult.leche_ltxhab=data.consumo_proteina_animal
    queryResult.estado=data.estado
    db.commit()
    db.refresh(queryResult)
    db.close()
    return jsonResponseStructure(status="success",code=200,data=queryResult,message="Data updated successfully")

@app.delete("/api/consumosAnualesLeche/{idData}")
def deleteByIdConsumosAnualesLeche(idData:int = Path(default=None,ge=1,description="This is the ConsumosAnualesLeche ID",example=1)):
    db = SessionLocal()
    queryResult = db.query(ConsumosAnualesLeche).get(idData)
    if queryResult is None: 
        raise HTTPException(status_code=500, detail="Id out range")
    queryResult.estado=False
    db.commit()
    db.refresh(queryResult)
    db.close()
    return jsonResponseStructure(status="success",code=200,data=queryResult,message="Data deleted successfully")




## ## ## ## LitroLechepagado  ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##   
@app.get("/api/litroLechepagado")
def getAllLitroLechepagado():
    db = SessionLocal()
    queryResult = db.query(LitroLechepagado).filter(LitroLechepagado.estado==True).all()
    db.close()
    return jsonResponseStructure(status="success",code=200,data=queryResult,count=len(queryResult),message="Request processed successfully")

@app.get("/api/litroLechepagado/")
def getByParametersLitroLechepagado(
        minLimit:int= Query(default=1,ge=1,description="Limit Initial"), 
        maxLimit:int= Query(default=2,ge=1, description="Limit Final")
    ):
    if (minLimit>maxLimit or minLimit==maxLimit):
        raise HTTPException(status_code=500, detail="Initial limit can't be less or equal to final limit")
    db = SessionLocal()
    queryResult = db.query(LitroLechepagado).filter(LitroLechepagado.id.between(minLimit,maxLimit)).filter(LitroLechepagado.estado==True).all()
    db.close()
    return jsonResponseStructure(status="success",code=200,data=queryResult,message="Request processed successfully")


@app.get("/api/litroLechepagado/{idData}")
def getByIdLitroLechepagado(idData:int = Path(default=1,ge=1,description="This is the LitroLechepagado ID",example=1)):
    db = SessionLocal()
    queryResult = db.query(LitroLechepagado).filter(LitroLechepagado.id==idData).filter(LitroLechepagado.estado==True).all()
    db.close()
    if len(queryResult)==0 or queryResult is None:
        queryResult=f"the id {idData} is not valid, try again with other id"
    return jsonResponseStructure(status="success",code=200,data=queryResult,message="Request processed successfully")

@app.post("/api/litroLechepagado/")
def postLitroLechepagado(data:litroLechepagadoBModel):
    db = SessionLocal()
    dataTarget = LitroLechepagado(id=data.id,
                                    bonificacion=data.bonificacion,
                                    fecha=data.fecha,
                                    precio_por_litro_nacional=data.precio_por_litro_nacional,
                                    estado=data.estado)
    db.add(dataTarget)
    db.commit()
    db.refresh(dataTarget)
    db.close()
    return jsonResponseStructure(status="success",code=200,data=dataTarget,message="Data inserted successfully")


@app.put("/api/litroLechepagado/{idData}")
def putByIdLitroLechepagado(data:litroLechepagadoBModel,idData:int = Path(default=1,ge=1,description="This is the LitroLechepagado ID",example=1)):
    db = SessionLocal()
    queryResult = db.query(LitroLechepagado).get(idData)
    if queryResult is None:
        raise HTTPException(status_code=500, detail="Id out range")
    queryResult.id=data.id
    queryResult.bonificacion=data.bonificacion
    queryResult.fecha=data.fecha
    queryResult.precio_por_litro_nacional=data.precio_por_litro_nacional
    queryResult.estado=data.estado
    db.commit()
    db.refresh(queryResult)
    db.close()
    return jsonResponseStructure(status="success",code=200,data=queryResult,message="Data updated successfully")

@app.delete("/api/litroLechepagado/{idData}")
def deleteByIdLitroLechepagado(idData:int = Path(default=None,ge=1,description="This is the LitroLechepagado ID",example=1)):
    db = SessionLocal()
    queryResult = db.query(LitroLechepagado).get(idData)
    if queryResult is None: 
        raise HTTPException(status_code=500, detail="Id out range")
    queryResult.estado=False
    db.commit()
    db.refresh(queryResult)
    db.close()
    return jsonResponseStructure(status="success",code=200,data=queryResult,message="Data deleted successfully")




## ## ## ## ProduccionCarne  ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##   
@app.get("/api/produccionCarne")
def getAllProduccionCarne():
    db = SessionLocal()
    queryResult = db.query(ProduccionCarne).filter(ProduccionCarne.estado==True).all()
    db.close()
    return jsonResponseStructure(status="success",code=200,data=queryResult,count=len(queryResult),message="Request processed successfully")

@app.get("/api/produccionCarne/")
def getByParametersProduccionCarne(
        minLimit:int= Query(default=1,ge=1,description="Limit Initial"), 
        maxLimit:int= Query(default=2,ge=1, description="Limit Final")
    ):
    if (minLimit>maxLimit or minLimit==maxLimit):
        raise HTTPException(status_code=500, detail="Initial limit can't be less or equal to final limit")
    db = SessionLocal()
    queryResult = db.query(ProduccionCarne).filter(ProduccionCarne.id.between(minLimit,maxLimit)).filter(ProduccionCarne.estado==True).all()
    db.close()
    return jsonResponseStructure(status="success",code=200,data=queryResult,message="Request processed successfully")


@app.get("/api/produccionCarne/{idData}")
def getByIdProduccionCarne(idData:int = Path(default=1,ge=1,description="This is the ProduccionCarne ID",example=1)):
    db = SessionLocal()
    queryResult = db.query(ProduccionCarne).filter(ProduccionCarne.id==idData).filter(ProduccionCarne.estado==True).all()
    db.close()
    if len(queryResult)==0 or queryResult is None:
        queryResult=f"the id {idData} is not valid, try again with other id"
    return jsonResponseStructure(status="success",code=200,data=queryResult,message="Request processed successfully")

@app.post("/api/produccionCarne/")
def postProduccionCarne(data:produccionCarneBModel):
    db = SessionLocal()
    dataTarget = ProduccionCarne(id=data.id,
                                    anio=data.anio,
                                    toneladas_eq_canal=data.toneladas_eq_canal,
                                    estado=data.estado)
    db.add(dataTarget)
    db.commit()
    db.refresh(dataTarget)
    db.close()
    return jsonResponseStructure(status="success",code=200,data=dataTarget,message="Data inserted successfully")


@app.put("/api/produccionCarne/{idData}")
def putByIdProduccionCarne(data:produccionCarneBModel,idData:int = Path(default=1,ge=1,description="This is the ProduccionCarne ID",example=1)):
    db = SessionLocal()
    queryResult = db.query(ProduccionCarne).get(idData)
    if queryResult is None:
        raise HTTPException(status_code=500, detail="Id out range")
    queryResult.id=data.id
    queryResult.anio=data.anio
    queryResult.toneladas_eq_canal=data.toneladas_eq_canal
    queryResult.estado=data.estado
    db.commit()
    db.refresh(queryResult)
    db.close()
    return jsonResponseStructure(status="success",code=200,data=queryResult,message="Data updated successfully")

@app.delete("/api/produccionCarne/{idData}")
def deleteByIdProduccionCarne(idData:int = Path(default=None,ge=1,description="This is the ProduccionCarne ID",example=1)):
    db = SessionLocal()
    queryResult = db.query(ProduccionCarne).get(idData)
    if queryResult is None: 
        raise HTTPException(status_code=500, detail="Id out range")
    queryResult.estado=False
    db.commit()
    db.refresh(queryResult)
    db.close()
    return jsonResponseStructure(status="success",code=200,data=queryResult,message="Data deleted successfully")




## ## ## ## ProduccionAcopioLeche  ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##   
@app.get("/api/produccionAcopioLeche")
def getAllProduccionAcopioLeche():
    db = SessionLocal()
    queryResult = db.query(ProduccionAcopioLeche).filter(ProduccionAcopioLeche.estado==True).all()
    db.close()
    return jsonResponseStructure(status="success",code=200,data=queryResult,count=len(queryResult),message="Request processed successfully")

@app.get("/api/produccionAcopioLeche/")
def getByParametersProduccionAcopioLeche(
        minLimit:int= Query(default=1,ge=1,description="Limit Initial"), 
        maxLimit:int= Query(default=2,ge=1, description="Limit Final")
    ):
    if (minLimit>maxLimit or minLimit==maxLimit):
        raise HTTPException(status_code=500, detail="Initial limit can't be less or equal to final limit")
    db = SessionLocal()
    queryResult = db.query(ProduccionAcopioLeche).filter(ProduccionAcopioLeche.id.between(minLimit,maxLimit)).filter(ProduccionAcopioLeche.estado==True).all()
    db.close()
    return jsonResponseStructure(status="success",code=200,data=queryResult,message="Request processed successfully")


@app.get("/api/produccionAcopioLeche/{idData}")
def getByIdProduccionAcopioLeche(idData:int = Path(default=1,ge=1,description="This is the ProduccionAcopioLeche ID",example=1)):
    db = SessionLocal()
    queryResult = db.query(ProduccionAcopioLeche).filter(ProduccionAcopioLeche.id==idData).filter(ProduccionAcopioLeche.estado==True).all()
    db.close()
    if len(queryResult)==0 or queryResult is None:
        queryResult=f"the id {idData} is not valid, try again with other id"
    return jsonResponseStructure(status="success",code=200,data=queryResult,message="Request processed successfully")

@app.post("/api/produccionAcopioLeche/")
def postProduccionAcopioLeche(data:produccionAcopioLecheBModel):
    db = SessionLocal()
    dataTarget = ProduccionAcopioLeche(id=data.id,
                                    anio=data.anio,
                                    produccion_millonesxlts=data.produccion_millonesxlts,
                                    acopio_millonesxlts=data.acopio_millonesxlts,
                                    estado=data.estado)
    db.add(dataTarget)
    db.commit()
    db.refresh(dataTarget)
    db.close()
    return jsonResponseStructure(status="success",code=200,data=dataTarget,message="Data inserted successfully")


@app.put("/api/produccionAcopioLeche/{idData}")
def putByIdProduccionAcopioLeche(data:produccionAcopioLecheBModel,idData:int = Path(default=1,ge=1,description="This is the ProduccionAcopioLeche ID",example=1)):
    db = SessionLocal()
    queryResult = db.query(ProduccionAcopioLeche).get(idData)
    if queryResult is None:
        raise HTTPException(status_code=500, detail="Id out range")
    queryResult.id=data.id
    queryResult.anio=data.anio
    queryResult.produccion_millonesxlts=data.produccion_millonesxlts
    queryResult.acopio_millonesxlts=data.acopio_millonesxlts
    queryResult.estado=data.estado
    db.commit()
    db.refresh(queryResult)
    db.close()
    return jsonResponseStructure(status="success",code=200,data=queryResult,message="Data updated successfully")

@app.delete("/api/produccionAcopioLeche/{idData}")
def deleteByIdProduccionAcopioLeche(idData:int = Path(default=None,ge=1,description="This is the ProduccionAcopioLeche ID",example=1)):
    db = SessionLocal()
    queryResult = db.query(ProduccionAcopioLeche).get(idData)
    if queryResult is None: 
        raise HTTPException(status_code=500, detail="Id out range")
    queryResult.estado=False
    db.commit()
    db.refresh(queryResult)
    db.close()
    return jsonResponseStructure(status="success",code=200,data=queryResult,message="Data deleted successfully")




## ## ## ## SacrificioMensualBovino  ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##   
@app.get("/api/sacrificioMensualBovino")
def getAllSacrificioMensualBovino():
    db = SessionLocal()
    queryResult = db.query(SacrificioMensualBovino).filter(SacrificioMensualBovino.estado==True).all()
    db.close()
    return jsonResponseStructure(status="success",code=200,data=queryResult,count=len(queryResult),message="Request processed successfully")

@app.get("/api/sacrificioMensualBovino/")
def getByParametersSacrificioMensualBovino(
        minLimit:int= Query(default=1,ge=1,description="Limit Initial"), 
        maxLimit:int= Query(default=2,ge=1, description="Limit Final")
    ):
    if (minLimit>maxLimit or minLimit==maxLimit):
        raise HTTPException(status_code=500, detail="Initial limit can't be less or equal to final limit")
    db = SessionLocal()
    queryResult = db.query(SacrificioMensualBovino).filter(SacrificioMensualBovino.id.between(minLimit,maxLimit)).filter(SacrificioMensualBovino.estado==True).all()
    db.close()
    return jsonResponseStructure(status="success",code=200,data=queryResult,message="Request processed successfully")


@app.get("/api/sacrificioMensualBovino/{idData}")
def getByIdSacrificioMensualBovino(idData:int = Path(default=1,ge=1,description="This is the SacrificioMensualBovino ID",example=1)):
    db = SessionLocal()
    queryResult = db.query(SacrificioMensualBovino).filter(SacrificioMensualBovino.id==idData).filter(SacrificioMensualBovino.estado==True).all()
    db.close()
    if len(queryResult)==0 or queryResult is None:
        queryResult=f"the id {idData} is not valid, try again with other id"
    return jsonResponseStructure(status="success",code=200,data=queryResult,message="Request processed successfully")

@app.post("/api/sacrificioMensualBovino/")
def postSacrificioMensualBovino(data:sacrificioMensualBovinoBModel):
    db = SessionLocal()
    dataTarget = SacrificioMensualBovino(id=data.id,
                                    fecha=data.fecha,
                                    sacrificio=data.sacrificio,
                                    estado=data.estado)
    db.add(dataTarget)
    db.commit()
    db.refresh(dataTarget)
    db.close()
    return jsonResponseStructure(status="success",code=200,data=dataTarget,message="Data inserted successfully")


@app.put("/api/sacrificioMensualBovino/{idData}")
def putByIdSacrificioMensualBovino(data:sacrificioMensualBovinoBModel,idData:int = Path(default=1,ge=1,description="This is the SacrificioMensualBovino ID",example=1)):
    db = SessionLocal()
    queryResult = db.query(SacrificioMensualBovino).get(idData)
    if queryResult is None:
        raise HTTPException(status_code=500, detail="Id out range")
    queryResult.id=data.id
    queryResult.fecha=data.fecha
    queryResult.sacrificio=data.sacrificio
    queryResult.estado=data.estado
    db.commit()
    db.refresh(queryResult)
    db.close()
    return jsonResponseStructure(status="success",code=200,data=queryResult,message="Data updated successfully")

@app.delete("/api/sacrificioMensualBovino/{idData}")
def deleteByIdSacrificioMensualBovino(idData:int = Path(default=None,ge=1,description="This is the SacrificioMensualBovino ID",example=1)):
    db = SessionLocal()
    queryResult = db.query(SacrificioMensualBovino).get(idData)
    if queryResult is None: 
        raise HTTPException(status_code=500, detail="Id out range")
    queryResult.estado=False
    db.commit()
    db.refresh(queryResult)
    db.close()
    return jsonResponseStructure(status="success",code=200,data=queryResult,message="Data deleted successfully")




## ## ## ## HembrasEnSacrificio  ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##   
@app.get("/api/hembrasEnSacrificio")
def getAllHembrasEnSacrificio():
    db = SessionLocal()
    queryResult = db.query(HembrasEnSacrificio).filter(HembrasEnSacrificio.estado==True).all()
    db.close()
    return jsonResponseStructure(status="success",code=200,data=queryResult,count=len(queryResult),message="Request processed successfully")

@app.get("/api/hembrasEnSacrificio/")
def getByParametersHembrasEnSacrificio(
        minLimit:int= Query(default=1,ge=1,description="Limit Initial"), 
        maxLimit:int= Query(default=2,ge=1, description="Limit Final")
    ):
    if (minLimit>maxLimit or minLimit==maxLimit):
        raise HTTPException(status_code=500, detail="Initial limit can't be less or equal to final limit")
    db = SessionLocal()
    queryResult = db.query(HembrasEnSacrificio).filter(HembrasEnSacrificio.id.between(minLimit,maxLimit)).filter(HembrasEnSacrificio.estado==True).all()
    db.close()
    return jsonResponseStructure(status="success",code=200,data=queryResult,message="Request processed successfully")


@app.get("/api/hembrasEnSacrificio/{idData}")
def getByIdHembrasEnSacrificio(idData:int = Path(default=1,ge=1,description="This is the HembrasEnSacrificio ID",example=1)):
    db = SessionLocal()
    queryResult = db.query(HembrasEnSacrificio).filter(HembrasEnSacrificio.id==idData).filter(HembrasEnSacrificio.estado==True).all()
    db.close()
    if len(queryResult)==0 or queryResult is None:
        queryResult=f"the id {idData} is not valid, try again with other id"
    return jsonResponseStructure(status="success",code=200,data=queryResult,message="Request processed successfully")

@app.post("/api/hembrasEnSacrificio/")
def postHembrasEnSacrificio(data:hembrasEnSacrificioBModel):
    db = SessionLocal()
    dataTarget = HembrasEnSacrificio(id=data.id,
                                    fecha=data.fecha,
                                    porcentaje_de_hembras=data.porcentaje_de_hembras,
                                    estado=data.estado)
    db.add(dataTarget)
    db.commit()
    db.refresh(dataTarget)
    db.close()
    return jsonResponseStructure(status="success",code=200,data=dataTarget,message="Data inserted successfully")


@app.put("/api/hembrasEnSacrificio/{idData}")
def putByIdHembrasEnSacrificio(data:hembrasEnSacrificioBModel,idData:int = Path(default=1,ge=1,description="This is the HembrasEnSacrificio ID",example=1)):
    db = SessionLocal()
    queryResult = db.query(HembrasEnSacrificio).get(idData)
    if queryResult is None:
        raise HTTPException(status_code=500, detail="Id out range")
    queryResult.id=data.id
    queryResult.fecha=data.fecha
    queryResult.porcentaje_de_hembras=data.porcentaje_de_hembras
    queryResult.estado=data.estado
    db.commit()
    db.refresh(queryResult)
    db.close()
    return jsonResponseStructure(status="success",code=200,data=queryResult,message="Data updated successfully")

@app.delete("/api/hembrasEnSacrificio/{idData}")
def deleteByIdHembrasEnSacrificio(idData:int = Path(default=None,ge=1,description="This is the HembrasEnSacrificio ID",example=1)):
    db = SessionLocal()
    queryResult = db.query(HembrasEnSacrificio).get(idData)
    if queryResult is None: 
        raise HTTPException(status_code=500, detail="Id out range")
    queryResult.estado=False
    db.commit()
    db.refresh(queryResult)
    db.close()
    return jsonResponseStructure(status="success",code=200,data=queryResult,message="Data deleted successfully")




## ## ## ## GanadoGordoEnpie  ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##   
@app.get("/api/ganadoGordoEnpie")
def getAllGanadoGordoEnpie():
    db = SessionLocal()
    queryResult = db.query(GanadoGordoEnpie).filter(GanadoGordoEnpie.estado==True).all()
    db.close()
    return jsonResponseStructure(status="success",code=200,data=queryResult,count=len(queryResult),message="Request processed successfully")

@app.get("/api/ganadoGordoEnpie/")
def getByParametersGanadoGordoEnpie(
        minLimit:int= Query(default=1,ge=1,description="Limit Initial"), 
        maxLimit:int= Query(default=2,ge=1, description="Limit Final")
    ):
    if (minLimit>maxLimit or minLimit==maxLimit):
        raise HTTPException(status_code=500, detail="Initial limit can't be less or equal to final limit")
    db = SessionLocal()
    queryResult = db.query(GanadoGordoEnpie).filter(GanadoGordoEnpie.id.between(minLimit,maxLimit)).filter(GanadoGordoEnpie.estado==True).all()
    db.close()
    return jsonResponseStructure(status="success",code=200,data=queryResult,message="Request processed successfully")


@app.get("/api/ganadoGordoEnpie/{idData}")
def getByIdGanadoGordoEnpie(idData:int = Path(default=1,ge=1,description="This is the GanadoGordoEnpie ID",example=1)):
    db = SessionLocal()
    queryResult = db.query(GanadoGordoEnpie).filter(GanadoGordoEnpie.id==idData).filter(GanadoGordoEnpie.estado==True).all()
    db.close()
    if len(queryResult)==0 or queryResult is None:
        queryResult=f"the id {idData} is not valid, try again with other id"
    return jsonResponseStructure(status="success",code=200,data=queryResult,message="Request processed successfully")

@app.post("/api/ganadoGordoEnpie/")
def postGanadoGordoEnpie(data:ganadoGordoEnpieBModel):
    db = SessionLocal()
    dataTarget = GanadoGordoEnpie(id=data.id,
                                    fecha=data.fecha,
                                    precio_x_kilo=data.precio_x_kilo,
                                    estado=data.estado)
    db.add(dataTarget)
    db.commit()
    db.refresh(dataTarget)
    db.close()
    return jsonResponseStructure(status="success",code=200,data=dataTarget,message="Data inserted successfully")


@app.put("/api/ganadoGordoEnpie/{idData}")
def putByIdGanadoGordoEnpie(data:ganadoGordoEnpieBModel,idData:int = Path(default=1,ge=1,description="This is the GanadoGordoEnpie ID",example=1)):
    db = SessionLocal()
    queryResult = db.query(GanadoGordoEnpie).get(idData)
    if queryResult is None:
        raise HTTPException(status_code=500, detail="Id out range")
    queryResult.id=data.id
    queryResult.fecha=data.fecha
    queryResult.precio_x_kilo=data.precio_x_kilo
    queryResult.estado=data.estado
    db.commit()
    db.refresh(queryResult)
    db.close()
    return jsonResponseStructure(status="success",code=200,data=queryResult,message="Data updated successfully")

@app.delete("/api/ganadoGordoEnpie/{idData}")
def deleteByIdGanadoGordoEnpie(idData:int = Path(default=None,ge=1,description="This is the GanadoGordoEnpie ID",example=1)):
    db = SessionLocal()
    queryResult = db.query(GanadoGordoEnpie).get(idData)
    if queryResult is None: 
        raise HTTPException(status_code=500, detail="Id out range")
    queryResult.estado=False
    db.commit()
    db.refresh(queryResult)
    db.close()
    return jsonResponseStructure(status="success",code=200,data=queryResult,message="Data deleted successfully")




## ## ## ## HembrasFlacaEnpie  ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##   
@app.get("/api/hembrasFlacaEnpie")
def getAllHembrasFlacaEnpie():
    db = SessionLocal()
    queryResult = db.query(HembrasFlacaEnpie).filter(HembrasFlacaEnpie.estado==True).all()
    db.close()
    return jsonResponseStructure(status="success",code=200,data=queryResult,count=len(queryResult),message="Request processed successfully")

@app.get("/api/hembrasFlacaEnpie/")
def getByParametersHembrasFlacaEnpie(
        minLimit:int= Query(default=1,ge=1,description="Limit Initial"), 
        maxLimit:int= Query(default=2,ge=1, description="Limit Final")
    ):
    if (minLimit>maxLimit or minLimit==maxLimit):
        raise HTTPException(status_code=500, detail="Initial limit can't be less or equal to final limit")
    db = SessionLocal()
    queryResult = db.query(HembrasFlacaEnpie).filter(HembrasFlacaEnpie.id.between(minLimit,maxLimit)).filter(HembrasFlacaEnpie.estado==True).all()
    db.close()
    return jsonResponseStructure(status="success",code=200,data=queryResult,message="Request processed successfully")


@app.get("/api/hembrasFlacaEnpie/{idData}")
def getByIdHembrasFlacaEnpie(idData:int = Path(default=1,ge=1,description="This is the HembrasFlacaEnpie ID",example=1)):
    db = SessionLocal()
    queryResult = db.query(HembrasFlacaEnpie).filter(HembrasFlacaEnpie.id==idData).filter(HembrasFlacaEnpie.estado==True).all()
    db.close()
    if len(queryResult)==0 or queryResult is None:
        queryResult=f"the id {idData} is not valid, try again with other id"
    return jsonResponseStructure(status="success",code=200,data=queryResult,message="Request processed successfully")

@app.post("/api/hembrasFlacaEnpie/")
def postHembrasFlacaEnpie(data:hembrasFlacaEnpieBModel):
    db = SessionLocal()
    dataTarget = HembrasFlacaEnpie(id=data.id,
                                    fecha=data.fecha,
                                    precio_region_caribe=data.precio_region_caribe,
                                    precio_magdalena_medio=data.precio_magdalena_medio,
                                    precio_llanos_orientales=data.precio_llanos_orientales,
                                    estado=data.estado)
    db.add(dataTarget)
    db.commit()
    db.refresh(dataTarget)
    db.close()
    return jsonResponseStructure(status="success",code=200,data=dataTarget,message="Data inserted successfully")


@app.put("/api/hembrasFlacaEnpie/{idData}")
def putByIdHembrasFlacaEnpie(data:hembrasFlacaEnpieBModel,idData:int = Path(default=1,ge=1,description="This is the HembrasFlacaEnpie ID",example=1)):
    db = SessionLocal()
    queryResult = db.query(HembrasFlacaEnpie).get(idData)
    if queryResult is None:
        raise HTTPException(status_code=500, detail="Id out range")
    queryResult.id=data.id
    queryResult.fecha=data.fecha
    queryResult.precio_region_caribe=data.precio_region_caribe
    queryResult.precio_magdalena_medio_santanderes=data.precio_magdalena_medio_santanderes
    queryResult.precio_llanos_orientales=data.precio_llanos_orientales
    queryResult.estado=data.estado
    db.commit()
    db.refresh(queryResult)
    db.close()
    return jsonResponseStructure(status="success",code=200,data=queryResult,message="Data updated successfully")

@app.delete("/api/hembrasFlacaEnpie/{idData}")
def deleteByIdHembrasFlacaEnpie(idData:int = Path(default=None,ge=1,description="This is the HembrasFlacaEnpie ID",example=1)):
    db = SessionLocal()
    queryResult = db.query(HembrasFlacaEnpie).get(idData)
    if queryResult is None: 
        raise HTTPException(status_code=500, detail="Id out range")
    queryResult.estado=False
    db.commit()
    db.refresh(queryResult)
    db.close()
    return jsonResponseStructure(status="success",code=200,data=queryResult,message="Data deleted successfully")




## ## ## ## MachoCebaGordopie  ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##   
@app.get("/api/machoCebaGordopie")
def getAllMachoCebaGordopie():
    db = SessionLocal()
    queryResult = db.query(MachoCebaGordopie).filter(MachoCebaGordopie.estado==True).all()
    db.close()
    return jsonResponseStructure(status="success",code=200,data=queryResult,count=len(queryResult),message="Request processed successfully")

@app.get("/api/machoCebaGordopie/")
def getByParametersMachoCebaGordopie(
        minLimit:int= Query(default=1,ge=1,description="Limit Initial"), 
        maxLimit:int= Query(default=2,ge=1, description="Limit Final")
    ):
    if (minLimit>maxLimit or minLimit==maxLimit):
        raise HTTPException(status_code=500, detail="Initial limit can't be less or equal to final limit")
    db = SessionLocal()
    queryResult = db.query(MachoCebaGordopie).filter(MachoCebaGordopie.id.between(minLimit,maxLimit)).filter(MachoCebaGordopie.estado==True).all()
    db.close()
    return jsonResponseStructure(status="success",code=200,data=queryResult,message="Request processed successfully")


@app.get("/api/machoCebaGordopie/{idData}")
def getByIdMachoCebaGordopie(idData:int = Path(default=1,ge=1,description="This is the MachoCebaGordopie ID",example=1)):
    db = SessionLocal()
    queryResult = db.query(MachoCebaGordopie).filter(MachoCebaGordopie.id==idData).filter(MachoCebaGordopie.estado==True).all()
    db.close()
    if len(queryResult)==0 or queryResult is None:
        queryResult=f"the id {idData} is not valid, try again with other id"
    return jsonResponseStructure(status="success",code=200,data=queryResult,message="Request processed successfully")

@app.post("/api/machoCebaGordopie/")
def postMachoCebaGordopie(data:machoCebaGordopieBModel):
    db = SessionLocal()
    dataTarget = MachoCebaGordopie(id=data.id,
                                    fecha=data.fecha,
                                    precio_region_caribe=data.precio_region_caribe,
                                    precio_magdalena_medio=data.precio_magdalena_medio,
                                    precio_llanos_orientales=data.precio_llanos_orientales,
                                    estado=data.estado)
    db.add(dataTarget)
    db.commit()
    db.refresh(dataTarget)
    db.close()
    return jsonResponseStructure(status="success",code=200,data=dataTarget,message="Data inserted successfully")


@app.put("/api/machoCebaGordopie/{idData}")
def putByIdMachoCebaGordopie(data:machoCebaGordopieBModel,idData:int = Path(default=1,ge=1,description="This is the MachoCebaGordopie ID",example=1)):
    db = SessionLocal()
    queryResult = db.query(MachoCebaGordopie).get(idData)
    if queryResult is None:
        raise HTTPException(status_code=500, detail="Id out range")
    queryResult.id=data.id
    queryResult.fecha=data.fecha
    queryResult.precio_region_caribe=data.precio_region_caribe
    queryResult.precio_magdalena_medio=data.precio_magdalena_medio
    queryResult.precio_llanos_orientales=data.precio_llanos_orientales
    queryResult.estado=data.estado
    db.commit()
    db.refresh(queryResult)
    db.close()
    return jsonResponseStructure(status="success",code=200,data=queryResult,message="Data updated successfully")

@app.delete("/api/machoCebaGordopie/{idData}")
def deleteByIdMachoCebaGordopie(idData:int = Path(default=None,ge=1,description="This is the MachoCebaGordopie ID",example=1)):
    db = SessionLocal()
    queryResult = db.query(MachoCebaGordopie).get(idData)
    if queryResult is None: 
        raise HTTPException(status_code=500, detail="Id out range")
    queryResult.estado=False
    db.commit()
    db.refresh(queryResult)
    db.close()
    return jsonResponseStructure(status="success",code=200,data=queryResult,message="Data deleted successfully")


