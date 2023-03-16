from sqlalchemy import Column, Integer, String, Float, Date,Boolean
from .database import Base

class Users(Base):
    __tablename__ = "users"
    id = Column(Integer)
    username = Column(String(100), primary_key=True, index=True)
    fullname = Column(String(150))
    email = Column(String(150))
    passwordhash = Column(String(500))
    statususer = Column(Boolean)


class Parametro(Base):
    __tablename__ = "parametros"
    idparametro = Column(Integer, primary_key=True, index=True)
    nombreparametro = Column(String(150))
    valor = Column(Integer)
    idpadre = Column(Integer)
    descripcion = Column(String(500))
    estado = Column(Boolean)


class ProduccionLecheSacrificio(Base):
    __tablename__ = "produccioneslechesacrificio006"
    id = Column(Integer, primary_key=True, index=True)
    anio = Column(Integer)
    sacrificio_bovino_milesxcab = Column(Integer)
    produccion_carne_ton = Column(Integer)
    tasa_extraccion_porcentage = Column(Float)
    produccion_leche_cruda_millonesxlts = Column(Integer)
    acopio_industrial_millonesxlts = Column(Integer)
    estado = Column(Boolean)


class PrecioUSDnovilloGordopie(Base):
    __tablename__ = "preciousdnovillogordopie014"
    id = Column(Integer, primary_key=True, index=True)
    pais = Column(String(50))
    fecha = Column(Date)
    precio = Column(Float)
    estado = Column(Boolean)


class PrecioLecheCrudaUSDxL(Base):
    __tablename__ = "preciolechecrudausdxl018"
    id = Column(Integer, primary_key=True, index=True)
    fecha = Column(Date)
    argentina = Column(Float)
    brasil = Column(Float)
    chile = Column(Float)
    colombia = Column(Float)
    estados_unidos = Column(Float)
    union_europea = Column(Float)
    uruguay = Column(Float)
    mexico = Column(Float)
    nueva_zelanda = Column(Float)
    china = Column(Float)
    estado = Column(Boolean)


class Costosproduccion(Base):
    __tablename__ = "costosproduccion020"
    id = Column(Integer, primary_key=True, index=True)
    indice = Column(Integer)
    anio = Column(Integer)
    valor = Column(Float)
    estado = Column(Boolean)


class ConsumosAnualCarne(Base):
    __tablename__ = "consumosanualcarne023"
    id = Column(Integer, primary_key=True, index=True)
    anio = Column(Integer)
    consumo_proteina_animal = Column(Float)
    carne_res_kgxhab = Column(Float)
    carne_pollo_kgxhab = Column(Float)
    carne_cerdo_kgxhab = Column(Float)
    leche_ltxhab = Column(Float)
    pescado_kgxhab = Column(Float)
    estado = Column(Boolean)


class ConsumosAnualesLeche(Base):
    __tablename__ = "consumosanualesleche023"
    id = Column(Integer, primary_key=True, index=True)
    anio = Column(Integer)
    leche_ltxhab = Column(Float)
    estado = Column(Boolean)


class LitroLechepagado(Base):
    __tablename__ = "litrolechepagado046"
    id = Column(Integer, primary_key=True, index=True)
    bonificacion = Column(Integer)
    fecha = Column(Date)
    precio_por_litro_nacional = Column(Float)
    estado = Column(Boolean)

#
class ProduccionCarne(Base):
    __tablename__ = "producionescarne048"
    id = Column(Integer, primary_key=True, index=True)
    anio = Column(Integer)
    toneladas_eq_canal = Column(Integer)
    estado = Column(Boolean)


class ProduccionAcopioLeche(Base):
    __tablename__ = "produccionacopioleche050"
    id = Column(Integer, primary_key=True, index=True)
    anio = Column(Integer)
    produccion_millonesxlts = Column(Float)
    acopio_millonesxlts = Column(Float)
    estado = Column(Boolean)


class SacrificioMensualBovino(Base):
    __tablename__ = 'sacrificiomensualbovino051'
    id = Column(Integer, primary_key=True, index=True)
    fecha = Column(Date)
    sacrificio = Column(Integer)
    estado = Column(Boolean)


class HembrasEnSacrificio(Base):
    __tablename__ = 'hembrasensacificio052'
    id = Column(Integer, primary_key=True, index=True)
    fecha = Column(Date)
    porcentaje_de_hembras = Column(Float)
    estado = Column(Boolean)


class GanadoGordoEnpie(Base):
    __tablename__ = 'ganadogordoenpie053'
    id = Column(Integer, primary_key=True, index=True)
    fecha = Column(Date)
    precio_x_kilo = Column(Integer)
    estado = Column(Boolean)


class HembrasFlacaEnpie(Base):
    __tablename__ = 'hembrasflacaenpie065'
    id = Column(Integer, primary_key=True, index=True)
    fecha = Column(Date)
    precio_region_caribe = Column(Integer)
    precio_magdalena_medio_santanderes = Column(Integer)
    precio_llanos_orientales = Column(Integer)
    estado = Column(Boolean)


class MachoCebaGordopie(Base):
    __tablename__ = 'machocebagordopie071'
    id = Column(Integer, primary_key=True, index=True)
    fecha = Column(Date)
    precio_region_caribe = Column(Integer)
    precio_magdalena_medio = Column(Integer)
    precio_llanos_orientales = Column(Integer)
    estado = Column(Boolean)
