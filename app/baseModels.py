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
    estado: Optional[bool]=True


class produccionLecheSacrificioBModel(BaseModel):
    id: Optional[int]= Field(default=None,ge=1,example=99)
    anio: int = Field(ge=0,example=2023)
    sacrificio_bovino_milesxcab: int = Field(ge=0,example=3886)
    produccion_carne_ton: int = Field(ge=0,example=795969)
    tasa_extraccion_porcentage: float = Field(ge=0,example=18.18)
    produccion_leche_cruda_millonesxlts: int = Field(ge=0,example=4917)
    acopio_industrial_millonesxlts: int = Field(ge=0,example=2309)
    estado: Optional[bool]=True


class precioUSDnovilloGordopieBModel(BaseModel):
    id: Optional[int]= Field(default=None,ge=1)
    pais: str = Field(min_length=1, max_length=50)
    fecha: date
    precio: float = Field(ge=0)
    estado: Optional[bool]=True


class precioLecheCrudaUSDxLBModel(BaseModel):
    id: Optional[int]= Field(default=None,ge=1)
    fecha: date
    argentina: float = Field(ge=0)
    brasil: float = Field(ge=0)
    chile: float = Field(ge=0)
    colombia: float = Field(ge=0)
    estados_unidos: float = Field(ge=0)
    union_europea: float = Field(ge=0)
    uruguay: float = Field(ge=0)
    mexico: float = Field(ge=0)
    nueva_zelanda: float = Field(ge=0)
    china: float = Field(ge=0)
    estado: Optional[bool]=True


class costosproduccionBModel(BaseModel):
    id: Optional[int]= Field(default=None,ge=1)
    indice: int = Field(ge=0)
    anio: int = Field(ge=0)
    valor: float = Field(ge=0)
    estado: Optional[bool]=True

class consumosAnualCarneBModel(BaseModel):
    id: Optional[int]= Field(default=None,ge=1)
    anio: int = Field(ge=0)
    consumo_proteina_animal: float = Field(ge=0)
    carne_res_kgxhab: float = Field(ge=0)
    carne_pollo_kgxhab: float = Field(ge=0)
    carne_cerdo_kgxhab: float = Field(ge=0)
    leche_ltxhab: float = Field(ge=0)
    pescado_kgxhab: float = Field(ge=0)
    estado: Optional[bool]=True

class consumosAnualesLecheBModel(BaseModel):
    id: Optional[int]= Field(default=None,ge=1)
    anio: int = Field(ge=0)
    leche_ltxhab: float = Field(ge=0)
    estado: Optional[bool]=True

class litroLechepagadoBModel(BaseModel):
    id: Optional[int]= Field(default=None,ge=1)
    bonificacion: int = Field(ge=0)
    fecha: date
    precio_por_litro_nacional: float = Field(ge=0)
    estado: Optional[bool]=True


class produccionCarneBModel(BaseModel):
    id: Optional[int]= Field(default=None,ge=1)
    anio: int = Field(ge=0)
    toneladas_eq_canal: int = Field(ge=0)
    estado: Optional[bool]=True


class produccionAcopioLecheBModel(BaseModel):
    id: Optional[int]= Field(default=None,ge=1)
    anio: int = Field(ge=0)
    produccion_millonesxlts: float = Field(ge=0)
    acopio_millonesxlts: float = Field(ge=0)
    estado: Optional[bool]=True


class sacrificioMensualBovinoBModel(BaseModel):
    id: Optional[int]= Field(default=None,ge=1)
    fecha: date
    sacrificio: int = Field(ge=0)
    estado: Optional[bool]=True


class hembrasEnSacrificioBModel(BaseModel):
    id: Optional[int]= Field(default=None,ge=1)
    fecha: date
    porcentaje_de_hembras: float = Field(ge=0)
    estado: Optional[bool]=True


class ganadoGordoEnpieBModel(BaseModel):
    id: Optional[int]= Field(default=None,ge=1)
    fecha: date
    precio_x_kilo: int = Field(ge=0)
    estado: Optional[bool]=True


class hembrasFlacaEnpieBModel(BaseModel):
    id: Optional[int]= Field(default=None,ge=1)
    fecha: date
    precio_region_caribe: int = Field(ge=0)
    precio_magdalena_medio_santanderes: int = Field(ge=0)
    precio_llanos_orientales: int = Field(ge=0)
    estado: Optional[bool]=True


class machoCebaGordopieBModel(BaseModel):
    id: Optional[int]= Field(default=None,ge=1)
    fecha: date
    precio_region_caribe: int = Field(ge=0)
    precio_magdalena_medio: int = Field(ge=0)
    precio_llanos_orientales: int = Field(ge=0)
    estado: Optional[bool]=True
