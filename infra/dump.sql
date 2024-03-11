--
-- PostgreSQL database dump
--

-- Dumped from database version 16.2 (Debian 16.2-1.pgdg120+2)
-- Dumped by pg_dump version 16.2 (Debian 16.2-1.pgdg120+2)

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

--
-- Name: userrole; Type: TYPE; Schema: public; Owner: postgres
--

CREATE TYPE public.userrole AS ENUM (
    'teacher',
    'candidate'
);


ALTER TYPE public.userrole OWNER TO postgres;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO postgres;

--
-- Name: interview; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.interview (
    name character varying(100),
    id integer NOT NULL
);


ALTER TABLE public.interview OWNER TO postgres;

--
-- Name: interview_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.interview_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.interview_id_seq OWNER TO postgres;

--
-- Name: interview_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.interview_id_seq OWNED BY public.interview.id;


--
-- Name: interview_status; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.interview_status (
    interview_id integer NOT NULL,
    user_id integer NOT NULL,
    is_passed boolean NOT NULL,
    score double precision NOT NULL,
    id integer NOT NULL
);


ALTER TABLE public.interview_status OWNER TO postgres;

--
-- Name: interview_status_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.interview_status_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.interview_status_id_seq OWNER TO postgres;

--
-- Name: interview_status_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.interview_status_id_seq OWNED BY public.interview_status.id;


--
-- Name: interview_task_association; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.interview_task_association (
    interview_id integer,
    task_id integer
);


ALTER TABLE public.interview_task_association OWNER TO postgres;

--
-- Name: task; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.task (
    name character varying(100),
    content character varying(1000),
    id integer NOT NULL
);


ALTER TABLE public.task OWNER TO postgres;

--
-- Name: task_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.task_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.task_id_seq OWNER TO postgres;

--
-- Name: task_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.task_id_seq OWNED BY public.task.id;


--
-- Name: user; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."user" (
    full_name character varying(50) NOT NULL,
    role public.userrole NOT NULL,
    id integer NOT NULL
);


ALTER TABLE public."user" OWNER TO postgres;

--
-- Name: user_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.user_id_seq OWNER TO postgres;

--
-- Name: user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.user_id_seq OWNED BY public."user".id;


--
-- Name: interview id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.interview ALTER COLUMN id SET DEFAULT nextval('public.interview_id_seq'::regclass);


--
-- Name: interview_status id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.interview_status ALTER COLUMN id SET DEFAULT nextval('public.interview_status_id_seq'::regclass);


--
-- Name: task id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.task ALTER COLUMN id SET DEFAULT nextval('public.task_id_seq'::regclass);


--
-- Name: user id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."user" ALTER COLUMN id SET DEFAULT nextval('public.user_id_seq'::regclass);


--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.alembic_version (version_num) FROM stdin;
95f7b3bce95a
\.


--
-- Data for Name: interview; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.interview (name, id) FROM stdin;
Python Developer	2
\.


--
-- Data for Name: interview_status; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.interview_status (interview_id, user_id, is_passed, score, id) FROM stdin;
\.


--
-- Data for Name: interview_task_association; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.interview_task_association (interview_id, task_id) FROM stdin;
2	4
2	5
2	6
2	7
2	8
2	8
2	9
2	10
2	11
2	12
2	13
\.


--
-- Data for Name: task; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.task (name, content, id) FROM stdin;
Python language	Could you tell me about the Python programming language? What is its type and typing system? Where is this language used, and when would you choose Python over C++?	4
Data structures in Python	Could you tell me about data structures in Python? What structures are present in this language, and could you classify them into two groups?	5
Hash table	What is a hash table? Is this structure used in Python? Could you please explain how it works in detail?	6
GIL	What is a GIL. Why GIL present in python.	7
Multithreading, multiprocessing, concurrency.	What are objects? Where, when, and how will you use each of them?	8
Solve task with un mutable and mutable structure	Example: structure = (1, 2, 3, [4, 5, 6]). a[0][0] = 10. a[0] = 10. a[3][0] = 10. 	9
SQL and NoSQL databases	You should explain what an SQL database is. What SQL databases do you know? What NoSQL databases do you know? What is the difference between SQL and NoSQL databases?	10
DB indexes	What are indexes do you know? Answer in detail.	11
Transactions in database.	What is it transaction and when you should use it?	12
Queries optimization	How do you optimize queries in a database?	13
\.


--
-- Data for Name: user; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."user" (full_name, role, id) FROM stdin;
\.


--
-- Name: interview_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.interview_id_seq', 2, true);


--
-- Name: interview_status_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.interview_status_id_seq', 8, true);


--
-- Name: task_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.task_id_seq', 13, true);


--
-- Name: user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.user_id_seq', 8, true);


--
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- Name: interview interview_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.interview
    ADD CONSTRAINT interview_pkey PRIMARY KEY (id);


--
-- Name: interview_status interview_status_interview_id_user_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.interview_status
    ADD CONSTRAINT interview_status_interview_id_user_id_key UNIQUE (interview_id, user_id);


--
-- Name: interview_status interview_status_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.interview_status
    ADD CONSTRAINT interview_status_pkey PRIMARY KEY (id);


--
-- Name: task task_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.task
    ADD CONSTRAINT task_pkey PRIMARY KEY (id);


--
-- Name: user user_full_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_full_name_key UNIQUE (full_name);


--
-- Name: user user_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_pkey PRIMARY KEY (id);


--
-- Name: interview_status interview_status_interview_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.interview_status
    ADD CONSTRAINT interview_status_interview_id_fkey FOREIGN KEY (interview_id) REFERENCES public.interview(id);


--
-- Name: interview_status interview_status_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.interview_status
    ADD CONSTRAINT interview_status_user_id_fkey FOREIGN KEY (user_id) REFERENCES public."user"(id);


--
-- Name: interview_task_association interview_task_association_interview_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.interview_task_association
    ADD CONSTRAINT interview_task_association_interview_id_fkey FOREIGN KEY (interview_id) REFERENCES public.interview(id);


--
-- Name: interview_task_association interview_task_association_task_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.interview_task_association
    ADD CONSTRAINT interview_task_association_task_id_fkey FOREIGN KEY (task_id) REFERENCES public.task(id);


--
-- PostgreSQL database dump complete
--

