CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  username VARCHAR(100),
  fullName VARCHAR(150),
  email VARCHAR(150),
  passwordHash VARCHAR(500),
  statusUser BOOLEAN DEFAULT TRUE
);

CREATE TABLE Parametros (
  idParametro SERIAL PRIMARY KEY,
  NombreParametro VARCHAR(150),
  Valor INTEGER,
  idPadre INTEGER,
  Descripcion VARCHAR(500),
  Estado BOOLEAN DEFAULT TRUE
);

CREATE TABLE produccionesLecheSacrificio006 (
  id SERIAL PRIMARY KEY,
  Anio INTEGER,
  Sacrificio_Bovino_milesxcab INTEGER,
  Produccion_carne_Ton INTEGER,
  Tasa_extraccion_porcentage	DOUBLE PRECISION,
  Produccion_leche_cruda_millonesxlts INTEGER,
  Acopio_Industrial_millonesxlts INTEGER,
  Estado BOOLEAN DEFAULT TRUE
);

CREATE TABLE precioUSDNovilloGordoPie014 (
  id SERIAL PRIMARY KEY,
  Pais VARCHAR(50),
  Fecha DATE,
  Precio DOUBLE PRECISION,
  Estado BOOLEAN DEFAULT TRUE
);

CREATE TABLE PrecioLecheCrudaUSDxL018 (
  id SERIAL PRIMARY KEY,
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
  China DOUBLE PRECISION,
  Estado BOOLEAN DEFAULT TRUE
);

CREATE TABLE costosProduccion020 (
  id SERIAL PRIMARY KEY,
  Indice	INTEGER,
  Anio	INTEGER,
  Valor	FLOAT,
  Estado BOOLEAN DEFAULT TRUE
);

CREATE TABLE consumosAnualCarne023 (
  id SERIAL PRIMARY KEY,
  Anio INTEGER,
  Consumo_proteina_animal	FLOAT,
  Carne_res_kgxhab FLOAT,
  Carne_pollo_kgxhab FLOAT,
  Carne_cerdo_kgxhab FLOAT,
  Leche_Ltxhab FLOAT,
  Pescado_kgxhab FLOAT,
  Estado BOOLEAN DEFAULT TRUE
);

CREATE TABLE consumosAnualesLeche023 (
  id SERIAL PRIMARY KEY,
  Anio INTEGER,
  Leche_Ltxhab DOUBLE PRECISION,
  Estado BOOLEAN DEFAULT TRUE
);

CREATE TABLE litroLechePagado046 (
  id SERIAL PRIMARY KEY,
  Bonificacion INTEGER,
  Fecha DATE,
  Precio_por_litro_Nacional DOUBLE PRECISION,
  Estado BOOLEAN DEFAULT TRUE
);

CREATE TABLE producionesCarne048 (
  id SERIAL PRIMARY KEY,
  Anio INTEGER,
  Toneladas_eq_canal INTEGER,
  Estado BOOLEAN DEFAULT TRUE
);

CREATE TABLE ProduccionAcopioLeche050 (
  id SERIAL PRIMARY KEY,
  Anio INTEGER,
  Produccion_millonesxlts DOUBLE PRECISION,
  Acopio_millonesxlts DOUBLE PRECISION,
  Estado BOOLEAN DEFAULT TRUE
);

CREATE TABLE sacrificioMensualBovino051 (
  id SERIAL PRIMARY KEY,
  Fecha DATE,
  Sacrificio INTEGER,
  Estado BOOLEAN DEFAULT TRUE
);

CREATE TABLE hembrasEnSacificio052 (
  id SERIAL PRIMARY KEY,
  Fecha DATE,
  Porcentaje_de_hembras FLOAT,
  Estado BOOLEAN DEFAULT TRUE
);

CREATE TABLE ganadoGordoEnPie053 (
  id SERIAL PRIMARY KEY,
  Fecha DATE,
  Precio_x_kilo INTEGER,
  Estado BOOLEAN DEFAULT TRUE
);

CREATE TABLE hembrasFlacaEnpie065 (
  id SERIAL PRIMARY KEY,
  Fecha DATE,
  Precio_Region_Caribe INTEGER,
  Precio_Magdalena_Medio_Santanderes INTEGER,
  Precio_Llanos_Orientales INTEGER,
  Estado BOOLEAN DEFAULT TRUE
);

CREATE TABLE MachoCebaGordoPie071 (
  id SERIAL PRIMARY KEY,
  Fecha DATE,
  Precio_Region_Caribe INTEGER,
  Precio_Magdalena_Medio INTEGER,
  Precio_Llanos_Orientales INTEGER,
  Estado BOOLEAN DEFAULT TRUE
);


