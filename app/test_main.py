from fastapi.testclient import TestClient
from .main import app


client = TestClient(app)



def test_home():
    response = client.get("/")
    assert response.status_code == 200

###### userToken ####################
def test_postToken():
    JsonExample={
                    "username": "lesterT",
                    "password": "lester24"
                }
    response = client.post("/api/token/",json=JsonExample)
    global TOKEN 
    TOKEN=response.json()["data"]
    assert response.status_code == 200

###### produccionLecheSacrificio####################
def test_getAllProduccionLecheSacrificio():
    response = client.get("/api/produccionLecheSacrificio")
    assert response.status_code == 200

def test_getByParametersProduccionLecheSacrificio():
    response = client.get("/api/produccionLecheSacrificio/?minLimit=1&maxLimit=5")
    assert response.status_code == 200

def test_getByIdProduccionLecheSacrificio():
    response = client.get("api/produccionLecheSacrificio/1")
    assert response.status_code == 200

def test_postProduccionLecheSacrificio():
    JsonExample={
                    "id": 10001,
                    "anio": 2023,
                    "sacrificio_bovino_milesxcab": 3886,
                    "produccion_carne_ton": 79469,
                    "tasa_extraccion_porcentage": 18.18,
                    "produccion_leche_cruda_millonesxlts": 4917,
                    "acopio_industrial_millonesxlts": 2309,
                    "estado": True
                }
    TOKEN
    print(TOKEN)
    response = client.post("api/produccionLecheSacrificio/",json=JsonExample, headers={"Authorization": f"Bearer {TOKEN}"})
    assert response.status_code == 200
    

def test_putByIdProduccionLecheSacrificio():
    JsonExample={
                    "id": 11001,
                    "anio": 2024,
                    "sacrificio_bovino_milesxcab": 3886,
                    "produccion_carne_ton": 79469,
                    "tasa_extraccion_porcentage": 18.18,
                    "produccion_leche_cruda_millonesxlts": 4917,
                    "acopio_industrial_millonesxlts": 2309,
                    "estado": True
                }
    response = client.put("api/produccionLecheSacrificio/10001",json=JsonExample, headers={"Authorization": f"Bearer {TOKEN}"})
    assert response.status_code == 200

def test_deleteByIdProduccionLecheSacrificio():
    response = client.delete("api/produccionLecheSacrificio/11001", headers={"Authorization": f"Bearer {TOKEN}"})
    assert response.status_code == 200



###### precioUSDnovilloGordopie ####################
def test_getAllPrecioUSDnovilloGordopie():
    response = client.get("/api/precioUSDnovilloGordopie")
    assert response.status_code == 200

def test_getByParametersPrecioUSDnovilloGordopie():
    response = client.get("/api/precioUSDnovilloGordopie/?minLimit=1&maxLimit=5")
    assert response.status_code == 200

def test_getByIdPrecioUSDnovilloGordopie():
    response = client.get("api/precioUSDnovilloGordopie/1")
    assert response.status_code == 200

def test_postPrecioUSDnovilloGordopie():
    JsonExample={
                    "id": 10002,
                    "pais": "Chile",
                    "fecha": "2021-02-01",
                    "precio": 0.591,
                    "estado": True
                }
    response = client.post("api/precioUSDnovilloGordopie/",json=JsonExample, headers={"Authorization": f"Bearer {TOKEN}"})
    assert response.status_code == 200
    

def test_putByIdPrecioUSDnovilloGordopie():
    JsonExample={
                    "id": 12002,
                    "pais": "Chile",
                    "fecha": "2021-02-01",
                    "precio": 0.591,
                    "estado": True
                }
    response = client.put("api/precioUSDnovilloGordopie/10002",json=JsonExample, headers={"Authorization": f"Bearer {TOKEN}"})
    assert response.status_code == 200

def test_deleteByIdPrecioUSDnovilloGordopie():
    response = client.delete("api/precioUSDnovilloGordopie/12002", headers={"Authorization": f"Bearer {TOKEN}"})
    assert response.status_code == 200



###### precioLecheCrudaUSDx L####################
def test_getAllPrecioLecheCrudaUSDxL():
    response = client.get("/api/precioLecheCrudaUSDxL")
    assert response.status_code == 200

def test_getByParametersPrecioLecheCrudaUSDxL():
    response = client.get("/api/precioLecheCrudaUSDxL/?minLimit=1&maxLimit=5")
    assert response.status_code == 200

def test_getByIdPrecioLecheCrudaUSDxL():
    response = client.get("api/precioLecheCrudaUSDxL/1")
    assert response.status_code == 200

def test_postPrecioLecheCrudaUSDxL():
    JsonExample={
                    "id": 10003,
                    "fecha": "2021-02-01",
                    "argentina": 0.97,
                    "brasil": 0.87,
                    "chile": 0.94,
                    "colombia": 0.84,
                    "estados_unidos": 0.92,
                    "union_europea": 0.82,
                    "uruguay": 0.9,
                    "mexico": 0.8,
                    "nueva_zelanda": 0.85,
                    "china": 0.95,
                    "estado": True
                }
    response = client.post("api/precioLecheCrudaUSDxL/",json=JsonExample, headers={"Authorization": f"Bearer {TOKEN}"})
    assert response.status_code == 200
    

def test_putByIdPrecioLecheCrudaUSDxL():
    JsonExample={
                    "id": 13003,
                    "fecha": "2021-02-01",
                    "argentina": 0.97,
                    "brasil": 0.87,
                    "chile": 0.94,
                    "colombia": 0.84,
                    "estados_unidos": 0.92,
                    "union_europea": 0.82,
                    "uruguay": 0.9,
                    "mexico": 0.8,
                    "nueva_zelanda": 0.85,
                    "china": 0.95,
                    "estado": True
                }
    response = client.put("api/precioLecheCrudaUSDxL/10003",json=JsonExample, headers={"Authorization": f"Bearer {TOKEN}"})
    assert response.status_code == 200

def test_deleteByIdPrecioLecheCrudaUSDxL():
    response = client.delete("api/precioLecheCrudaUSDxL/13003", headers={"Authorization": f"Bearer {TOKEN}"})
    assert response.status_code == 200



###### costosproduccion ####################
def test_getAllCostosproduccion():
    response = client.get("/api/costosproduccion")
    assert response.status_code == 200

def test_getByParametersCostosproduccion():
    response = client.get("/api/costosproduccion/?minLimit=1&maxLimit=5")
    assert response.status_code == 200

def test_getByIdCostosproduccion():
    response = client.get("api/costosproduccion/1")
    assert response.status_code == 200

def test_postCostosproduccion():
    JsonExample={
                    "id": 10004,
                    "indice": 4,
                    "anio": 2015,
                    "valor": 100,
                    "estado": True
                }
    response = client.post("api/costosproduccion/",json=JsonExample, headers={"Authorization": f"Bearer {TOKEN}"})
    assert response.status_code == 200
    

def test_putByIdCostosproduccion():
    JsonExample={
                    "id": 14004,
                    "indice": 4,
                    "anio": 2015,
                    "valor": 100,
                    "estado": True
                }
    response = client.put("api/costosproduccion/10004",json=JsonExample, headers={"Authorization": f"Bearer {TOKEN}"})
    assert response.status_code == 200

def test_deleteByIdCostosproduccion():
    response = client.delete("api/costosproduccion/14004", headers={"Authorization": f"Bearer {TOKEN}"})
    assert response.status_code == 200



###### consumosAnualCarne ####################
def test_getAllConsumosAnualCarne():
    response = client.get("/api/consumosAnualCarne")
    assert response.status_code == 200

def test_getByParametersConsumosAnualCarne():
    response = client.get("/api/consumosAnualCarne/?minLimit=1&maxLimit=5")
    assert response.status_code == 200

def test_getByIdConsumosAnualCarne():
    response = client.get("api/consumosAnualCarne/1")
    assert response.status_code == 200

def test_postConsumosAnualCarne():
    JsonExample={
                    "id": 10005,
                    "anio": 2005,
                    "consumo_proteina_animal": 45.49,
                    "carne_res_kgxhab": 18.88,
                    "carne_pollo_kgxhab": 20.1,
                    "carne_cerdo_kgxhab": 3.49,
                    "leche_ltxhab": 139.813,
                    "pescado_kgxhab": 2.81,
                    "estado": True
                }
    response = client.post("api/consumosAnualCarne/",json=JsonExample, headers={"Authorization": f"Bearer {TOKEN}"})
    assert response.status_code == 200
    

def test_putByIdConsumosAnualCarne():
    JsonExample={
                    "id": 15005,
                    "anio": 2005,
                    "consumo_proteina_animal": 45.49,
                    "carne_res_kgxhab": 18.88,
                    "carne_pollo_kgxhab": 20.1,
                    "carne_cerdo_kgxhab": 3.49,
                    "leche_ltxhab": 139.813,
                    "pescado_kgxhab": 2.81,
                    "estado": True
                }
    response = client.put("api/consumosAnualCarne/10005",json=JsonExample, headers={"Authorization": f"Bearer {TOKEN}"})
    assert response.status_code == 200

def test_deleteByIdConsumosAnualCarne():
    response = client.delete("api/consumosAnualCarne/15005", headers={"Authorization": f"Bearer {TOKEN}"})
    assert response.status_code == 200



###### consumosAnualesLeche ####################
def test_getAllConsumosAnualesLeche():
    response = client.get("/api/consumosAnualesLeche")
    assert response.status_code == 200

def test_getByParametersConsumosAnualesLeche():
    response = client.get("/api/consumosAnualesLeche/?minLimit=1&maxLimit=5")
    assert response.status_code == 200

def test_getByIdConsumosAnualesLeche():
    response = client.get("api/consumosAnualesLeche/1")
    assert response.status_code == 200

def test_postConsumosAnualesLeche():
    JsonExample={
                    "id": 10006,
                    "anio": 1991,
                    "leche_ltxhab": 119.478,
                    "estado": True
                }
    response = client.post("api/consumosAnualesLeche/",json=JsonExample, headers={"Authorization": f"Bearer {TOKEN}"})
    assert response.status_code == 200
    

def test_putByIdConsumosAnualesLeche():
    JsonExample={
                    "id": 16006,
                    "anio": 1991,
                    "leche_ltxhab": 119.478,
                    "estado": True
                }
    response = client.put("api/consumosAnualesLeche/10006",json=JsonExample, headers={"Authorization": f"Bearer {TOKEN}"})
    assert response.status_code == 200

def test_deleteByIdConsumosAnualesLeche():
    response = client.delete("api/consumosAnualesLeche/16006", headers={"Authorization": f"Bearer {TOKEN}"})
    assert response.status_code == 200



###### litroLechepagado ####################
def test_getAllLitroLechepagado():
    response = client.get("/api/litroLechepagado")
    assert response.status_code == 200

def test_getByParametersLitroLechepagado():
    response = client.get("/api/litroLechepagado/?minLimit=1&maxLimit=5")
    assert response.status_code == 200

def test_getByIdLitroLechepagado():
    response = client.get("api/litroLechepagado/1")
    assert response.status_code == 200

def test_postLitroLechepagado():
    JsonExample={
                    "id": 10007,
                    "bonificacion": 2,
                    "fecha": "2022-02-01",
                    "precio_por_litro_nacional": 951,
                    "estado": True
                }
    response = client.post("api/litroLechepagado/",json=JsonExample, headers={"Authorization": f"Bearer {TOKEN}"})
    assert response.status_code == 200
    

def test_putByIdLitroLechepagado():
    JsonExample={
                    "id": 17007,
                    "bonificacion": 2,
                    "fecha": "2022-02-01",
                    "precio_por_litro_nacional": 951,
                    "estado": True
                }
    response = client.put("api/litroLechepagado/10007",json=JsonExample, headers={"Authorization": f"Bearer {TOKEN}"})
    assert response.status_code == 200

def test_deleteByIdLitroLechepagado():
    response = client.delete("api/litroLechepagado/17007", headers={"Authorization": f"Bearer {TOKEN}"})
    assert response.status_code == 200



###### produccionCarne ####################
def test_getAllProduccionCarne():
    response = client.get("/api/produccionCarne")
    assert response.status_code == 200

def test_getByParametersProduccionCarne():
    response = client.get("/api/produccionCarne/?minLimit=1&maxLimit=5")
    assert response.status_code == 200

def test_getByIdProduccionCarne():
    response = client.get("api/produccionCarne/1")
    assert response.status_code == 200

def test_postProduccionCarne():
    JsonExample={
                    "id": 10008,
                    "anio": 2009,
                    "toneladas_eq_canal": 810068,
                    "estado": True
                }
    response = client.post("api/produccionCarne/",json=JsonExample, headers={"Authorization": f"Bearer {TOKEN}"})
    assert response.status_code == 200
    

def test_putByIdProduccionCarne():
    JsonExample={
                    "id": 18008,
                    "anio": 2009,
                    "toneladas_eq_canal": 810068,
                    "estado": True
                }
    response = client.put("api/produccionCarne/10008",json=JsonExample, headers={"Authorization": f"Bearer {TOKEN}"})
    assert response.status_code == 200

def test_deleteByIdProduccionCarne():
    response = client.delete("api/produccionCarne/18008", headers={"Authorization": f"Bearer {TOKEN}"})
    assert response.status_code == 200



###### produccionAcopioLeche ####################
def test_getAllProduccionAcopioLeche():
    response = client.get("/api/produccionAcopioLeche")
    assert response.status_code == 200

def test_getByParametersProduccionAcopioLeche():
    response = client.get("/api/produccionAcopioLeche/?minLimit=1&maxLimit=5")
    assert response.status_code == 200

def test_getByIdProduccionAcopioLeche():
    response = client.get("api/produccionAcopioLeche/1")
    assert response.status_code == 200

def test_postProduccionAcopioLeche():
    JsonExample={
                    "id": 10009,
                    "anio": 2012,
                    "produccion_millonesxlts": 6.617,
                    "acopio_millonesxlts": 3.129,
                    "estado": True
                }
    response = client.post("api/produccionAcopioLeche/",json=JsonExample, headers={"Authorization": f"Bearer {TOKEN}"})
    assert response.status_code == 200
    

def test_putByIdProduccionAcopioLeche():
    JsonExample={
                    "id": 19009,
                    "anio": 2012,
                    "produccion_millonesxlts": 6.617,
                    "acopio_millonesxlts": 3.129,
                    "estado": True
                }
    response = client.put("api/produccionAcopioLeche/10009",json=JsonExample, headers={"Authorization": f"Bearer {TOKEN}"})
    assert response.status_code == 200

def test_deleteByIdProduccionAcopioLeche():
    response = client.delete("api/produccionAcopioLeche/19009", headers={"Authorization": f"Bearer {TOKEN}"})
    assert response.status_code == 200



###### sacrificioMensualBovino ####################
def test_getAllSacrificioMensualBovino():
    response = client.get("/api/sacrificioMensualBovino")
    assert response.status_code == 200

def test_getByParametersSacrificioMensualBovino():
    response = client.get("/api/sacrificioMensualBovino/?minLimit=1&maxLimit=5")
    assert response.status_code == 200

def test_getByIdSacrificioMensualBovino():
    response = client.get("api/sacrificioMensualBovino/1")
    assert response.status_code == 200

def test_postSacrificioMensualBovino():
    JsonExample={
                    "id": 10010,
                    "fecha": "2020-02-01",
                    "sacrificio": 291929,
                    "estado": True
                }
    response = client.post("api/sacrificioMensualBovino/",json=JsonExample, headers={"Authorization": f"Bearer {TOKEN}"})
    assert response.status_code == 200
    

def test_putByIdSacrificioMensualBovino():
    JsonExample={
                    "id": 11000,
                    "fecha": "2020-02-01",
                    "sacrificio": 291929,
                    "estado": True
                }
    response = client.put("api/sacrificioMensualBovino/10010",json=JsonExample, headers={"Authorization": f"Bearer {TOKEN}"})
    assert response.status_code == 200

def test_deleteByIdSacrificioMensualBovino():
    response = client.delete("api/sacrificioMensualBovino/11000", headers={"Authorization": f"Bearer {TOKEN}"})
    assert response.status_code == 200



###### hembrasEnSacrificio ####################
def test_getAllHembrasEnSacrificio():
    response = client.get("/api/hembrasEnSacrificio")
    assert response.status_code == 200

def test_getByParametersHembrasEnSacrificio():
    response = client.get("/api/hembrasEnSacrificio/?minLimit=1&maxLimit=5")
    assert response.status_code == 200

def test_getByIdHembrasEnSacrificio():
    response = client.get("api/hembrasEnSacrificio/1")
    assert response.status_code == 200

def test_postHembrasEnSacrificio():
    JsonExample={
                    "id": 10011,
                    "fecha": "2023-02-01",
                    "porcentaje_de_hembras": 37.3,
                    "estado": True
                }
    response = client.post("api/hembrasEnSacrificio/",json=JsonExample, headers={"Authorization": f"Bearer {TOKEN}"})
    assert response.status_code == 200
    

def test_putByIdHembrasEnSacrificio():
    JsonExample={
                    "id": 11100,
                    "fecha": "2023-02-01",
                    "porcentaje_de_hembras": 37.3,
                    "estado": True
                }
    response = client.put("api/hembrasEnSacrificio/10011",json=JsonExample, headers={"Authorization": f"Bearer {TOKEN}"})
    assert response.status_code == 200

def test_deleteByIdHembrasEnSacrificio():
    response = client.delete("api/hembrasEnSacrificio/11100", headers={"Authorization": f"Bearer {TOKEN}"})
    assert response.status_code == 200



###### ganadoGordoEnpie ####################
def test_getAllGanadoGordoEnpie():
    response = client.get("/api/ganadoGordoEnpie")
    assert response.status_code == 200

def test_getByParametersGanadoGordoEnpie():
    response = client.get("/api/ganadoGordoEnpie/?minLimit=1&maxLimit=5")
    assert response.status_code == 200

def test_getByIdGanadoGordoEnpie():
    response = client.get("api/ganadoGordoEnpie/1")
    assert response.status_code == 200

def test_postGanadoGordoEnpie():
    JsonExample={
                    "id": 10012,
                    "fecha": "2019-02-01",
                    "precio_x_kilo": 4215,
                    "estado": True
                }
    response = client.post("api/ganadoGordoEnpie/",json=JsonExample, headers={"Authorization": f"Bearer {TOKEN}"})
    assert response.status_code == 200
    

def test_putByIdGanadoGordoEnpie():
    JsonExample={
                    "id": 11200,
                    "fecha": "2019-02-01",
                    "precio_x_kilo": 4215,
                    "estado": True
                }
    response = client.put("api/ganadoGordoEnpie/10012",json=JsonExample, headers={"Authorization": f"Bearer {TOKEN}"})
    assert response.status_code == 200

def test_deleteByIdGanadoGordoEnpie():
    response = client.delete("api/ganadoGordoEnpie/11200", headers={"Authorization": f"Bearer {TOKEN}"})
    assert response.status_code == 200



###### hembrasFlacaEnpie ####################
def test_getAllHembrasFlacaEnpie():
    response = client.get("/api/hembrasFlacaEnpie")
    assert response.status_code == 200

def test_getByParametersHembrasFlacaEnpie():
    response = client.get("/api/hembrasFlacaEnpie/?minLimit=1&maxLimit=5")
    assert response.status_code == 200

def test_getByIdHembrasFlacaEnpie():
    response = client.get("api/hembrasFlacaEnpie/1")
    assert response.status_code == 200

def test_postHembrasFlacaEnpie():
    JsonExample={
                    "id": 10013,
                    "fecha": "2018-02-01",
                    "precio_region_caribe": 4009,
                    "precio_magdalena_medio_santanderes": 4325,
                    "precio_llanos_orientales": 4150,
                    "estado": True
                }
    response = client.post("api/hembrasFlacaEnpie/",json=JsonExample, headers={"Authorization": f"Bearer {TOKEN}"})
    assert response.status_code == 200
    

def test_putByIdHembrasFlacaEnpie():
    JsonExample={
                    "id": 11300,
                    "fecha": "2018-02-01",
                    "precio_region_caribe": 4009,
                    "precio_magdalena_medio_santanderes": 4325,
                    "precio_llanos_orientales": 4150,
                    "estado": True
                }
    response = client.put("api/hembrasFlacaEnpie/10013",json=JsonExample, headers={"Authorization": f"Bearer {TOKEN}"})
    assert response.status_code == 200

def test_deleteByIdHembrasFlacaEnpie():
    response = client.delete("api/hembrasFlacaEnpie/11300", headers={"Authorization": f"Bearer {TOKEN}"})
    assert response.status_code == 200



###### machoCebaGordopie ####################
def test_getAllMachoCebaGordopie():
    response = client.get("/api/machoCebaGordopie")
    assert response.status_code == 200

def test_getByParametersMachoCebaGordopie():
    response = client.get("/api/machoCebaGordopie/?minLimit=1&maxLimit=5")
    assert response.status_code == 200

def test_getByIdMachoCebaGordopie():
    response = client.get("api/machoCebaGordopie/1")
    assert response.status_code == 200

def test_postMachoCebaGordopie():
    print(TOKEN)
    JsonExample={
                    "id": 10014,
                    "fecha": "2017-02-01",
                    "precio_region_caribe": 4077,
                    "precio_magdalena_medio": 4017,
                    "precio_llanos_orientales": 3927,
                    "estado": True
                }
    response = client.post("api/machoCebaGordopie/",json=JsonExample, headers={"Authorization": f"Bearer {TOKEN}"})
    assert response.status_code == 200
    

def test_putByIdMachoCebaGordopie():
    JsonExample={
                    "id": 11400,
                    "fecha": "2017-02-01",
                    "precio_region_caribe": 4077,
                    "precio_magdalena_medio": 4017,
                    "precio_llanos_orientales": 3927,
                    "estado": True
                }
    response = client.put("api/machoCebaGordopie/10014",json=JsonExample, headers={"Authorization": f"Bearer {TOKEN}"})
    assert response.status_code == 200

def test_deleteByIdMachoCebaGordopie():
    response = client.delete("api/machoCebaGordopie/11400", headers={"Authorization": f"Bearer {TOKEN}"})
    assert response.status_code == 200
