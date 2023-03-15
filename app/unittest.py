import unittest
from fastapi.testclient import TestClient
from .main import app   
from requests import get
from requests import post
from requests import put
from requests import delete

HOST="http://127.0.0.1:3000"

class TestAPI(unittest.TestCase):
    
    def setUp(self):
        self.client = TestClient(app)

    def test_home(self):
        response = get(f'{HOST}/')
        self.assertEqual(response.status_code, 200)



    ###### produccionLecheSacrificio####################
    def test_getAllProduccionLecheSacrificio(self):
        response = get(f'{HOST}/api/produccionLecheSacrificio')
        self.assertEqual(response.status_code, 200)

    def test_getByParametersProduccionLecheSacrificio(self):
        response = get(f'{HOST}/api/produccionLecheSacrificio/?minLimit=1&maxLimit=5')
        self.assertEqual(response.status_code, 200)

    def test_getByIdProduccionLecheSacrificio(self):
        response = get(f'{HOST}api/produccionLecheSacrificio/1')
        self.assertEqual(response.status_code, 200)

    def test_postProduccionLecheSacrificio(self):
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
        response = post(f'{HOST}api/produccionLecheSacrificio/',json=JsonExample)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().status, "success")

    def test_putByIdProduccionLecheSacrificio(self):
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
        response = put(f'{HOST}api/produccionLecheSacrificio/10001',json=JsonExample)
        self.assertEqual(response.status_code, 200)

    def test_deleteByIdProduccionLecheSacrificio(self):
        response = delete(f'{HOST}api/produccionLecheSacrificio/11001')
        self.assertEqual(response.status_code, 200)



    ###### precioUSDnovilloGordopie ####################
    def test_getAllPrecioUSDnovilloGordopie(self):
        response = get(f'{HOST}/api/precioUSDnovilloGordopie')
        self.assertEqual(response.status_code, 200)

    def test_getByParametersPrecioUSDnovilloGordopie(self):
        response = get(f'{HOST}/api/precioUSDnovilloGordopie/?minLimit=1&maxLimit=5')
        self.assertEqual(response.status_code, 200)

    def test_getByIdPrecioUSDnovilloGordopie(self):
        response = get(f'{HOST}api/precioUSDnovilloGordopie/1')
        self.assertEqual(response.status_code, 200)

    def test_postPrecioUSDnovilloGordopie(self):
        JsonExample={
                        "id": 10002,
                        "pais": "Chile",
                        "fecha": "2021-02-01",
                        "precio": 0.591,
                        "estado": True
                    }
        response = post(f'{HOST}api/precioUSDnovilloGordopie/',json=JsonExample)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().status, "success")

    def test_putByIdPrecioUSDnovilloGordopie(self):
        JsonExample={
                        "id": 12002,
                        "pais": "Chile",
                        "fecha": "2021-02-01",
                        "precio": 0.591,
                        "estado": True
                    }
        response = put(f'{HOST}api/precioUSDnovilloGordopie/10002',json=JsonExample)
        self.assertEqual(response.status_code, 200)

    def test_deleteByIdPrecioUSDnovilloGordopie(self):
        response = delete(f'{HOST}api/precioUSDnovilloGordopie/12002')
        self.assertEqual(response.status_code, 200)



    ###### precioLecheCrudaUSDx L####################
    def test_getAllPrecioLecheCrudaUSDxL(self):
        response = get(f'{HOST}/api/precioLecheCrudaUSDxL')
        self.assertEqual(response.status_code, 200)

    def test_getByParametersPrecioLecheCrudaUSDxL(self):
        response = get(f'{HOST}/api/precioLecheCrudaUSDxL/?minLimit=1&maxLimit=5')
        self.assertEqual(response.status_code, 200)

    def test_getByIdPrecioLecheCrudaUSDxL(self):
        response = get(f'{HOST}api/precioLecheCrudaUSDxL/1')
        self.assertEqual(response.status_code, 200)

    def test_postPrecioLecheCrudaUSDxL(self):
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
        response = post(f'{HOST}api/precioLecheCrudaUSDxL/',json=JsonExample)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().status, "success")

    def test_putByIdPrecioLecheCrudaUSDxL(self):
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
        response = put(f'{HOST}api/precioLecheCrudaUSDxL/10003',json=JsonExample)
        self.assertEqual(response.status_code, 200)

    def test_deleteByIdPrecioLecheCrudaUSDxL(self):
        response = delete(f'{HOST}api/precioLecheCrudaUSDxL/13003')
        self.assertEqual(response.status_code, 200)



    ###### costosproduccion ####################
    def test_getAllCostosproduccion(self):
        response = get(f'{HOST}/api/costosproduccion')
        self.assertEqual(response.status_code, 200)

    def test_getByParametersCostosproduccion(self):
        response = get(f'{HOST}/api/costosproduccion/?minLimit=1&maxLimit=5')
        self.assertEqual(response.status_code, 200)

    def test_getByIdCostosproduccion(self):
        response = get(f'{HOST}api/costosproduccion/1')
        self.assertEqual(response.status_code, 200)

    def test_postCostosproduccion(self):
        JsonExample={
                        "id": 10004,
                        "indice": 4,
                        "anio": 2015,
                        "valor": 100,
                        "estado": True
                    }
        response = post(f'{HOST}api/costosproduccion/',json=JsonExample)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().status, "success")

    def test_putByIdCostosproduccion(self):
        JsonExample={
                        "id": 14004,
                        "indice": 4,
                        "anio": 2015,
                        "valor": 100,
                        "estado": True
                    }
        response = put(f'{HOST}api/costosproduccion/10004',json=JsonExample)
        self.assertEqual(response.status_code, 200)

    def test_deleteByIdCostosproduccion(self):
        response = delete(f'{HOST}api/costosproduccion/14004')
        self.assertEqual(response.status_code, 200)



    ###### consumosAnualCarne ####################
    def test_getAllConsumosAnualCarne(self):
        response = get(f'{HOST}/api/consumosAnualCarne')
        self.assertEqual(response.status_code, 200)

    def test_getByParametersConsumosAnualCarne(self):
        response = get(f'{HOST}/api/consumosAnualCarne/?minLimit=1&maxLimit=5')
        self.assertEqual(response.status_code, 200)

    def test_getByIdConsumosAnualCarne(self):
        response = get(f'{HOST}api/consumosAnualCarne/1')
        self.assertEqual(response.status_code, 200)

    def test_postConsumosAnualCarne(self):
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
        response = post(f'{HOST}api/consumosAnualCarne/',json=JsonExample)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().status, "success")

    def test_putByIdConsumosAnualCarne(self):
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
        response = put(f'{HOST}api/consumosAnualCarne/10005',json=JsonExample)
        self.assertEqual(response.status_code, 200)

    def test_deleteByIdConsumosAnualCarne(self):
        response = delete(f'{HOST}api/consumosAnualCarne/15005')
        self.assertEqual(response.status_code, 200)



    ###### consumosAnualesLeche ####################
    def test_getAllConsumosAnualesLeche(self):
        response = get(f'{HOST}/api/consumosAnualesLeche')
        self.assertEqual(response.status_code, 200)

    def test_getByParametersConsumosAnualesLeche(self):
        response = get(f'{HOST}/api/consumosAnualesLeche/?minLimit=1&maxLimit=5')
        self.assertEqual(response.status_code, 200)

    def test_getByIdConsumosAnualesLeche(self):
        response = get(f'{HOST}api/consumosAnualesLeche/1')
        self.assertEqual(response.status_code, 200)

    def test_postConsumosAnualesLeche(self):
        JsonExample={
                        "id": 10006,
                        "anio": 1991,
                        "leche_ltxhab": 119.478,
                        "estado": True
                    }
        response = post(f'{HOST}api/consumosAnualesLeche/',json=JsonExample)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().status, "success")

    def test_putByIdConsumosAnualesLeche(self):
        JsonExample={
                        "id": 16006,
                        "anio": 1991,
                        "leche_ltxhab": 119.478,
                        "estado": True
                    }
        response = put(f'{HOST}api/consumosAnualesLeche/10006',json=JsonExample)
        self.assertEqual(response.status_code, 200)

    def test_deleteByIdConsumosAnualesLeche(self):
        response = delete(f'{HOST}api/consumosAnualesLeche/16006')
        self.assertEqual(response.status_code, 200)



    ###### litroLechepagado ####################
    def test_getAllLitroLechepagado(self):
        response = get(f'{HOST}/api/litroLechepagado')
        self.assertEqual(response.status_code, 200)

    def test_getByParametersLitroLechepagado(self):
        response = get(f'{HOST}/api/litroLechepagado/?minLimit=1&maxLimit=5')
        self.assertEqual(response.status_code, 200)

    def test_getByIdLitroLechepagado(self):
        response = get(f'{HOST}api/litroLechepagado/1')
        self.assertEqual(response.status_code, 200)

    def test_postLitroLechepagado(self):
        JsonExample={
                        "id": 10007,
                        "bonificacion": 2,
                        "fecha": "2022-02-01",
                        "precio_por_litro_nacional": 951,
                        "estado": True
                    }
        response = post(f'{HOST}api/litroLechepagado/',json=JsonExample)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().status, "success")

    def test_putByIdLitroLechepagado(self):
        JsonExample={
                        "id": 17007,
                        "bonificacion": 2,
                        "fecha": "2022-02-01",
                        "precio_por_litro_nacional": 951,
                        "estado": True
                    }
        response = put(f'{HOST}api/litroLechepagado/10007',json=JsonExample)
        self.assertEqual(response.status_code, 200)

    def test_deleteByIdLitroLechepagado(self):
        response = delete(f'{HOST}api/litroLechepagado/17007')
        self.assertEqual(response.status_code, 200)



    ###### produccionCarne ####################
    def test_getAllProduccionCarne(self):
        response = get(f'{HOST}/api/produccionCarne')
        self.assertEqual(response.status_code, 200)

    def test_getByParametersProduccionCarne(self):
        response = get(f'{HOST}/api/produccionCarne/?minLimit=1&maxLimit=5')
        self.assertEqual(response.status_code, 200)

    def test_getByIdProduccionCarne(self):
        response = get(f'{HOST}api/produccionCarne/1')
        self.assertEqual(response.status_code, 200)

    def test_postProduccionCarne(self):
        JsonExample={
                        "id": 10008,
                        "anio": 2009,
                        "toneladas_eq_canal": 810068,
                        "estado": True
                    }
        response = post(f'{HOST}api/produccionCarne/',json=JsonExample)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().status, "success")

    def test_putByIdProduccionCarne(self):
        JsonExample={
                        "id": 18008,
                        "anio": 2009,
                        "toneladas_eq_canal": 810068,
                        "estado": True
                    }
        response = put(f'{HOST}api/produccionCarne/10008',json=JsonExample)
        self.assertEqual(response.status_code, 200)

    def test_deleteByIdProduccionCarne(self):
        response = delete(f'{HOST}api/produccionCarne/18008')
        self.assertEqual(response.status_code, 200)



    ###### produccionAcopioLeche ####################
    def test_getAllProduccionAcopioLeche(self):
        response = get(f'{HOST}/api/produccionAcopioLeche')
        self.assertEqual(response.status_code, 200)

    def test_getByParametersProduccionAcopioLeche(self):
        response = get(f'{HOST}/api/produccionAcopioLeche/?minLimit=1&maxLimit=5')
        self.assertEqual(response.status_code, 200)

    def test_getByIdProduccionAcopioLeche(self):
        response = get(f'{HOST}api/produccionAcopioLeche/1')
        self.assertEqual(response.status_code, 200)

    def test_postProduccionAcopioLeche(self):
        JsonExample={
                        "id": 10009,
                        "anio": 2012,
                        "produccion_millonesxlts": 6.617,
                        "acopio_millonesxlts": 3.129,
                        "estado": True
                    }
        response = post(f'{HOST}api/produccionAcopioLeche/',json=JsonExample)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().status, "success")

    def test_putByIdProduccionAcopioLeche(self):
        JsonExample={
                        "id": 19009,
                        "anio": 2012,
                        "produccion_millonesxlts": 6.617,
                        "acopio_millonesxlts": 3.129,
                        "estado": True
                    }
        response = put(f'{HOST}api/produccionAcopioLeche/10009',json=JsonExample)
        self.assertEqual(response.status_code, 200)

    def test_deleteByIdProduccionAcopioLeche(self):
        response = delete(f'{HOST}api/produccionAcopioLeche/19009')
        self.assertEqual(response.status_code, 200)



    ###### sacrificioMensualBovino ####################
    def test_getAllSacrificioMensualBovino(self):
        response = get(f'{HOST}/api/sacrificioMensualBovino')
        self.assertEqual(response.status_code, 200)

    def test_getByParametersSacrificioMensualBovino(self):
        response = get(f'{HOST}/api/sacrificioMensualBovino/?minLimit=1&maxLimit=5')
        self.assertEqual(response.status_code, 200)

    def test_getByIdSacrificioMensualBovino(self):
        response = get(f'{HOST}api/sacrificioMensualBovino/1')
        self.assertEqual(response.status_code, 200)

    def test_postSacrificioMensualBovino(self):
        JsonExample={
                        "id": 10010,
                        "fecha": "2020-02-01",
                        "sacrificio": 291929,
                        "estado": True
                    }
        response = post(f'{HOST}api/sacrificioMensualBovino/',json=JsonExample)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().status, "success")

    def test_putByIdSacrificioMensualBovino(self):
        JsonExample={
                        "id": 11000,
                        "fecha": "2020-02-01",
                        "sacrificio": 291929,
                        "estado": True
                    }
        response = put(f'{HOST}api/sacrificioMensualBovino/10010',json=JsonExample)
        self.assertEqual(response.status_code, 200)

    def test_deleteByIdSacrificioMensualBovino(self):
        response = delete(f'{HOST}api/sacrificioMensualBovino/11000')
        self.assertEqual(response.status_code, 200)



    ###### hembrasEnSacrificio ####################
    def test_getAllHembrasEnSacrificio(self):
        response = get(f'{HOST}/api/hembrasEnSacrificio')
        self.assertEqual(response.status_code, 200)

    def test_getByParametersHembrasEnSacrificio(self):
        response = get(f'{HOST}/api/hembrasEnSacrificio/?minLimit=1&maxLimit=5')
        self.assertEqual(response.status_code, 200)

    def test_getByIdHembrasEnSacrificio(self):
        response = get(f'{HOST}api/hembrasEnSacrificio/1')
        self.assertEqual(response.status_code, 200)

    def test_postHembrasEnSacrificio(self):
        JsonExample={
                        "id": 10011,
                        "anio": 2009,
                        "toneladas_eq_canal": 810068,
                        "estado": True
                    }
        response = post(f'{HOST}api/hembrasEnSacrificio/',json=JsonExample)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().status, "success")

    def test_putByIdHembrasEnSacrificio(self):
        JsonExample={
                        "id": 11100,
                        "anio": 2009,
                        "toneladas_eq_canal": 810068,
                        "estado": True
                    }
        response = put(f'{HOST}api/hembrasEnSacrificio/10011',json=JsonExample)
        self.assertEqual(response.status_code, 200)

    def test_deleteByIdHembrasEnSacrificio(self):
        response = delete(f'{HOST}api/hembrasEnSacrificio/11100')
        self.assertEqual(response.status_code, 200)



    ###### ganadoGordoEnpie ####################
    def test_getAllGanadoGordoEnpie(self):
        response = get(f'{HOST}/api/ganadoGordoEnpie')
        self.assertEqual(response.status_code, 200)

    def test_getByParametersGanadoGordoEnpie(self):
        response = get(f'{HOST}/api/ganadoGordoEnpie/?minLimit=1&maxLimit=5')
        self.assertEqual(response.status_code, 200)

    def test_getByIdGanadoGordoEnpie(self):
        response = get(f'{HOST}api/ganadoGordoEnpie/1')
        self.assertEqual(response.status_code, 200)

    def test_postGanadoGordoEnpie(self):
        JsonExample={
                        "id": 10012,
                        "fecha": "2019-02-01",
                        "precio_x_kilo": 4215,
                        "estado": True
                    }
        response = post(f'{HOST}api/ganadoGordoEnpie/',json=JsonExample)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().status, "success")

    def test_putByIdGanadoGordoEnpie(self):
        JsonExample={
                        "id": 11200,
                        "fecha": "2019-02-01",
                        "precio_x_kilo": 4215,
                        "estado": True
                    }
        response = put(f'{HOST}api/ganadoGordoEnpie/10012',json=JsonExample)
        self.assertEqual(response.status_code, 200)

    def test_deleteByIdGanadoGordoEnpie(self):
        response = delete(f'{HOST}api/ganadoGordoEnpie/11200')
        self.assertEqual(response.status_code, 200)



    ###### hembrasFlacaEnpie ####################
    def test_getAllHembrasFlacaEnpie(self):
        response = get(f'{HOST}/api/hembrasFlacaEnpie')
        self.assertEqual(response.status_code, 200)

    def test_getByParametersHembrasFlacaEnpie(self):
        response = get(f'{HOST}/api/hembrasFlacaEnpie/?minLimit=1&maxLimit=5')
        self.assertEqual(response.status_code, 200)

    def test_getByIdHembrasFlacaEnpie(self):
        response = get(f'{HOST}api/hembrasFlacaEnpie/1')
        self.assertEqual(response.status_code, 200)

    def test_postHembrasFlacaEnpie(self):
        JsonExample={
                        "id": 10013,
                        "fecha": "2018-02-01",
                        "precio_region_caribe": 4009,
                        "precio_magdalena_medio_santanderes": 4325,
                        "precio_llanos_orientales": 4150,
                        "estado": True
                    }
        response = post(f'{HOST}api/hembrasFlacaEnpie/',json=JsonExample)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().status, "success")

    def test_putByIdHembrasFlacaEnpie(self):
        JsonExample={
                        "id": 11300,
                        "fecha": "2018-02-01",
                        "precio_region_caribe": 4009,
                        "precio_magdalena_medio_santanderes": 4325,
                        "precio_llanos_orientales": 4150,
                        "estado": True
                    }
        response = put(f'{HOST}api/hembrasFlacaEnpie/10013',json=JsonExample)
        self.assertEqual(response.status_code, 200)

    def test_deleteByIdHembrasFlacaEnpie(self):
        response = delete(f'{HOST}api/hembrasFlacaEnpie/11300')
        self.assertEqual(response.status_code, 200)



    ###### machoCebaGordopie ####################
    def test_getAllMachoCebaGordopie(self):
        response = get(f'{HOST}/api/machoCebaGordopie')
        self.assertEqual(response.status_code, 200)

    def test_getByParametersMachoCebaGordopie(self):
        response = get(f'{HOST}/api/machoCebaGordopie/?minLimit=1&maxLimit=5')
        self.assertEqual(response.status_code, 200)

    def test_getByIdMachoCebaGordopie(self):
        response = get(f'{HOST}api/machoCebaGordopie/1')
        self.assertEqual(response.status_code, 200)

    def test_postMachoCebaGordopie(self):
        JsonExample={
                        "id": 10014,
                        "fecha": "2017-02-01",
                        "precio_region_caribe": 4077,
                        "precio_magdalena_medio": 4017,
                        "precio_llanos_orientales": 3927,
                        "estado": True
                    }
        response = post(f'{HOST}api/hembrasEnSacrificio/',json=JsonExample)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().status, "success")

    def test_putByIdMachoCebaGordopie(self):
        JsonExample={
                        "id": 11400,
                        "fecha": "2017-02-01",
                        "precio_region_caribe": 4077,
                        "precio_magdalena_medio": 4017,
                        "precio_llanos_orientales": 3927,
                        "estado": True
                    }
        response = put(f'{HOST}api/hembrasEnSacrificio/10014',json=JsonExample)
        self.assertEqual(response.status_code, 200)

    def test_deleteByIdMachoCebaGordopie(self):
        response = delete(f'{HOST}api/hembrasEnSacrificio/11400')
        self.assertEqual(response.status_code, 200)



if __name__ == '__main__':
    unittest.main()