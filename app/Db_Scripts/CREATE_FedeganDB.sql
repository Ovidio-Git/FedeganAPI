CREATE TABLE Parametros (
  idParametro INTEGER PRIMARY KEY,
  NombreParametro VARCHAR(150),
  Valor INTEGER,
  idPadre INTEGER,
  Descripcion VARCHAR(500)
);

CREATE TABLE produccionesLecheSacrificio006 (
  Anio INTEGER,
  Sacrificio_Bovino_milesxcab INTEGER,
  Produccion_carne_Ton INTEGER,
  Tasa_extraccion_porcentage	DOUBLE PRECISION,
  Produccion_leche_cruda_millonesxlts INTEGER,
  Acopio_Industrial_millonesxlts INTEGER
);

CREATE TABLE precioUSDNovilloGordoPie014 (
  Pais VARCHAR(50),
  Fecha DATE,
  Precio DOUBLE PRECISION
);

CREATE TABLE PrecioLecheCrudaUSDxL018 (
  Fecha DATE,
  Argentina DOUBLE PRECISION,
  Brasil DOUBLE PRECISION,
  Chile DOUBLE PRECISION,
  Colombia DOUBLE PRECISION,
  Estados_Unidos DOUBLE PRECISION,
  Union_Europea DOUBLE PRECISION,
  Uruguay DOUBLE PRECISION,
  Mexico DOUBLE PRECISION,
  Nueva_Zelanda DOUBLE PRECISION,
  China DOUBLE PRECISION
);

CREATE TABLE costosProduccion020 (
  Indice	INTEGER,
  Anio	INTEGER,
  Valor	FLOAT
);

CREATE TABLE consumosAnualCarne023 (
  Anio INTEGER,
  Consumo_proteina_animal	FLOAT,
  Carne_res_kgxhab FLOAT,
  Carne_pollo_kgxhab FLOAT,
  Carne_cerdo_kgxhab FLOAT,
  Leche_Ltxhab FLOAT,
  Pescado_kgxhab FLOAT
);

CREATE TABLE consumosAnualesLeche023 (
  Anio INTEGER,
  Leche_Ltxhab DOUBLE PRECISION
);

CREATE TABLE litroLechePagado046 (
  Bonificacion INTEGER,
  Fecha DATE,
  Precio_por_litro_Nacional DOUBLE PRECISION
);

CREATE TABLE producionesCarne048 (
  Anio INTEGER,
  Toneladas_eq_canal INTEGER
);

CREATE TABLE ProduccionAcopioLeche050 (
  Anio INTEGER,
  Produccion_millonesxlts DOUBLE PRECISION,
  Acopio_millonesxlts DOUBLE PRECISION
);

CREATE TABLE sacrificioMensualBovino051 (
  Fecha DATE,
  Sacrificio INTEGER
);

CREATE TABLE hembrasEnSacificio052 (
  Fecha DATE,
  Porcentaje_de_hembras FLOAT
);

CREATE TABLE ganadoGordoEnPie053 (
  Fecha DATE,
  Precio_x_kilo INTEGER
);

CREATE TABLE hembrasFlacaEnpie065 (
  Fecha DATE,
  Precio_Region_Caribe INTEGER,
  Precio_Magdalena_Medio_Santanderes INTEGER,
  Precio_Llanos_Orientales INTEGER
);

CREATE TABLE MachoCebaGordoPie071 (
  Fecha DATE,
  Precio_Region_Caribe INTEGER,
  Precio_Magdalena_Medio INTEGER,
  Precio_Llanos_Orientales INTEGER
);


