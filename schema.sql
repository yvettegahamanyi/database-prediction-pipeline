--
-- PostgreSQL database dump
--

\restrict Ob4bfEnY17oWT2S2DnqOLzBWPtm15qj9Q7cY60SaV1wzQMvMLnuK8XpkwcsAfDr

-- Dumped from database version 17.6 (Debian 17.6-2.pgdg12+1)
-- Dumped by pg_dump version 17.6 (Debian 17.6-2.pgdg13+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: public; Type: SCHEMA; Schema: -; Owner: heart_disease_dataset_user
--

-- *not* creating schema, since initdb creates it


ALTER SCHEMA public OWNER TO heart_disease_dataset_user;

--
-- Name: pg_stat_statements; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS pg_stat_statements WITH SCHEMA public;


--
-- Name: EXTENSION pg_stat_statements; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION pg_stat_statements IS 'track planning and execution statistics of all SQL statements executed';


--
-- Name: add_patient_record(double precision, double precision, double precision, double precision, double precision, double precision, double precision, double precision, double precision, double precision, double precision, double precision, double precision, double precision, double precision, double precision, double precision, double precision, double precision, double precision, double precision, double precision); Type: PROCEDURE; Schema: public; Owner: heart_disease_dataset_user
--

CREATE PROCEDURE public.add_patient_record(IN _sex double precision, IN _age double precision, IN _education double precision, IN _income double precision, IN _bmi double precision, IN _smoker double precision, IN _phys_activity double precision, IN _fruits double precision, IN _veggies double precision, IN _hvy_alcohol_consump double precision, IN _heart_disease_or_attack double precision, IN _high_bp double precision, IN _high_chol double precision, IN _chol_check double precision, IN _stroke double precision, IN _diabetes double precision, IN _any_healthcare double precision, IN _no_docbc_cost double precision, IN _gen_hlth double precision, IN _ment_hlth double precision, IN _phys_hlth double precision, IN _diff_walk double precision)
    LANGUAGE plpgsql
    AS $$
DECLARE
    new_patient_id INT;
BEGIN
    -- Insert into patients
    INSERT INTO patients (sex, age, education, income)
    VALUES (_sex, _age, _education, _income)
    RETURNING patient_id INTO new_patient_id;

    -- Insert into health_indicators
    INSERT INTO health_indicators (patient_id, bmi, smoker, phys_activity, fruits, veggies, hvy_alcohol_consump)
    VALUES (new_patient_id, _bmi, _smoker, _phys_activity, _fruits, _veggies, _hvy_alcohol_consump);

    -- Insert into medical_history
    INSERT INTO medical_history (
        patient_id, heart_disease_or_attack, high_bp, high_chol, chol_check, stroke,
        diabetes, any_healthcare, no_docbc_cost, gen_hlth, ment_hlth, phys_hlth, diff_walk
    )
    VALUES (
        new_patient_id, _heart_disease_or_attack, _high_bp, _high_chol, _chol_check, _stroke,
        _diabetes, _any_healthcare, _no_docbc_cost, _gen_hlth, _ment_hlth, _phys_hlth, _diff_walk
    );

    RAISE NOTICE 'Patient % added successfully', new_patient_id;
END;
$$;


ALTER PROCEDURE public.add_patient_record(IN _sex double precision, IN _age double precision, IN _education double precision, IN _income double precision, IN _bmi double precision, IN _smoker double precision, IN _phys_activity double precision, IN _fruits double precision, IN _veggies double precision, IN _hvy_alcohol_consump double precision, IN _heart_disease_or_attack double precision, IN _high_bp double precision, IN _high_chol double precision, IN _chol_check double precision, IN _stroke double precision, IN _diabetes double precision, IN _any_healthcare double precision, IN _no_docbc_cost double precision, IN _gen_hlth double precision, IN _ment_hlth double precision, IN _phys_hlth double precision, IN _diff_walk double precision) OWNER TO heart_disease_dataset_user;

--
-- Name: add_patient_record(integer, integer, integer, integer, double precision, integer, integer, integer, integer, integer, integer, integer, integer, integer, integer, integer, integer, integer, integer, integer, integer, integer); Type: PROCEDURE; Schema: public; Owner: heart_disease_dataset_user
--

CREATE PROCEDURE public.add_patient_record(IN _sex integer, IN _age integer, IN _education integer, IN _income integer, IN _bmi double precision, IN _smoker integer, IN _phys_activity integer, IN _fruits integer, IN _veggies integer, IN _hvy_alcohol_consump integer, IN _heart_disease_or_attack integer, IN _high_bp integer, IN _high_chol integer, IN _chol_check integer, IN _stroke integer, IN _diabetes integer, IN _any_healthcare integer, IN _no_docbc_cost integer, IN _gen_hlth integer, IN _ment_hlth integer, IN _phys_hlth integer, IN _diff_walk integer)
    LANGUAGE plpgsql
    AS $$
DECLARE
    new_patient_id INT;
BEGIN
    -- Insert into patients
    INSERT INTO patients (sex, age, education, income)
    VALUES (_sex, _age, _education, _income)
    RETURNING patient_id INTO new_patient_id;

    -- Insert into health_indicators
    INSERT INTO health_indicators (patient_id, bmi, smoker, phys_activity, fruits, veggies, hvy_alcohol_consump)
    VALUES (new_patient_id, _bmi, _smoker, _phys_activity, _fruits, _veggies, _hvy_alcohol_consump);

    -- Insert into medical_history
    INSERT INTO medical_history (
        patient_id, heart_disease_or_attack, high_bp, high_chol, chol_check, stroke,
        diabetes, any_healthcare, no_docbc_cost, gen_hlth, ment_hlth, phys_hlth, diff_walk
    )
    VALUES (
        new_patient_id, _heart_disease_or_attack, _high_bp, _high_chol, _chol_check, _stroke,
        _diabetes, _any_healthcare, _no_docbc_cost, _gen_hlth, _ment_hlth, _phys_hlth, _diff_walk
    );

    RAISE NOTICE 'Patient % added successfully', new_patient_id;
END;
$$;


ALTER PROCEDURE public.add_patient_record(IN _sex integer, IN _age integer, IN _education integer, IN _income integer, IN _bmi double precision, IN _smoker integer, IN _phys_activity integer, IN _fruits integer, IN _veggies integer, IN _hvy_alcohol_consump integer, IN _heart_disease_or_attack integer, IN _high_bp integer, IN _high_chol integer, IN _chol_check integer, IN _stroke integer, IN _diabetes integer, IN _any_healthcare integer, IN _no_docbc_cost integer, IN _gen_hlth integer, IN _ment_hlth integer, IN _phys_hlth integer, IN _diff_walk integer) OWNER TO heart_disease_dataset_user;

--
-- Name: validate_healthcare_access(); Type: FUNCTION; Schema: public; Owner: heart_disease_dataset_user
--

CREATE FUNCTION public.validate_healthcare_access() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
BEGIN
    -- Rule: cannot have a cholesterol check if no healthcare access
    IF NEW.any_healthcare = 0 AND NEW.chol_check = 1 THEN
        RAISE EXCEPTION 'Invalid data: Cannot have a cholesterol check without healthcare access.';
    END IF;
    RETURN NEW;
END;
$$;


ALTER FUNCTION public.validate_healthcare_access() OWNER TO heart_disease_dataset_user;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: health_indicators; Type: TABLE; Schema: public; Owner: heart_disease_dataset_user
--

CREATE TABLE public.health_indicators (
    indicator_id integer NOT NULL,
    patient_id integer,
    bmi double precision,
    smoker double precision,
    phys_activity double precision,
    fruits double precision,
    veggies double precision,
    hvy_alcohol_consump double precision
);


ALTER TABLE public.health_indicators OWNER TO heart_disease_dataset_user;

--
-- Name: health_indicators_indicator_id_seq; Type: SEQUENCE; Schema: public; Owner: heart_disease_dataset_user
--

CREATE SEQUENCE public.health_indicators_indicator_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.health_indicators_indicator_id_seq OWNER TO heart_disease_dataset_user;

--
-- Name: health_indicators_indicator_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: heart_disease_dataset_user
--

ALTER SEQUENCE public.health_indicators_indicator_id_seq OWNED BY public.health_indicators.indicator_id;


--
-- Name: heart_desease_predictions; Type: TABLE; Schema: public; Owner: heart_disease_dataset_user
--

CREATE TABLE public.heart_desease_predictions (
    prediction_id integer NOT NULL,
    patient_id integer,
    predition double precision,
    created_at timestamp without time zone DEFAULT now(),
    CONSTRAINT heart_desease_predictions_predition_check CHECK (((predition >= (0)::double precision) AND (predition <= (1)::double precision)))
);


ALTER TABLE public.heart_desease_predictions OWNER TO heart_disease_dataset_user;

--
-- Name: heart_desease_predictions_prediction_id_seq; Type: SEQUENCE; Schema: public; Owner: heart_disease_dataset_user
--

CREATE SEQUENCE public.heart_desease_predictions_prediction_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.heart_desease_predictions_prediction_id_seq OWNER TO heart_disease_dataset_user;

--
-- Name: heart_desease_predictions_prediction_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: heart_disease_dataset_user
--

ALTER SEQUENCE public.heart_desease_predictions_prediction_id_seq OWNED BY public.heart_desease_predictions.prediction_id;


--
-- Name: medical_history; Type: TABLE; Schema: public; Owner: heart_disease_dataset_user
--

CREATE TABLE public.medical_history (
    history_id integer NOT NULL,
    patient_id integer,
    heart_disease_or_attack double precision,
    high_bp double precision,
    high_chol double precision,
    chol_check double precision,
    stroke double precision,
    diabetes double precision,
    any_healthcare double precision,
    no_docbc_cost double precision,
    gen_hlth double precision,
    ment_hlth double precision,
    phys_hlth double precision,
    diff_walk double precision
);


ALTER TABLE public.medical_history OWNER TO heart_disease_dataset_user;

--
-- Name: medical_history_history_id_seq; Type: SEQUENCE; Schema: public; Owner: heart_disease_dataset_user
--

CREATE SEQUENCE public.medical_history_history_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.medical_history_history_id_seq OWNER TO heart_disease_dataset_user;

--
-- Name: medical_history_history_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: heart_disease_dataset_user
--

ALTER SEQUENCE public.medical_history_history_id_seq OWNED BY public.medical_history.history_id;


--
-- Name: patients; Type: TABLE; Schema: public; Owner: heart_disease_dataset_user
--

CREATE TABLE public.patients (
    patient_id integer NOT NULL,
    sex double precision,
    age double precision,
    education double precision,
    income double precision
);


ALTER TABLE public.patients OWNER TO heart_disease_dataset_user;

--
-- Name: patients_patient_id_seq; Type: SEQUENCE; Schema: public; Owner: heart_disease_dataset_user
--

CREATE SEQUENCE public.patients_patient_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.patients_patient_id_seq OWNER TO heart_disease_dataset_user;

--
-- Name: patients_patient_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: heart_disease_dataset_user
--

ALTER SEQUENCE public.patients_patient_id_seq OWNED BY public.patients.patient_id;


--
-- Name: predictions; Type: TABLE; Schema: public; Owner: heart_disease_dataset_user
--

CREATE TABLE public.predictions (
    id integer NOT NULL,
    patient_id integer,
    probability double precision,
    prediction integer,
    created_at timestamp without time zone DEFAULT now()
);


ALTER TABLE public.predictions OWNER TO heart_disease_dataset_user;

--
-- Name: predictions_id_seq; Type: SEQUENCE; Schema: public; Owner: heart_disease_dataset_user
--

CREATE SEQUENCE public.predictions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.predictions_id_seq OWNER TO heart_disease_dataset_user;

--
-- Name: predictions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: heart_disease_dataset_user
--

ALTER SEQUENCE public.predictions_id_seq OWNED BY public.predictions.id;


--
-- Name: health_indicators indicator_id; Type: DEFAULT; Schema: public; Owner: heart_disease_dataset_user
--

ALTER TABLE ONLY public.health_indicators ALTER COLUMN indicator_id SET DEFAULT nextval('public.health_indicators_indicator_id_seq'::regclass);


--
-- Name: heart_desease_predictions prediction_id; Type: DEFAULT; Schema: public; Owner: heart_disease_dataset_user
--

ALTER TABLE ONLY public.heart_desease_predictions ALTER COLUMN prediction_id SET DEFAULT nextval('public.heart_desease_predictions_prediction_id_seq'::regclass);


--
-- Name: medical_history history_id; Type: DEFAULT; Schema: public; Owner: heart_disease_dataset_user
--

ALTER TABLE ONLY public.medical_history ALTER COLUMN history_id SET DEFAULT nextval('public.medical_history_history_id_seq'::regclass);


--
-- Name: patients patient_id; Type: DEFAULT; Schema: public; Owner: heart_disease_dataset_user
--

ALTER TABLE ONLY public.patients ALTER COLUMN patient_id SET DEFAULT nextval('public.patients_patient_id_seq'::regclass);


--
-- Name: predictions id; Type: DEFAULT; Schema: public; Owner: heart_disease_dataset_user
--

ALTER TABLE ONLY public.predictions ALTER COLUMN id SET DEFAULT nextval('public.predictions_id_seq'::regclass);


--
-- Name: health_indicators health_indicators_pkey; Type: CONSTRAINT; Schema: public; Owner: heart_disease_dataset_user
--

ALTER TABLE ONLY public.health_indicators
    ADD CONSTRAINT health_indicators_pkey PRIMARY KEY (indicator_id);


--
-- Name: heart_desease_predictions heart_desease_predictions_pkey; Type: CONSTRAINT; Schema: public; Owner: heart_disease_dataset_user
--

ALTER TABLE ONLY public.heart_desease_predictions
    ADD CONSTRAINT heart_desease_predictions_pkey PRIMARY KEY (prediction_id);


--
-- Name: medical_history medical_history_pkey; Type: CONSTRAINT; Schema: public; Owner: heart_disease_dataset_user
--

ALTER TABLE ONLY public.medical_history
    ADD CONSTRAINT medical_history_pkey PRIMARY KEY (history_id);


--
-- Name: patients patients_pkey; Type: CONSTRAINT; Schema: public; Owner: heart_disease_dataset_user
--

ALTER TABLE ONLY public.patients
    ADD CONSTRAINT patients_pkey PRIMARY KEY (patient_id);


--
-- Name: predictions predictions_pkey; Type: CONSTRAINT; Schema: public; Owner: heart_disease_dataset_user
--

ALTER TABLE ONLY public.predictions
    ADD CONSTRAINT predictions_pkey PRIMARY KEY (id);


--
-- Name: health_indicators health_indicators_patient_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: heart_disease_dataset_user
--

ALTER TABLE ONLY public.health_indicators
    ADD CONSTRAINT health_indicators_patient_id_fkey FOREIGN KEY (patient_id) REFERENCES public.patients(patient_id) ON DELETE CASCADE;


--
-- Name: heart_desease_predictions heart_desease_predictions_patient_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: heart_disease_dataset_user
--

ALTER TABLE ONLY public.heart_desease_predictions
    ADD CONSTRAINT heart_desease_predictions_patient_id_fkey FOREIGN KEY (patient_id) REFERENCES public.patients(patient_id) ON DELETE CASCADE;


--
-- Name: medical_history medical_history_patient_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: heart_disease_dataset_user
--

ALTER TABLE ONLY public.medical_history
    ADD CONSTRAINT medical_history_patient_id_fkey FOREIGN KEY (patient_id) REFERENCES public.patients(patient_id) ON DELETE CASCADE;


--
-- Name: predictions predictions_patient_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: heart_disease_dataset_user
--

ALTER TABLE ONLY public.predictions
    ADD CONSTRAINT predictions_patient_id_fkey FOREIGN KEY (patient_id) REFERENCES public.patients(patient_id) ON DELETE CASCADE;


--
-- Name: FUNCTION pg_stat_statements(showtext boolean, OUT userid oid, OUT dbid oid, OUT toplevel boolean, OUT queryid bigint, OUT query text, OUT plans bigint, OUT total_plan_time double precision, OUT min_plan_time double precision, OUT max_plan_time double precision, OUT mean_plan_time double precision, OUT stddev_plan_time double precision, OUT calls bigint, OUT total_exec_time double precision, OUT min_exec_time double precision, OUT max_exec_time double precision, OUT mean_exec_time double precision, OUT stddev_exec_time double precision, OUT rows bigint, OUT shared_blks_hit bigint, OUT shared_blks_read bigint, OUT shared_blks_dirtied bigint, OUT shared_blks_written bigint, OUT local_blks_hit bigint, OUT local_blks_read bigint, OUT local_blks_dirtied bigint, OUT local_blks_written bigint, OUT temp_blks_read bigint, OUT temp_blks_written bigint, OUT shared_blk_read_time double precision, OUT shared_blk_write_time double precision, OUT local_blk_read_time double precision, OUT local_blk_write_time double precision, OUT temp_blk_read_time double precision, OUT temp_blk_write_time double precision, OUT wal_records bigint, OUT wal_fpi bigint, OUT wal_bytes numeric, OUT jit_functions bigint, OUT jit_generation_time double precision, OUT jit_inlining_count bigint, OUT jit_inlining_time double precision, OUT jit_optimization_count bigint, OUT jit_optimization_time double precision, OUT jit_emission_count bigint, OUT jit_emission_time double precision, OUT jit_deform_count bigint, OUT jit_deform_time double precision, OUT stats_since timestamp with time zone, OUT minmax_stats_since timestamp with time zone); Type: ACL; Schema: public; Owner: postgres
--

GRANT ALL ON FUNCTION public.pg_stat_statements(showtext boolean, OUT userid oid, OUT dbid oid, OUT toplevel boolean, OUT queryid bigint, OUT query text, OUT plans bigint, OUT total_plan_time double precision, OUT min_plan_time double precision, OUT max_plan_time double precision, OUT mean_plan_time double precision, OUT stddev_plan_time double precision, OUT calls bigint, OUT total_exec_time double precision, OUT min_exec_time double precision, OUT max_exec_time double precision, OUT mean_exec_time double precision, OUT stddev_exec_time double precision, OUT rows bigint, OUT shared_blks_hit bigint, OUT shared_blks_read bigint, OUT shared_blks_dirtied bigint, OUT shared_blks_written bigint, OUT local_blks_hit bigint, OUT local_blks_read bigint, OUT local_blks_dirtied bigint, OUT local_blks_written bigint, OUT temp_blks_read bigint, OUT temp_blks_written bigint, OUT shared_blk_read_time double precision, OUT shared_blk_write_time double precision, OUT local_blk_read_time double precision, OUT local_blk_write_time double precision, OUT temp_blk_read_time double precision, OUT temp_blk_write_time double precision, OUT wal_records bigint, OUT wal_fpi bigint, OUT wal_bytes numeric, OUT jit_functions bigint, OUT jit_generation_time double precision, OUT jit_inlining_count bigint, OUT jit_inlining_time double precision, OUT jit_optimization_count bigint, OUT jit_optimization_time double precision, OUT jit_emission_count bigint, OUT jit_emission_time double precision, OUT jit_deform_count bigint, OUT jit_deform_time double precision, OUT stats_since timestamp with time zone, OUT minmax_stats_since timestamp with time zone) TO heart_disease_dataset_user;


--
-- Name: FUNCTION pg_stat_statements_info(OUT dealloc bigint, OUT stats_reset timestamp with time zone); Type: ACL; Schema: public; Owner: postgres
--

GRANT ALL ON FUNCTION public.pg_stat_statements_info(OUT dealloc bigint, OUT stats_reset timestamp with time zone) TO heart_disease_dataset_user;


--
-- Name: DEFAULT PRIVILEGES FOR SEQUENCES; Type: DEFAULT ACL; Schema: -; Owner: postgres
--

ALTER DEFAULT PRIVILEGES FOR ROLE postgres GRANT ALL ON SEQUENCES TO heart_disease_dataset_user;


--
-- Name: DEFAULT PRIVILEGES FOR TYPES; Type: DEFAULT ACL; Schema: -; Owner: postgres
--

ALTER DEFAULT PRIVILEGES FOR ROLE postgres GRANT ALL ON TYPES TO heart_disease_dataset_user;


--
-- Name: DEFAULT PRIVILEGES FOR FUNCTIONS; Type: DEFAULT ACL; Schema: -; Owner: postgres
--

ALTER DEFAULT PRIVILEGES FOR ROLE postgres GRANT ALL ON FUNCTIONS TO heart_disease_dataset_user;


--
-- Name: DEFAULT PRIVILEGES FOR TABLES; Type: DEFAULT ACL; Schema: -; Owner: postgres
--

ALTER DEFAULT PRIVILEGES FOR ROLE postgres GRANT ALL ON TABLES TO heart_disease_dataset_user;


--
-- PostgreSQL database dump complete
--

\unrestrict Ob4bfEnY17oWT2S2DnqOLzBWPtm15qj9Q7cY60SaV1wzQMvMLnuK8XpkwcsAfDr

