import unittest
from fastapi.testclient import TestClient
from .main import app   
from requests import get
from requests import post

HOST="http://127.0.0.1:3000"

class TestAPI(unittest.TestCase):
    
    def setUp(self):
        self.client = TestClient(app)

    def test_home(self):
        response = get(f'{HOST}/')
        self.assertEqual(response.status_code, 200)

    def test_getAllProduccionLecheSacrificio(self):
        response = get(f'{HOST}/api/produccionLecheSacrificio')
        self.assertEqual(response.status_code, 200)

    def test_getByParametersProduccionLecheSacrificio(self):
        response = get(f'{HOST}/api/produccionLecheSacrificio/?minLimit=1&maxLimit=5')
        self.assertEqual(response.status_code, 200)

    def test_getByIdProduccionLecheSacrificio(self):
        response = get(f'{HOST}api/produccionLecheSacrificio/1')
        self.assertEqual(response.status_code, 200)

    def test_getAllPrecioUSDnovilloGordopie(self):
        response = get(f'{HOST}/api/precioUSDnovilloGordopie')
        self.assertEqual(response.status_code, 200)

    def test_getByParametersPrecioUSDnovilloGordopie(self):
        response = get(f'{HOST}/api/precioUSDnovilloGordopie/?minLimit=1&maxLimit=5')
        self.assertEqual(response.status_code, 200)

    def test_getByIdPrecioUSDnovilloGordopie(self):
        response = get(f'{HOST}api/precioUSDnovilloGordopie/1')
        self.assertEqual(response.status_code, 200)

    def test_getAllPrecioLecheCrudaUSDxL(self):
        response = get(f'{HOST}/api/precioLecheCrudaUSDxL')
        self.assertEqual(response.status_code, 200)

    def test_getByParametersPrecioLecheCrudaUSDxL(self):
        response = get(f'{HOST}/api/precioLecheCrudaUSDxL/?minLimit=1&maxLimit=5')
        self.assertEqual(response.status_code, 200)

    def test_getByIdPrecioLecheCrudaUSDxL(self):
        response = get(f'{HOST}api/precioLecheCrudaUSDxL/1')
        self.assertEqual(response.status_code, 200)

    def test_getAllCostosproduccion(self):
        response = get(f'{HOST}/api/costosproduccion')
        self.assertEqual(response.status_code, 200)

    def test_getByParametersCostosproduccion(self):
        response = get(f'{HOST}/api/costosproduccion/?minLimit=1&maxLimit=5')
        self.assertEqual(response.status_code, 200)

    def test_getByIdCostosproduccion(self):
        response = get(f'{HOST}api/costosproduccion/1')
        self.assertEqual(response.status_code, 200)

    def test_getAllConsumosAnualCarne(self):
        response = get(f'{HOST}/api/consumosAnualCarne')
        self.assertEqual(response.status_code, 200)

    def test_getByParametersConsumosAnualCarne(self):
        response = get(f'{HOST}/api/consumosAnualCarne/?minLimit=1&maxLimit=5')
        self.assertEqual(response.status_code, 200)

    def test_getByIdConsumosAnualCarne(self):
        response = get(f'{HOST}api/consumosAnualCarne/1')
        self.assertEqual(response.status_code, 200)

    def test_getAllConsumosAnualesLeche(self):
        response = get(f'{HOST}/api/consumosAnualesLeche')
        self.assertEqual(response.status_code, 200)

    def test_getByParametersConsumosAnualesLeche(self):
        response = get(f'{HOST}/api/consumosAnualesLeche/?minLimit=1&maxLimit=5')
        self.assertEqual(response.status_code, 200)

    def test_getByIdConsumosAnualesLeche(self):
        response = get(f'{HOST}api/consumosAnualesLeche/1')
        self.assertEqual(response.status_code, 200)

    def test_getAllLitroLechepagado(self):
        response = get(f'{HOST}/api/litroLechepagado')
        self.assertEqual(response.status_code, 200)

    def test_getByParametersLitroLechepagado(self):
        response = get(f'{HOST}/api/litroLechepagado/?minLimit=1&maxLimit=5')
        self.assertEqual(response.status_code, 200)

    def test_getByIdLitroLechepagado(self):
        response = get(f'{HOST}api/litroLechepagado/1')
        self.assertEqual(response.status_code, 200)

    def test_getAllProduccionCarne(self):
        response = get(f'{HOST}/api/produccionCarne')
        self.assertEqual(response.status_code, 200)

    def test_getByParametersProduccionCarne(self):
        response = get(f'{HOST}/api/produccionCarne/?minLimit=1&maxLimit=5')
        self.assertEqual(response.status_code, 200)

    def test_getByIdProduccionCarne(self):
        response = get(f'{HOST}api/produccionCarne/1')
        self.assertEqual(response.status_code, 200)

    def test_getAllProduccionAcopioLeche(self):
        response = get(f'{HOST}/api/produccionAcopioLeche')
        self.assertEqual(response.status_code, 200)

    def test_getByParametersProduccionAcopioLeche(self):
        response = get(f'{HOST}/api/produccionAcopioLeche/?minLimit=1&maxLimit=5')
        self.assertEqual(response.status_code, 200)

    def test_getByIdProduccionAcopioLeche(self):
        response = get(f'{HOST}api/produccionAcopioLeche/1')
        self.assertEqual(response.status_code, 200)

    def test_getAllSacrificioMensualBovino(self):
        response = get(f'{HOST}/api/sacrificioMensualBovino')
        self.assertEqual(response.status_code, 200)

    def test_getByParametersSacrificioMensualBovino(self):
        response = get(f'{HOST}/api/sacrificioMensualBovino/?minLimit=1&maxLimit=5')
        self.assertEqual(response.status_code, 200)

    def test_getByIdSacrificioMensualBovino(self):
        response = get(f'{HOST}api/sacrificioMensualBovino/1')
        self.assertEqual(response.status_code, 200)


    def test_getAllSacrificioMensualBovino(self):
        response = get(f'{HOST}/api/sacrificioMensualBovino')
        self.assertEqual(response.status_code, 200)

    def test_getByParametersSacrificioMensualBovino(self):
        response = get(f'{HOST}/api/sacrificioMensualBovino/?minLimit=1&maxLimit=5')
        self.assertEqual(response.status_code, 200)

    def test_getByIdSacrificioMensualBovino(self):
        response = get(f'{HOST}api/sacrificioMensualBovino/1')
        self.assertEqual(response.status_code, 200)

    def test_getAllHembrasEnSacrificio(self):
        response = get(f'{HOST}/api/hembrasEnSacrificio')
        self.assertEqual(response.status_code, 200)

    def test_getByParametersHembrasEnSacrificio(self):
        response = get(f'{HOST}/api/hembrasEnSacrificio/?minLimit=1&maxLimit=5')
        self.assertEqual(response.status_code, 200)

    def test_getByIdHembrasEnSacrificio(self):
        response = get(f'{HOST}api/hembrasEnSacrificio/1')
        self.assertEqual(response.status_code, 200)

    def test_getAllGanadoGordoEnpie(self):
        response = get(f'{HOST}/api/ganadoGordoEnpie')
        self.assertEqual(response.status_code, 200)

    def test_getByParametersGanadoGordoEnpie(self):
        response = get(f'{HOST}/api/ganadoGordoEnpie/?minLimit=1&maxLimit=5')
        self.assertEqual(response.status_code, 200)

    def test_getByIdGanadoGordoEnpie(self):
        response = get(f'{HOST}api/ganadoGordoEnpie/1')
        self.assertEqual(response.status_code, 200)

    def test_getAllHembrasFlacaEnpie(self):
        response = get(f'{HOST}/api/hembrasFlacaEnpie')
        self.assertEqual(response.status_code, 200)

    def test_getByParametersHembrasFlacaEnpie(self):
        response = get(f'{HOST}/api/hembrasFlacaEnpie/?minLimit=1&maxLimit=5')
        self.assertEqual(response.status_code, 200)

    def test_getByIdHembrasFlacaEnpie(self):
        response = get(f'{HOST}api/hembrasFlacaEnpie/1')
        self.assertEqual(response.status_code, 200)

    def test_getAllMachoCebaGordopie(self):
        response = get(f'{HOST}/api/machoCebaGordopie')
        self.assertEqual(response.status_code, 200)

    def test_getByParametersMachoCebaGordopie(self):
        response = get(f'{HOST}/api/machoCebaGordopie/?minLimit=1&maxLimit=5')
        self.assertEqual(response.status_code, 200)

    def test_getByIdMachoCebaGordopie(self):
        response = get(f'{HOST}api/machoCebaGordopie/1')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()