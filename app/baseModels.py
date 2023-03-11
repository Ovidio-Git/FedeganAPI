from pydantic import BaseModel
from pydantic import Field
from datetime import date
from typing import Optional


class parametroBModel(BaseModel):
    idparametro: Optional[int]= Field(default=None,ge=1)
    nombreparametro: str = Field(min_length=1, max_length=150)
    valor: int = Field(ge=0)
    idpadre: int = Field(ge=0)
    descripcion: str = Field(min_length=1, max_length=500)
    estado: Optional[bool]=Field(default=True,example=True)


class produccionLecheSacrificioBModel(BaseModel):
    id: Optional[int]= Field(default=None,ge=1,example=99)
    anio: int = Field(ge=0,example=2023)
    sacrificio_bovino_milesxcab: int = Field(ge=0,example=3886)
    produccion_carne_ton: int = Field(ge=0,example=795969)
    tasa_extraccion_porcentage: float = Field(ge=0,example=18.18)
    produccion_leche_cruda_millonesxlts: int = Field(ge=0,example=4917)
    acopio_industrial_millonesxlts: int = Field(ge=0,example=2309)
    estado: Optional[bool]=Field(default=True,example=True)


class precioUSDnovilloGordopieBModel(BaseModel):
    id: Optional[int]= Field(default=None,ge=1,example=98)
    pais: str = Field(min_length=1, max_length=50,example="Chile")
    fecha: date = Field(example="2001-02-01")
    precio: float = Field(ge=0,example=0.591)
    estado: Optional[bool]=Field(default=True,example=True)


class precioLecheCrudaUSDxLBModel(BaseModel):
    id: Optional[int]= Field(default=None,ge=1,example=97)
    fecha: date = Field(example="2021-02-01")
    argentina: float = Field(ge=0,example=0.97)
    brasil: float = Field(ge=0,example=0.87)
    chile: float = Field(ge=0,example=0.94)
    colombia: float = Field(ge=0,example=0.84)
    estados_unidos: float = Field(ge=0,example=0.92)
    union_europea: float = Field(ge=0,example=0.82)
    uruguay: float = Field(ge=0,example=0.90)
    mexico: float = Field(ge=0,example=0.80)
    nueva_zelanda: float = Field(ge=0,example=0.85)
    china: float = Field(ge=0,example=0.95)
    estado: Optional[bool]=Field(default=True,example=True)


class costosproduccionBModel(BaseModel):
    id: Optional[int]= Field(default=None,ge=1,example=96)
    indice: int = Field(ge=0,example=4)
    anio: int = Field(ge=0,example=2015)
    valor: float = Field(ge=0,example=100)
    estado: Optional[bool]=Field(default=True,example=True)

class consumosAnualCarneBModel(BaseModel):
    id: Optional[int]= Field(default=None,ge=1,example=95)
    anio: int = Field(ge=0,example=2005)
    consumo_proteina_animal: float = Field(ge=0,example=45.49)
    carne_res_kgxhab: float = Field(ge=0,example=18.88)
    carne_pollo_kgxhab: float = Field(ge=0,example=20.1)
    carne_cerdo_kgxhab: float = Field(ge=0,example=3.49)
    leche_ltxhab: float = Field(ge=0,example=139.813)
    pescado_kgxhab: float = Field(ge=0,example=2.81)
    estado: Optional[bool]=Field(default=True,example=True)

class consumosAnualesLecheBModel(BaseModel):
    id: Optional[int]= Field(default=None,ge=1,example=94)
    anio: int = Field(ge=0,example=1991)
    leche_ltxhab: float = Field(ge=0,example=119.478)
    estado: Optional[bool]=Field(default=True,example=True)

class litroLechepagadoBModel(BaseModel):
    id: Optional[int]= Field(default=None,ge=1,example=93)
    bonificacion: int = Field(ge=0,example=2)
    fecha: date = Field(example="2022-02-01")
    precio_por_litro_nacional: float = Field(ge=0,example=951)
    estado: Optional[bool]=Field(default=True,example=True)


class produccionCarneBModel(BaseModel):
    id: Optional[int]= Field(default=None,ge=1,example=92)
    anio: int = Field(ge=0,example=2009)
    toneladas_eq_canal: int = Field(ge=0,example=810068)
    estado: Optional[bool]=Field(default=True,example=True)


class produccionAcopioLecheBModel(BaseModel):
    id: Optional[int]= Field(default=None,ge=1,example=91)
    anio: int = Field(ge=0,example=2012)
    produccion_millonesxlts: float = Field(ge=0,example=6.617)
    acopio_millonesxlts: float = Field(ge=0,example=3.129)
    estado: Optional[bool]=Field(default=True,example=True)


class sacrificioMensualBovinoBModel(BaseModel):
    id: Optional[int]= Field(default=None,ge=1,example=90)
    fecha: date = Field(example="2020-02-01")
    sacrificio: int = Field(ge=0,example=291929)
    estado: Optional[bool]=Field(default=True,example=True)


class hembrasEnSacrificioBModel(BaseModel):
    id: Optional[int]= Field(default=None,ge=1,example=89)
    fecha: date = Field(example="2023-02-01")
    porcentaje_de_hembras: float = Field(ge=0,example=37.3)
    estado: Optional[bool]=Field(default=True,example=True)


class ganadoGordoEnpieBModel(BaseModel):
    id: Optional[int]= Field(default=None,ge=1,example=88)
    fecha: date = Field(example="2019-02-01")
    precio_x_kilo: int = Field(ge=0,example=4215)
    estado: Optional[bool]=Field(default=True,example=True)


class hembrasFlacaEnpieBModel(BaseModel):
    id: Optional[int]= Field(default=None,ge=1,example=87)
    fecha: date = Field(example="2018-02-01")
    precio_region_caribe: int = Field(ge=0,example=4009)
    precio_magdalena_medio_santanderes: int = Field(ge=0,example=4325)
    precio_llanos_orientales: int = Field(ge=0,example=4150)
    estado: Optional[bool]=Field(default=True,example=True)


class machoCebaGordopieBModel(BaseModel):
    id: Optional[int]= Field(default=None,ge=1,example=86)
    fecha: date = Field(example="2017-02-01")
    precio_region_caribe: int = Field(ge=0,example=4077)
    precio_magdalena_medio: int = Field(ge=0,example=4017)
    precio_llanos_orientales: int = Field(ge=0,example=3927)
    estado: Optional[bool]=Field(default=True,example=True)
