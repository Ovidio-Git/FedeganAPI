from sqlalchemy import Column, Integer, String, Float, Date
from .database import Base

class Parametro(Base):
    __tablename__ = "parametros"
    idparametro = Column(Integer, primary_key=True, index=True)
    nombreparametro = Column(String(150))
    valor = Column(Integer)
    idpadre = Column(Integer)
    descripcion = Column(String(500))


class ProduccionLecheSacrificio(Base):
    __tablename__ = "produccioneslechesacrificio006"
    anio = Column(Integer, primary_key=True, index=True)
    sacrificio_bovino_milesxcab = Column(Integer)
    produccion_carne_ton = Column(Integer)
    tasa_extraccion_porcentage = Column(Float)
    produccion_leche_cruda_millonesxlts = Column(Integer)
    acopio_industrial_millonesxlts = Column(Integer)


class PrecioUSDnovilloGordopie(Base):
    __tablename__ = "preciousdnovillogordopie014"
    pais = Column(String(50), primary_key=True, index=True)
    fecha = Column(Date, primary_key=True, index=True)
    precio = Column(Float)


class PrecioLecheCrudaUSDxL(Base):
    __tablename__ = "preciolechecrudausdxl018"
    fecha = Column(Date, primary_key=True, index=True)
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


class Costosproduccion(Base):
    __tablename__ = "costosproduccion020"
    indice = Column(Integer, primary_key=True, index=True)
    anio = Column(Integer)
    valor = Column(Float)


class ConsumosAnualCarne(Base):
    __tablename__ = "consumosanualcarne023"
    anio = Column(Integer, primary_key=True, index=True)
    consumo_proteina_animal = Column(Float)
    carne_res_kgxhab = Column(Float)
    carne_pollo_kgxhab = Column(Float)
    carne_cerdo_kgxhab = Column(Float)
    leche_ltxhab = Column(Float)
    pescado_kgxhab = Column(Float)


class ConsumosAnualesLeche(Base):
    __tablename__ = "consumosanualesleche023"
    anio = Column(Integer, primary_key=True, index=True)
    leche_ltxhab = Column(Float)


class LitroLechepagado(Base):
    __tablename__ = "litrolechepagado046"
    bonificacion = Column(Integer, primary_key=True, index=True)
    fecha = Column(Date, primary_key=True, index=True)
    precio_por_litro_nacional = Column(Float)


class produccionCarne(Base):
    __tablename__ = "producionescarne048"
    anio = Column(Integer, primary_key=True, index=True)
    toneladas_eq_canal = Column(Integer)


class produccionAcopioLeche(Base):
    __tablename__ = "produccionacopioleche050"
    anio = Column(Integer, primary_key=True, index=True)
    produccion_millonesxlts = Column(Float)
    acopio_millonesxlts = Column(Float)


class SacrificioMensualBovino(Base):
    __tablename__ = 'sacrificiomensualbovino051'
    fecha = Column(Date, primary_key=True)
    sacrificio = Column(Integer)


class HembrasEnSacrificio(Base):
    __tablename__ = 'hembrasensacificio052'
    fecha = Column(Date, primary_key=True)
    porcentaje_de_hembras = Column(Float)


class GanadoGordoEnpie(Base):
    __tablename__ = 'ganadogordoenpie053'
    fecha = Column(Date, primary_key=True)
    precio_x_kilo = Column(Integer)


class HembrasFlacaEnpie(Base):
    __tablename__ = 'hembrasflacaenpie065'
    fecha = Column(Date, primary_key=True)
    precio_region_caribe = Column(Integer)
    precio_magdalena_medio_santanderes = Column(Integer)
    precio_llanos_orientales = Column(Integer)


class MachoCebaGordopie(Base):
    __tablename__ = 'machocebagordopie071'
    fecha = Column(Date, primary_key=True)
    precio_region_caribe = Column(Integer)
    precio_magdalena_medio = Column(Integer)
    precio_llanos_orientales = Column(Integer)
