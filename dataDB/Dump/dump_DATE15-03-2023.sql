--
-- PostgreSQL database dump
--

-- Dumped from database version 15.2
-- Dumped by pg_dump version 15.1

-- Started on 2023-03-16 02:19:15 UTC

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 225 (class 1259 OID 16477)
-- Name: consumosanualcarne023; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE public.consumosanualcarne023 (
    id integer NOT NULL,
    anio integer,
    consumo_proteina_animal double precision,
    carne_res_kgxhab double precision,
    carne_pollo_kgxhab double precision,
    carne_cerdo_kgxhab double precision,
    leche_ltxhab double precision,
    pescado_kgxhab double precision,
    estado boolean DEFAULT true
);


ALTER TABLE public.consumosanualcarne023 OWNER TO root;

--
-- TOC entry 224 (class 1259 OID 16476)
-- Name: consumosanualcarne023_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE public.consumosanualcarne023_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.consumosanualcarne023_id_seq OWNER TO root;

--
-- TOC entry 3482 (class 0 OID 0)
-- Dependencies: 224
-- Name: consumosanualcarne023_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE public.consumosanualcarne023_id_seq OWNED BY public.consumosanualcarne023.id;


--
-- TOC entry 227 (class 1259 OID 16485)
-- Name: consumosanualesleche023; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE public.consumosanualesleche023 (
    id integer NOT NULL,
    anio integer,
    leche_ltxhab double precision,
    estado boolean DEFAULT true
);


ALTER TABLE public.consumosanualesleche023 OWNER TO root;

--
-- TOC entry 226 (class 1259 OID 16484)
-- Name: consumosanualesleche023_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE public.consumosanualesleche023_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.consumosanualesleche023_id_seq OWNER TO root;

--
-- TOC entry 3483 (class 0 OID 0)
-- Dependencies: 226
-- Name: consumosanualesleche023_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE public.consumosanualesleche023_id_seq OWNED BY public.consumosanualesleche023.id;


--
-- TOC entry 223 (class 1259 OID 16469)
-- Name: costosproduccion020; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE public.costosproduccion020 (
    id integer NOT NULL,
    indice integer,
    anio integer,
    valor double precision,
    estado boolean DEFAULT true
);


ALTER TABLE public.costosproduccion020 OWNER TO root;

--
-- TOC entry 222 (class 1259 OID 16468)
-- Name: costosproduccion020_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE public.costosproduccion020_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.costosproduccion020_id_seq OWNER TO root;

--
-- TOC entry 3484 (class 0 OID 0)
-- Dependencies: 222
-- Name: costosproduccion020_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE public.costosproduccion020_id_seq OWNED BY public.costosproduccion020.id;


--
-- TOC entry 239 (class 1259 OID 16533)
-- Name: ganadogordoenpie053; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE public.ganadogordoenpie053 (
    id integer NOT NULL,
    fecha date,
    precio_x_kilo integer,
    estado boolean DEFAULT true
);


ALTER TABLE public.ganadogordoenpie053 OWNER TO root;

--
-- TOC entry 238 (class 1259 OID 16532)
-- Name: ganadogordoenpie053_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE public.ganadogordoenpie053_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ganadogordoenpie053_id_seq OWNER TO root;

--
-- TOC entry 3485 (class 0 OID 0)
-- Dependencies: 238
-- Name: ganadogordoenpie053_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE public.ganadogordoenpie053_id_seq OWNED BY public.ganadogordoenpie053.id;


--
-- TOC entry 237 (class 1259 OID 16525)
-- Name: hembrasensacificio052; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE public.hembrasensacificio052 (
    id integer NOT NULL,
    fecha date,
    porcentaje_de_hembras double precision,
    estado boolean DEFAULT true
);


ALTER TABLE public.hembrasensacificio052 OWNER TO root;

--
-- TOC entry 236 (class 1259 OID 16524)
-- Name: hembrasensacificio052_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE public.hembrasensacificio052_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.hembrasensacificio052_id_seq OWNER TO root;

--
-- TOC entry 3486 (class 0 OID 0)
-- Dependencies: 236
-- Name: hembrasensacificio052_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE public.hembrasensacificio052_id_seq OWNED BY public.hembrasensacificio052.id;


--
-- TOC entry 241 (class 1259 OID 16541)
-- Name: hembrasflacaenpie065; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE public.hembrasflacaenpie065 (
    id integer NOT NULL,
    fecha date,
    precio_region_caribe integer,
    precio_magdalena_medio_santanderes integer,
    precio_llanos_orientales integer,
    estado boolean DEFAULT true
);


ALTER TABLE public.hembrasflacaenpie065 OWNER TO root;

--
-- TOC entry 240 (class 1259 OID 16540)
-- Name: hembrasflacaenpie065_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE public.hembrasflacaenpie065_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.hembrasflacaenpie065_id_seq OWNER TO root;

--
-- TOC entry 3487 (class 0 OID 0)
-- Dependencies: 240
-- Name: hembrasflacaenpie065_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE public.hembrasflacaenpie065_id_seq OWNED BY public.hembrasflacaenpie065.id;


--
-- TOC entry 229 (class 1259 OID 16493)
-- Name: litrolechepagado046; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE public.litrolechepagado046 (
    id integer NOT NULL,
    bonificacion integer,
    fecha date,
    precio_por_litro_nacional double precision,
    estado boolean DEFAULT true
);


ALTER TABLE public.litrolechepagado046 OWNER TO root;

--
-- TOC entry 228 (class 1259 OID 16492)
-- Name: litrolechepagado046_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE public.litrolechepagado046_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.litrolechepagado046_id_seq OWNER TO root;

--
-- TOC entry 3488 (class 0 OID 0)
-- Dependencies: 228
-- Name: litrolechepagado046_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE public.litrolechepagado046_id_seq OWNED BY public.litrolechepagado046.id;


--
-- TOC entry 243 (class 1259 OID 16549)
-- Name: machocebagordopie071; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE public.machocebagordopie071 (
    id integer NOT NULL,
    fecha date,
    precio_region_caribe integer,
    precio_magdalena_medio integer,
    precio_llanos_orientales integer,
    estado boolean DEFAULT true
);


ALTER TABLE public.machocebagordopie071 OWNER TO root;

--
-- TOC entry 242 (class 1259 OID 16548)
-- Name: machocebagordopie071_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE public.machocebagordopie071_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.machocebagordopie071_id_seq OWNER TO root;

--
-- TOC entry 3489 (class 0 OID 0)
-- Dependencies: 242
-- Name: machocebagordopie071_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE public.machocebagordopie071_id_seq OWNED BY public.machocebagordopie071.id;


--
-- TOC entry 215 (class 1259 OID 16435)
-- Name: parametros; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE public.parametros (
    idparametro integer NOT NULL,
    nombreparametro character varying(150),
    valor integer,
    idpadre integer,
    descripcion character varying(500),
    estado boolean DEFAULT true
);


ALTER TABLE public.parametros OWNER TO root;

--
-- TOC entry 214 (class 1259 OID 16434)
-- Name: parametros_idparametro_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE public.parametros_idparametro_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.parametros_idparametro_seq OWNER TO root;

--
-- TOC entry 3490 (class 0 OID 0)
-- Dependencies: 214
-- Name: parametros_idparametro_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE public.parametros_idparametro_seq OWNED BY public.parametros.idparametro;


--
-- TOC entry 221 (class 1259 OID 16461)
-- Name: preciolechecrudausdxl018; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE public.preciolechecrudausdxl018 (
    id integer NOT NULL,
    fecha date,
    argentina double precision,
    brasil double precision,
    chile double precision,
    colombia double precision,
    estados_unidos double precision,
    union_europea double precision,
    uruguay double precision,
    mexico double precision,
    nueva_zelanda double precision,
    china double precision,
    estado boolean DEFAULT true
);


ALTER TABLE public.preciolechecrudausdxl018 OWNER TO root;

--
-- TOC entry 220 (class 1259 OID 16460)
-- Name: preciolechecrudausdxl018_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE public.preciolechecrudausdxl018_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.preciolechecrudausdxl018_id_seq OWNER TO root;

--
-- TOC entry 3491 (class 0 OID 0)
-- Dependencies: 220
-- Name: preciolechecrudausdxl018_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE public.preciolechecrudausdxl018_id_seq OWNED BY public.preciolechecrudausdxl018.id;


--
-- TOC entry 219 (class 1259 OID 16453)
-- Name: preciousdnovillogordopie014; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE public.preciousdnovillogordopie014 (
    id integer NOT NULL,
    pais character varying(50),
    fecha date,
    precio double precision,
    estado boolean DEFAULT true
);


ALTER TABLE public.preciousdnovillogordopie014 OWNER TO root;

--
-- TOC entry 218 (class 1259 OID 16452)
-- Name: preciousdnovillogordopie014_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE public.preciousdnovillogordopie014_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.preciousdnovillogordopie014_id_seq OWNER TO root;

--
-- TOC entry 3492 (class 0 OID 0)
-- Dependencies: 218
-- Name: preciousdnovillogordopie014_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE public.preciousdnovillogordopie014_id_seq OWNED BY public.preciousdnovillogordopie014.id;


--
-- TOC entry 233 (class 1259 OID 16509)
-- Name: produccionacopioleche050; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE public.produccionacopioleche050 (
    id integer NOT NULL,
    anio integer,
    produccion_millonesxlts double precision,
    acopio_millonesxlts double precision,
    estado boolean DEFAULT true
);


ALTER TABLE public.produccionacopioleche050 OWNER TO root;

--
-- TOC entry 232 (class 1259 OID 16508)
-- Name: produccionacopioleche050_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE public.produccionacopioleche050_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.produccionacopioleche050_id_seq OWNER TO root;

--
-- TOC entry 3493 (class 0 OID 0)
-- Dependencies: 232
-- Name: produccionacopioleche050_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE public.produccionacopioleche050_id_seq OWNED BY public.produccionacopioleche050.id;


--
-- TOC entry 217 (class 1259 OID 16445)
-- Name: produccioneslechesacrificio006; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE public.produccioneslechesacrificio006 (
    id integer NOT NULL,
    anio integer,
    sacrificio_bovino_milesxcab integer,
    produccion_carne_ton integer,
    tasa_extraccion_porcentage double precision,
    produccion_leche_cruda_millonesxlts integer,
    acopio_industrial_millonesxlts integer,
    estado boolean DEFAULT true
);


ALTER TABLE public.produccioneslechesacrificio006 OWNER TO root;

--
-- TOC entry 216 (class 1259 OID 16444)
-- Name: produccioneslechesacrificio006_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE public.produccioneslechesacrificio006_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.produccioneslechesacrificio006_id_seq OWNER TO root;

--
-- TOC entry 3494 (class 0 OID 0)
-- Dependencies: 216
-- Name: produccioneslechesacrificio006_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE public.produccioneslechesacrificio006_id_seq OWNED BY public.produccioneslechesacrificio006.id;


--
-- TOC entry 231 (class 1259 OID 16501)
-- Name: producionescarne048; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE public.producionescarne048 (
    id integer NOT NULL,
    anio integer,
    toneladas_eq_canal integer,
    estado boolean DEFAULT true
);


ALTER TABLE public.producionescarne048 OWNER TO root;

--
-- TOC entry 230 (class 1259 OID 16500)
-- Name: producionescarne048_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE public.producionescarne048_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.producionescarne048_id_seq OWNER TO root;

--
-- TOC entry 3495 (class 0 OID 0)
-- Dependencies: 230
-- Name: producionescarne048_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE public.producionescarne048_id_seq OWNED BY public.producionescarne048.id;


--
-- TOC entry 235 (class 1259 OID 16517)
-- Name: sacrificiomensualbovino051; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE public.sacrificiomensualbovino051 (
    id integer NOT NULL,
    fecha date,
    sacrificio integer,
    estado boolean DEFAULT true
);


ALTER TABLE public.sacrificiomensualbovino051 OWNER TO root;

--
-- TOC entry 234 (class 1259 OID 16516)
-- Name: sacrificiomensualbovino051_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE public.sacrificiomensualbovino051_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.sacrificiomensualbovino051_id_seq OWNER TO root;

--
-- TOC entry 3496 (class 0 OID 0)
-- Dependencies: 234
-- Name: sacrificiomensualbovino051_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE public.sacrificiomensualbovino051_id_seq OWNED BY public.sacrificiomensualbovino051.id;


--
-- TOC entry 245 (class 1259 OID 32819)
-- Name: users; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE public.users (
    id integer NOT NULL,
    username character varying(100),
    fullname character varying(150),
    email character varying(150),
    passwordhash character varying(500),
    statususer boolean DEFAULT true
);


ALTER TABLE public.users OWNER TO root;

--
-- TOC entry 244 (class 1259 OID 32818)
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE public.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_id_seq OWNER TO root;

--
-- TOC entry 3497 (class 0 OID 0)
-- Dependencies: 244
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;


--
-- TOC entry 3281 (class 2604 OID 16480)
-- Name: consumosanualcarne023 id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.consumosanualcarne023 ALTER COLUMN id SET DEFAULT nextval('public.consumosanualcarne023_id_seq'::regclass);


--
-- TOC entry 3283 (class 2604 OID 16488)
-- Name: consumosanualesleche023 id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.consumosanualesleche023 ALTER COLUMN id SET DEFAULT nextval('public.consumosanualesleche023_id_seq'::regclass);


--
-- TOC entry 3279 (class 2604 OID 16472)
-- Name: costosproduccion020 id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.costosproduccion020 ALTER COLUMN id SET DEFAULT nextval('public.costosproduccion020_id_seq'::regclass);


--
-- TOC entry 3295 (class 2604 OID 16536)
-- Name: ganadogordoenpie053 id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.ganadogordoenpie053 ALTER COLUMN id SET DEFAULT nextval('public.ganadogordoenpie053_id_seq'::regclass);


--
-- TOC entry 3293 (class 2604 OID 16528)
-- Name: hembrasensacificio052 id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.hembrasensacificio052 ALTER COLUMN id SET DEFAULT nextval('public.hembrasensacificio052_id_seq'::regclass);


--
-- TOC entry 3297 (class 2604 OID 16544)
-- Name: hembrasflacaenpie065 id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.hembrasflacaenpie065 ALTER COLUMN id SET DEFAULT nextval('public.hembrasflacaenpie065_id_seq'::regclass);


--
-- TOC entry 3285 (class 2604 OID 16496)
-- Name: litrolechepagado046 id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.litrolechepagado046 ALTER COLUMN id SET DEFAULT nextval('public.litrolechepagado046_id_seq'::regclass);


--
-- TOC entry 3299 (class 2604 OID 16552)
-- Name: machocebagordopie071 id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.machocebagordopie071 ALTER COLUMN id SET DEFAULT nextval('public.machocebagordopie071_id_seq'::regclass);


--
-- TOC entry 3271 (class 2604 OID 16438)
-- Name: parametros idparametro; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.parametros ALTER COLUMN idparametro SET DEFAULT nextval('public.parametros_idparametro_seq'::regclass);


--
-- TOC entry 3277 (class 2604 OID 16464)
-- Name: preciolechecrudausdxl018 id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.preciolechecrudausdxl018 ALTER COLUMN id SET DEFAULT nextval('public.preciolechecrudausdxl018_id_seq'::regclass);


--
-- TOC entry 3275 (class 2604 OID 16456)
-- Name: preciousdnovillogordopie014 id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.preciousdnovillogordopie014 ALTER COLUMN id SET DEFAULT nextval('public.preciousdnovillogordopie014_id_seq'::regclass);


--
-- TOC entry 3289 (class 2604 OID 16512)
-- Name: produccionacopioleche050 id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.produccionacopioleche050 ALTER COLUMN id SET DEFAULT nextval('public.produccionacopioleche050_id_seq'::regclass);


--
-- TOC entry 3273 (class 2604 OID 16448)
-- Name: produccioneslechesacrificio006 id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.produccioneslechesacrificio006 ALTER COLUMN id SET DEFAULT nextval('public.produccioneslechesacrificio006_id_seq'::regclass);


--
-- TOC entry 3287 (class 2604 OID 16504)
-- Name: producionescarne048 id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.producionescarne048 ALTER COLUMN id SET DEFAULT nextval('public.producionescarne048_id_seq'::regclass);


--
-- TOC entry 3291 (class 2604 OID 16520)
-- Name: sacrificiomensualbovino051 id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.sacrificiomensualbovino051 ALTER COLUMN id SET DEFAULT nextval('public.sacrificiomensualbovino051_id_seq'::regclass);


--
-- TOC entry 3301 (class 2604 OID 32822)
-- Name: users id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- TOC entry 3314 (class 2606 OID 16483)
-- Name: consumosanualcarne023 consumosanualcarne023_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.consumosanualcarne023
    ADD CONSTRAINT consumosanualcarne023_pkey PRIMARY KEY (id);


--
-- TOC entry 3316 (class 2606 OID 16491)
-- Name: consumosanualesleche023 consumosanualesleche023_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.consumosanualesleche023
    ADD CONSTRAINT consumosanualesleche023_pkey PRIMARY KEY (id);


--
-- TOC entry 3312 (class 2606 OID 16475)
-- Name: costosproduccion020 costosproduccion020_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.costosproduccion020
    ADD CONSTRAINT costosproduccion020_pkey PRIMARY KEY (id);


--
-- TOC entry 3328 (class 2606 OID 16539)
-- Name: ganadogordoenpie053 ganadogordoenpie053_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.ganadogordoenpie053
    ADD CONSTRAINT ganadogordoenpie053_pkey PRIMARY KEY (id);


--
-- TOC entry 3326 (class 2606 OID 16531)
-- Name: hembrasensacificio052 hembrasensacificio052_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.hembrasensacificio052
    ADD CONSTRAINT hembrasensacificio052_pkey PRIMARY KEY (id);


--
-- TOC entry 3330 (class 2606 OID 16547)
-- Name: hembrasflacaenpie065 hembrasflacaenpie065_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.hembrasflacaenpie065
    ADD CONSTRAINT hembrasflacaenpie065_pkey PRIMARY KEY (id);


--
-- TOC entry 3318 (class 2606 OID 16499)
-- Name: litrolechepagado046 litrolechepagado046_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.litrolechepagado046
    ADD CONSTRAINT litrolechepagado046_pkey PRIMARY KEY (id);


--
-- TOC entry 3332 (class 2606 OID 16555)
-- Name: machocebagordopie071 machocebagordopie071_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.machocebagordopie071
    ADD CONSTRAINT machocebagordopie071_pkey PRIMARY KEY (id);


--
-- TOC entry 3304 (class 2606 OID 16443)
-- Name: parametros parametros_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.parametros
    ADD CONSTRAINT parametros_pkey PRIMARY KEY (idparametro);


--
-- TOC entry 3310 (class 2606 OID 16467)
-- Name: preciolechecrudausdxl018 preciolechecrudausdxl018_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.preciolechecrudausdxl018
    ADD CONSTRAINT preciolechecrudausdxl018_pkey PRIMARY KEY (id);


--
-- TOC entry 3308 (class 2606 OID 16459)
-- Name: preciousdnovillogordopie014 preciousdnovillogordopie014_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.preciousdnovillogordopie014
    ADD CONSTRAINT preciousdnovillogordopie014_pkey PRIMARY KEY (id);


--
-- TOC entry 3322 (class 2606 OID 16515)
-- Name: produccionacopioleche050 produccionacopioleche050_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.produccionacopioleche050
    ADD CONSTRAINT produccionacopioleche050_pkey PRIMARY KEY (id);


--
-- TOC entry 3306 (class 2606 OID 16451)
-- Name: produccioneslechesacrificio006 produccioneslechesacrificio006_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.produccioneslechesacrificio006
    ADD CONSTRAINT produccioneslechesacrificio006_pkey PRIMARY KEY (id);


--
-- TOC entry 3320 (class 2606 OID 16507)
-- Name: producionescarne048 producionescarne048_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.producionescarne048
    ADD CONSTRAINT producionescarne048_pkey PRIMARY KEY (id);


--
-- TOC entry 3324 (class 2606 OID 16523)
-- Name: sacrificiomensualbovino051 sacrificiomensualbovino051_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.sacrificiomensualbovino051
    ADD CONSTRAINT sacrificiomensualbovino051_pkey PRIMARY KEY (id);


--
-- TOC entry 3334 (class 2606 OID 32827)
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


-- Completed on 2023-03-16 02:19:19 UTC

--
-- PostgreSQL database dump complete
--

