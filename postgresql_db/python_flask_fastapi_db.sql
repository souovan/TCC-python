--
-- PostgreSQL database dump
--

-- Dumped from database version 12.9 (Ubuntu 12.9-0ubuntu0.20.04.1)
-- Dumped by pg_dump version 12.9 (Ubuntu 12.9-0ubuntu0.20.04.1)

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
-- Name: agendamento; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.agendamento (
    id_agendamento uuid NOT NULL,
    data_agendamento date,
    valor money,
    fk_id_usuario uuid,
    fk_id_vendedor uuid
);


ALTER TABLE public.agendamento OWNER TO postgres;

--
-- Name: categoria_cliente; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.categoria_cliente (
    id_categoria_cliente uuid NOT NULL,
    nome_categoria_cliente text
);


ALTER TABLE public.categoria_cliente OWNER TO postgres;

--
-- Name: categoria_fornecedor; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.categoria_fornecedor (
    id_categoria_fornecedor uuid NOT NULL,
    nome_categoria_fornecedor text
);


ALTER TABLE public.categoria_fornecedor OWNER TO postgres;

--
-- Name: categoria_produto; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.categoria_produto (
    id_categoria_produto uuid NOT NULL,
    nome_categoria_produto text
);


ALTER TABLE public.categoria_produto OWNER TO postgres;

--
-- Name: categoria_usuario; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.categoria_usuario (
    id_categoria_usuario uuid NOT NULL,
    nome_categoria_usuario text,
    fk_id_permissao_acesso uuid
);


ALTER TABLE public.categoria_usuario OWNER TO postgres;

--
-- Name: cliente; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.cliente (
    id_cliente uuid NOT NULL,
    nome text,
    razao_social text,
    cpf numeric,
    cnpj numeric,
    endereco text,
    numero_endereco numeric,
    complemento text,
    bairro text,
    cidade text,
    uf text,
    cep numeric,
    telefone numeric,
    celular numeric,
    email text,
    observacao text,
    fk_nome_categoria_cliente uuid
);


ALTER TABLE public.cliente OWNER TO postgres;

--
-- Name: compra; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.compra (
    id_compra uuid NOT NULL,
    fk_id_cotacao_compra uuid,
    fk_id_condicao_pagamento uuid
);


ALTER TABLE public.compra OWNER TO postgres;

--
-- Name: condicao_pagamento; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.condicao_pagamento (
    id_condicao_pagamento uuid NOT NULL,
    nome_condicao_pagamento text
);


ALTER TABLE public.condicao_pagamento OWNER TO postgres;

--
-- Name: cotacao_compra; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.cotacao_compra (
    id_cotacao_compra uuid NOT NULL,
    fk_id_fornecedor uuid,
    fk_id_usuario uuid,
    valor_total money,
    data_cotacao date
);


ALTER TABLE public.cotacao_compra OWNER TO postgres;

--
-- Name: estoque; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.estoque (
    id_estoque uuid NOT NULL,
    fk_id_produto uuid,
    quantidade_produto numeric
);


ALTER TABLE public.estoque OWNER TO postgres;

--
-- Name: fornecedor; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.fornecedor (
    id_fornecedor uuid NOT NULL,
    fk_id_categoria_fornecedor uuid,
    nome_fantasia text,
    razal_social text,
    telefone numeric,
    celular numeric,
    email text,
    endereco text,
    complemento text,
    bairro text,
    cidade text,
    uf text,
    cep numeric,
    observacao text
);


ALTER TABLE public.fornecedor OWNER TO postgres;

--
-- Name: item_orcamento; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.item_orcamento (
    id_item_orcamento uuid NOT NULL,
    fk_id_cotacao_compra uuid,
    fk_id_produto uuid
);


ALTER TABLE public.item_orcamento OWNER TO postgres;

--
-- Name: orcamento; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.orcamento (
    id_orcamento uuid NOT NULL,
    fk_id_cliente uuid,
    fk_id_usuario uuid,
    valor_total money,
    data_orcamento date
);


ALTER TABLE public.orcamento OWNER TO postgres;

--
-- Name: permissao_acesso; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.permissao_acesso (
    id_permissao_acesso uuid NOT NULL,
    nome_permissao text
);


ALTER TABLE public.permissao_acesso OWNER TO postgres;

--
-- Name: produto; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.produto (
    id_produto uuid NOT NULL,
    fk_id_categoria_produto uuid,
    codigo_barra numeric,
    nome_produto text,
    preco_custo money,
    preco_venda money,
    fk_quantidade_produto numeric
);


ALTER TABLE public.produto OWNER TO postgres;

--
-- Name: titulo_a_pagar; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.titulo_a_pagar (
    id_titulo_a_pagar uuid NOT NULL,
    fk_id_compra uuid,
    data_documento date,
    data_vencimento date,
    valor_titulo money,
    desconto money
);


ALTER TABLE public.titulo_a_pagar OWNER TO postgres;

--
-- Name: usuario; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.usuario (
    id_usuario uuid NOT NULL,
    fk_id_categoria_usuario uuid,
    login text,
    senha text
);


ALTER TABLE public.usuario OWNER TO postgres;

--
-- Name: venda; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.venda (
    id_venda uuid NOT NULL,
    fk_id_orcamento uuid,
    fk_id_condicao_pagamento uuid
);


ALTER TABLE public.venda OWNER TO postgres;

--
-- Name: vendedor; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.vendedor (
    id_vendedor uuid NOT NULL,
    nome_vendedor text,
    login text,
    senha text
);


ALTER TABLE public.vendedor OWNER TO postgres;

--
-- Data for Name: agendamento; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.agendamento (id_agendamento, data_agendamento, valor, fk_id_usuario, fk_id_vendedor) FROM stdin;
\.


--
-- Data for Name: categoria_cliente; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.categoria_cliente (id_categoria_cliente, nome_categoria_cliente) FROM stdin;
\.


--
-- Data for Name: categoria_fornecedor; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.categoria_fornecedor (id_categoria_fornecedor, nome_categoria_fornecedor) FROM stdin;
\.


--
-- Data for Name: categoria_produto; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.categoria_produto (id_categoria_produto, nome_categoria_produto) FROM stdin;
\.


--
-- Data for Name: categoria_usuario; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.categoria_usuario (id_categoria_usuario, nome_categoria_usuario, fk_id_permissao_acesso) FROM stdin;
a5d6035e-7851-4f59-a297-f2348a958b54	test	5fd772fe-3ad7-494c-93e7-4d5f7cf8bd3d
\.


--
-- Data for Name: cliente; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.cliente (id_cliente, nome, razao_social, cpf, cnpj, endereco, numero_endereco, complemento, bairro, cidade, uf, cep, telefone, celular, email, observacao, fk_nome_categoria_cliente) FROM stdin;
\.


--
-- Data for Name: compra; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.compra (id_compra, fk_id_cotacao_compra, fk_id_condicao_pagamento) FROM stdin;
\.


--
-- Data for Name: condicao_pagamento; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.condicao_pagamento (id_condicao_pagamento, nome_condicao_pagamento) FROM stdin;
\.


--
-- Data for Name: cotacao_compra; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.cotacao_compra (id_cotacao_compra, fk_id_fornecedor, fk_id_usuario, valor_total, data_cotacao) FROM stdin;
\.


--
-- Data for Name: estoque; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.estoque (id_estoque, fk_id_produto, quantidade_produto) FROM stdin;
\.


--
-- Data for Name: fornecedor; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.fornecedor (id_fornecedor, fk_id_categoria_fornecedor, nome_fantasia, razal_social, telefone, celular, email, endereco, complemento, bairro, cidade, uf, cep, observacao) FROM stdin;
\.


--
-- Data for Name: item_orcamento; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.item_orcamento (id_item_orcamento, fk_id_cotacao_compra, fk_id_produto) FROM stdin;
\.


--
-- Data for Name: orcamento; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.orcamento (id_orcamento, fk_id_cliente, fk_id_usuario, valor_total, data_orcamento) FROM stdin;
\.


--
-- Data for Name: permissao_acesso; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.permissao_acesso (id_permissao_acesso, nome_permissao) FROM stdin;
5fd772fe-3ad7-494c-93e7-4d5f7cf8bd3d	test
\.


--
-- Data for Name: produto; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.produto (id_produto, fk_id_categoria_produto, codigo_barra, nome_produto, preco_custo, preco_venda, fk_quantidade_produto) FROM stdin;
\.


--
-- Data for Name: titulo_a_pagar; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.titulo_a_pagar (id_titulo_a_pagar, fk_id_compra, data_documento, data_vencimento, valor_titulo, desconto) FROM stdin;
\.


--
-- Data for Name: usuario; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.usuario (id_usuario, fk_id_categoria_usuario, login, senha) FROM stdin;
919d64e6-c102-47b8-81e2-47d18fded04b	a5d6035e-7851-4f59-a297-f2348a958b54	test	test123
\.


--
-- Data for Name: venda; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.venda (id_venda, fk_id_orcamento, fk_id_condicao_pagamento) FROM stdin;
\.


--
-- Data for Name: vendedor; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.vendedor (id_vendedor, nome_vendedor, login, senha) FROM stdin;
\.


--
-- Name: agendamento agendamento_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.agendamento
    ADD CONSTRAINT agendamento_pkey PRIMARY KEY (id_agendamento);


--
-- Name: categoria_cliente categoria_cliente_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.categoria_cliente
    ADD CONSTRAINT categoria_cliente_pkey PRIMARY KEY (id_categoria_cliente);


--
-- Name: categoria_fornecedor categoria_fornecedor_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.categoria_fornecedor
    ADD CONSTRAINT categoria_fornecedor_pkey PRIMARY KEY (id_categoria_fornecedor);


--
-- Name: categoria_produto categoria_produto_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.categoria_produto
    ADD CONSTRAINT categoria_produto_pkey PRIMARY KEY (id_categoria_produto);


--
-- Name: categoria_usuario categoria_usuario_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.categoria_usuario
    ADD CONSTRAINT categoria_usuario_pkey PRIMARY KEY (id_categoria_usuario);


--
-- Name: cliente cliente_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cliente
    ADD CONSTRAINT cliente_pkey PRIMARY KEY (id_cliente);


--
-- Name: compra compra_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.compra
    ADD CONSTRAINT compra_pkey PRIMARY KEY (id_compra);


--
-- Name: condicao_pagamento condicao_pagamento_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.condicao_pagamento
    ADD CONSTRAINT condicao_pagamento_pkey PRIMARY KEY (id_condicao_pagamento);


--
-- Name: cotacao_compra cotacao_compra_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cotacao_compra
    ADD CONSTRAINT cotacao_compra_pkey PRIMARY KEY (id_cotacao_compra);


--
-- Name: estoque estoque_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.estoque
    ADD CONSTRAINT estoque_pkey PRIMARY KEY (id_estoque);


--
-- Name: fornecedor fornecedor_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fornecedor
    ADD CONSTRAINT fornecedor_pkey PRIMARY KEY (id_fornecedor);


--
-- Name: item_orcamento item_orcamento_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.item_orcamento
    ADD CONSTRAINT item_orcamento_pkey PRIMARY KEY (id_item_orcamento);


--
-- Name: categoria_cliente nome_categoria_cliente; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.categoria_cliente
    ADD CONSTRAINT nome_categoria_cliente UNIQUE (nome_categoria_cliente);


--
-- Name: categoria_produto nome_categoria_produto; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.categoria_produto
    ADD CONSTRAINT nome_categoria_produto UNIQUE (nome_categoria_produto);


--
-- Name: categoria_usuario nome_categoria_usuario; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.categoria_usuario
    ADD CONSTRAINT nome_categoria_usuario UNIQUE (nome_categoria_usuario);


--
-- Name: condicao_pagamento nome_condicao_pagamento; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.condicao_pagamento
    ADD CONSTRAINT nome_condicao_pagamento UNIQUE (nome_condicao_pagamento);


--
-- Name: permissao_acesso nome_permissao; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.permissao_acesso
    ADD CONSTRAINT nome_permissao UNIQUE (nome_permissao);


--
-- Name: orcamento orcamento_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.orcamento
    ADD CONSTRAINT orcamento_pkey PRIMARY KEY (id_orcamento);


--
-- Name: permissao_acesso permissao_acesso_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.permissao_acesso
    ADD CONSTRAINT permissao_acesso_pkey PRIMARY KEY (id_permissao_acesso);


--
-- Name: produto produto_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.produto
    ADD CONSTRAINT produto_pkey PRIMARY KEY (id_produto);


--
-- Name: estoque quantidade_produto; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.estoque
    ADD CONSTRAINT quantidade_produto UNIQUE (quantidade_produto);


--
-- Name: titulo_a_pagar titulo_a_pagar_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.titulo_a_pagar
    ADD CONSTRAINT titulo_a_pagar_pkey PRIMARY KEY (id_titulo_a_pagar);


--
-- Name: usuario usuario_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.usuario
    ADD CONSTRAINT usuario_pkey PRIMARY KEY (id_usuario);


--
-- Name: venda venda_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.venda
    ADD CONSTRAINT venda_pkey PRIMARY KEY (id_venda);


--
-- Name: vendedor vendedor_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.vendedor
    ADD CONSTRAINT vendedor_pkey PRIMARY KEY (id_vendedor);


--
-- Name: fornecedor fk_id_categoria_fornecedor; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fornecedor
    ADD CONSTRAINT fk_id_categoria_fornecedor FOREIGN KEY (fk_id_categoria_fornecedor) REFERENCES public.categoria_fornecedor(id_categoria_fornecedor) ON UPDATE CASCADE ON DELETE CASCADE NOT VALID;


--
-- Name: produto fk_id_categoria_produto; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.produto
    ADD CONSTRAINT fk_id_categoria_produto FOREIGN KEY (fk_id_categoria_produto) REFERENCES public.categoria_produto(id_categoria_produto) ON UPDATE CASCADE ON DELETE CASCADE NOT VALID;


--
-- Name: usuario fk_id_categoria_usuario; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.usuario
    ADD CONSTRAINT fk_id_categoria_usuario FOREIGN KEY (fk_id_categoria_usuario) REFERENCES public.categoria_usuario(id_categoria_usuario) ON UPDATE CASCADE ON DELETE CASCADE NOT VALID;


--
-- Name: orcamento fk_id_cliente; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.orcamento
    ADD CONSTRAINT fk_id_cliente FOREIGN KEY (fk_id_cliente) REFERENCES public.cliente(id_cliente) ON UPDATE CASCADE ON DELETE CASCADE NOT VALID;


--
-- Name: titulo_a_pagar fk_id_compra; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.titulo_a_pagar
    ADD CONSTRAINT fk_id_compra FOREIGN KEY (fk_id_compra) REFERENCES public.compra(id_compra) ON UPDATE CASCADE ON DELETE CASCADE NOT VALID;


--
-- Name: compra fk_id_condicao_pagamento; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.compra
    ADD CONSTRAINT fk_id_condicao_pagamento FOREIGN KEY (fk_id_condicao_pagamento) REFERENCES public.condicao_pagamento(id_condicao_pagamento) ON UPDATE CASCADE ON DELETE CASCADE NOT VALID;


--
-- Name: venda fk_id_condicao_pagamento; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.venda
    ADD CONSTRAINT fk_id_condicao_pagamento FOREIGN KEY (fk_id_condicao_pagamento) REFERENCES public.condicao_pagamento(id_condicao_pagamento) ON UPDATE CASCADE ON DELETE CASCADE NOT VALID;


--
-- Name: compra fk_id_cotacao_compra; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.compra
    ADD CONSTRAINT fk_id_cotacao_compra FOREIGN KEY (fk_id_cotacao_compra) REFERENCES public.cotacao_compra(id_cotacao_compra) ON UPDATE CASCADE ON DELETE CASCADE NOT VALID;


--
-- Name: item_orcamento fk_id_cotacao_compra; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.item_orcamento
    ADD CONSTRAINT fk_id_cotacao_compra FOREIGN KEY (fk_id_cotacao_compra) REFERENCES public.cotacao_compra(id_cotacao_compra) ON UPDATE CASCADE ON DELETE CASCADE NOT VALID;


--
-- Name: cotacao_compra fk_id_fornecedor; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cotacao_compra
    ADD CONSTRAINT fk_id_fornecedor FOREIGN KEY (fk_id_fornecedor) REFERENCES public.fornecedor(id_fornecedor) ON UPDATE CASCADE ON DELETE CASCADE NOT VALID;


--
-- Name: venda fk_id_orcamento; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.venda
    ADD CONSTRAINT fk_id_orcamento FOREIGN KEY (fk_id_orcamento) REFERENCES public.orcamento(id_orcamento) ON UPDATE CASCADE ON DELETE CASCADE NOT VALID;


--
-- Name: categoria_usuario fk_id_permissao_acesso; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.categoria_usuario
    ADD CONSTRAINT fk_id_permissao_acesso FOREIGN KEY (fk_id_permissao_acesso) REFERENCES public.permissao_acesso(id_permissao_acesso) ON UPDATE CASCADE ON DELETE CASCADE NOT VALID;


--
-- Name: item_orcamento fk_id_produto; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.item_orcamento
    ADD CONSTRAINT fk_id_produto FOREIGN KEY (fk_id_produto) REFERENCES public.produto(id_produto) ON UPDATE CASCADE ON DELETE CASCADE NOT VALID;


--
-- Name: estoque fk_id_produto; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.estoque
    ADD CONSTRAINT fk_id_produto FOREIGN KEY (fk_id_produto) REFERENCES public.produto(id_produto) ON UPDATE CASCADE ON DELETE CASCADE NOT VALID;


--
-- Name: cotacao_compra fk_id_usuario; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cotacao_compra
    ADD CONSTRAINT fk_id_usuario FOREIGN KEY (fk_id_usuario) REFERENCES public.usuario(id_usuario) ON UPDATE CASCADE ON DELETE CASCADE NOT VALID;


--
-- Name: orcamento fk_id_usuario; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.orcamento
    ADD CONSTRAINT fk_id_usuario FOREIGN KEY (fk_id_usuario) REFERENCES public.usuario(id_usuario) ON UPDATE CASCADE ON DELETE CASCADE NOT VALID;


--
-- Name: agendamento fk_id_usuario; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.agendamento
    ADD CONSTRAINT fk_id_usuario FOREIGN KEY (fk_id_usuario) REFERENCES public.usuario(id_usuario) ON UPDATE CASCADE ON DELETE CASCADE NOT VALID;


--
-- Name: agendamento fk_id_vendedor; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.agendamento
    ADD CONSTRAINT fk_id_vendedor FOREIGN KEY (fk_id_vendedor) REFERENCES public.vendedor(id_vendedor) ON UPDATE CASCADE ON DELETE CASCADE NOT VALID;


--
-- Name: cliente fk_nome_categoria_cliente; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cliente
    ADD CONSTRAINT fk_nome_categoria_cliente FOREIGN KEY (fk_nome_categoria_cliente) REFERENCES public.categoria_cliente(id_categoria_cliente) ON UPDATE CASCADE ON DELETE CASCADE NOT VALID;


--
-- Name: produto fk_quantidade_produto; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.produto
    ADD CONSTRAINT fk_quantidade_produto FOREIGN KEY (fk_quantidade_produto) REFERENCES public.estoque(quantidade_produto) ON UPDATE CASCADE ON DELETE CASCADE NOT VALID;


--
-- PostgreSQL database dump complete
--

