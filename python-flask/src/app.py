from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost/postgres'
app.debug = True
db = SQLAlchemy(app)

class user(db.Model):
    __tablename__ = 'usuario'
    id_usuario = db.Column(db.String(), primary_key=True)
    fk_id_categoria_usuario = db.Column(db.String(), nullable=False)
    login = db.Column(db.String(), nullable=False)
    senha = db.Column(db.String(), nullable=False)

    def __init__(self, id_usuario, fk_id_categoria_usuario, login, senha):
        self.id_usuario = id_usuario
        self.fk_id_categoria_usuario = fk_id_categoria_usuario
        self.login = login
        self.senha = senha

class scheduling(db.Model):
    __tablename__ = 'agendamento'
    id_agendamento = db.Column(db.String(), primary_key=True)
    fk_id_usuario = db.Column(db.String(), nullable=False)
    fk_id_vendedor = db.Column(db.String(), nullable=False)
    data_agendamento = db.Column(db.Date(), nullable=False)

    def __init__(self, id_agendamento, fk_id_usuario, fk_id_vendedor, data_agendamento):
        self.id_agendamento = id_agendamento
        self.fk_id_usuario = fk_id_usuario
        self.fk_id_vendedor = fk_id_vendedor
        self.data_agendamento = data_agendamento

class client_category(db.Model):
    __tablename__ = 'categoria_cliente'
    id_categoria_cliente = db.Column(db.String(), primary_key=True)
    nome_categoria_cliente = db.Column(db.String(), nullable=False)

    def __init__(self, id_categoria_cliente, nome_categoria_cliente):
        self.id_categoria_cliente = id_categoria_cliente
        self.nome_categoria_cliente = nome_categoria_cliente

class provider_category(db.Model):
    __tablename__ = 'categoria_fornecedor'
    id_categoria_fornecedor = db.Column(db.String(), primary_key=True)
    nome_categoria_fornecedor = db.Column(db.String(), nullable=False)

    def __init__(self, id_categoria_fornecedor, nome_categoria_fornecedor):
        self.id_categoria_fornecedor = id_categoria_fornecedor
        self.nome_categoria_fornecedor = nome_categoria_fornecedor

class product_category(db.Model):
    __tablename__ = 'categoria_produto'
    id_categoria_produto = db.Column(db.String(), primary_key=True)
    nome_categoria_produto = db.Column(db.String(), nullable=False)

    def __init__(self, id_categoria_produto, nome_categoria_produto):
        self.id_categoria_produto = id_categoria_produto
        self.nome_categoria_produto = nome_categoria_produto

class user_category(db.Model):
    __tablename__ = 'categoria_usuario'
    id_categoria_usuario = db.Column(db.String(), primary_key=True)
    nome_categoria_usuario = db.Column(db.String(), nullable=False)
    fk_id_permissao_acesso = db.Column(db.String(), nullable=False)

    def __init__(self, id_categoria_usuario, nome_categoria_usuario, fk_id_permissao_acesso):
        self.id_categoria_usuario = id_categoria_usuario
        self.nome_categoria_usuario = nome_categoria_usuario
        self.fk_id_permissao_acesso = fk_id_permissao_acesso

class client(db.Model):
    __tablename__ = 'cliente'
    id_cliente = db.Column(db.String(), primary_key=True)
    fk_nome_categoria_cliente = db.Column(db.String(), nullable=False)
    nome = db.Column(db.String(), nullable=False)
    razao_social = db.Column(db.String(), nullable=False)
    cpf = db.Column(db.String(), nullable=False)
    cnpj = db.Column(db.String(), nullable=False)
    endereco = db.Column(db.String(), nullable=False)
    numero_endereco = db.Column(db.String(), nullable=False)
    complemento = db.Column(db.String(), nullable=False)
    bairro = db.Column(db.String(), nullable=False)
    cidade = db.Column(db.String(), nullable=False)
    uf = db.Column(db.String(), nullable=False)
    cep = db.Column(db.String(), nullable=False)
    celular = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), nullable=False)
    observacao = db.Column(db.String(), nullable=False)

    def __init__(self, id_cliente, fk_nome_categoria_cliente, nome, razao_social, cpf, cnpj, endereco, numero_endereco, complemento, bairro, cidade, uf, cep, celular, email, observacao):
        self.id_cliente = id_cliente
        self.fk_nome_categoria_cliente = fk_nome_categoria_cliente
        self.razao_social = razao_social
        self.cpf = cpf
        self.cnpj = cnpj
        self.endereco = endereco
        self.numero_endereco = numero_endereco
        self.complemento = complemento
        self.bairro = bairro
        self.cidade = cidade
        self.uf = uf
        self.cep = cep
        self.celular = celular
        self.email = email
        self.observacao = observacao

class purchase(db.Model):
    __tablename__ = 'compra'
    id_compra = db.Column(db.String(), primary_key=True)
    fk_id_cotacao_compra = db.Column(db.String(), nullable=False)
    fk_id_condicao_pagamento = db.Column(db.String(), nullable=False)

    def __init__(self, id_compra, fk_id_cotacao_compra, fk_id_condicao_pagamento):
        self.id_compra = id_compra
        self.fk_id_cotacao_compra = fk_id_cotacao_compra
        self.fk_id_condicao_pagamento = fk_id_condicao_pagamento

class payment_terms(db.Model):
    __tablename__ = 'condicao_pagamento'
    id_condicao_pagamento = db.Column(db.String(), primary_key=True)
    nome_condicao_pagamento = db.Column(db.String(), nullable=False)

    def __init__(self, id_condicao_pagamento, nome_condicao_pagamento):
        self.id_condicao_pagamento = id_condicao_pagamento
        self.nome_condicao_pagamento = nome_condicao_pagamento

class purchase_quotation(db.Model):
    __tablename__ = 'cotacao_compra'
    id_cotacao_compra = db.Column(db.String(), primary_key=True)
    fk_id_fornecedor = db.Column(db.String(), nullable=False)
    fk_id_usuario = db.Column(db.String(), nullable=False)
    valor_total = db.Column(db.String(), nullable=False)
    data_cotacao = db.Column(db.Date(), nullable=False)

    def __init__(self, id_cotacao_compra, fk_id_fornecedor, fk_id_usuario, valor_total, data_cotacao):
        self.id_cotacao_compra = id_cotacao_compra
        self.fk_id_fornecedor = fk_id_fornecedor
        self.fk_id_usuario = fk_id_usuario
        self.valor_total = valor_total
        self.data_cotacao = data_cotacao

class inventory(db.Model):
    __tablename__ = 'estoque'
    id_estoque = db.Column(db.String(), primary_key=True)
    fk_id_produto = db.Column(db.String(), nullable=False)
    quantidade_produto = db.Column(db.String(), nullable=False)

    def __init__(self, id_estoque, fk_id_produto, quantidade_produto):
        self.id_estoque = id_estoque
        self.fk_id_produto = fk_id_produto
        self.quantidade_produto = quantidade_produto

class provider(db.Model):
    __tablename__ = 'fornecedor'
    id_fornecedor = db.Column(db.String(), primary_key=True)
    fk_id_categoria_fornecedor = db.Column(db.String(), nullable=False)
    nome_fantasia = db.Column(db.String(), nullable=False)
    razao_social = db.Column(db.String(), nullable=False)
    telefone = db.Column(db.String(), nullable=False)
    celular = db.Column(db.String(), nullable=False)
    cnpj = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), nullable=False)
    endereco = db.Column(db.String(), nullable=False)
    complemento = db.Column(db.String(), nullable=False)
    bairro = db.Column(db.String(), nullable=False)
    cidade = db.Column(db.String(), nullable=False)
    uf = db.Column(db.String(), nullable=False)
    cep = db.Column(db.String(), nullable=False)
    observacao = db.Column(db.String(), nullable=False)

    def __init__(self, id_fornecedor, fk_id_categoria_fornecedor, nome_fantasia, razao_social, telefone, celular, cpf, cnpj, email, endereco, complemento, bairro, cidade, uf, cep, observacao):
        self.id_fornecedor = id_fornecedor
        self.fk_id_categoria_fornecedor = fk_id_categoria_fornecedor
        self.nome_fantasia = nome_fantasia
        self.razao_social = razao_social
        self.telefone = telefone
        self.celular = celular
        self.cpf = cpf
        self.cnpj = cnpj
        self.email = email
        self.endereco = endereco
        self.complemento = complemento
        self.bairro = bairro
        self.cidade = cidade
        self.uf = uf
        self.cep = cep
        self.celular = celular
        self.email = email
        self.observacao = observacao

class budget_item(db.Model):
    __tablename__ = 'item_orcamento'
    id_item_orcamento = db.Column(db.String(), primary_key=True)
    fk_id_cotacao_compra = db.Column(db.String(), nullable=False)
    fk_id_produto = db.Column(db.String(), nullable=False)

    def __init__(self, id_item_orcamento, fk_id_cotacao_compra, fk_id_produto):
        self.id_item_orcamento = id_item_orcamento
        self.fk_id_cotacao_compra = fk_id_cotacao_compra
        self.fk_id_produto = fk_id_produto

class budget(db.Model):
    __tablename__ = 'orcamento'
    id_orcamento = db.Column(db.String(), primary_key=True)
    fk_id_cliente = db.Column(db.String(), nullable=False)
    fk_id_usuario = db.Column(db.String(), nullable=False)
    valor_total = db.Column(db.String(), nullable=False)
    data_orcamento = db.Column(db.String(), nullable=False)

    def __init__(self, id_orcamento, fk_id_cliente, fk_id_usuario, valor_total, data_orcamento):
        self.id_orcamento = id_orcamento
        self.fk_id_cliente = fk_id_cliente
        self.fk_id_usuario = fk_id_usuario
        self.valor_total = valor_total
        self.data_orcamento = data_orcamento

class access_permissions(db.Model):
    __tablename__ = 'permissao_acesso'
    id_permissao_acesso = db.Column(db.String(), primary_key=True)
    nome_permissao = db.Column(db.String(), nullable=False)

    def __init__(self, id_permissao_acesso, nome_permissao):
        self.id_permissao_acesso = id_permissao_acesso
        self.nome_permissao = nome_permissao

class product(db.Model):
    __tablename__ = 'produto'
    id_produto = db.Column(db.String(), primary_key=True)
    fk_id_categoria_produto = db.Column(db.String(), nullable=False)
    codigo_barra = db.Column(db.String(), nullable=False)
    nome_produto = db.Column(db.String(), nullable=False)
    preco_custo = db.Column(db.Date(), nullable=False)
    preco_venda = db.Column(db.Date(), nullable=False)
    fk_quantidade_produto = db.Column(db.Date(), nullable=False)

    def __init__(self, id_produto, fk_id_categoria_produto, codigo_barra, nome_produto, preco_custo, preco_venda, fk_quantidade_produto):
        self.id_produto = id_produto
        self.fk_id_categoria_produto = fk_id_categoria_produto
        self.codigo_barra = codigo_barra
        self.nome_produto = nome_produto
        self.preco_custo = preco_custo
        self.preco_venda = preco_venda
        self.fk_quantidade_produto = fk_quantidade_produto

class title_to_pay(db.Model):
    __tablename__ = 'titulo_a_pagar'
    id_titulo_a_pagar = db.Column(db.String(), primary_key=True)
    fk_id_compra = db.Column(db.String(), nullable=False)
    data_documento = db.Column(db.String(), nullable=False)
    data_vencimento = db.Column(db.String(), nullable=False)
    valor_titulo = db.Column(db.Date(), nullable=False)
    desconto = db.Column(db.Date(), nullable=False)

    def __init__(self, id_titulo_a_pagar, fk_id_compra, data_documento, data_vencimento, valor_titulo, desconto):
        self.id_titulo_a_pagar = id_titulo_a_pagar
        self.fk_id_compra = fk_id_compra
        self.data_documento = data_documento
        self.data_vencimento = data_vencimento
        self.valor_titulo = valor_titulo
        self.desconto = desconto

class sale(db.Model):
    __tablename__ = 'venda'
    id_venda = db.Column(db.String(), primary_key=True)
    fk_id_orcamento = db.Column(db.String(), nullable=False)
    fk_id_condicao_pagamento = db.Column(db.String(), nullable=False)

    def __init__(self, id_venda, fk_id_orcamento, fk_id_condicao_pagamento):
        self.id_venda = id_venda
        self.fk_id_orcamento = fk_id_orcamento
        self.fk_id_condicao_pagamento = fk_id_condicao_pagamento

class seller(db.Model):
    __tablename__ = 'vendedor'
    id_vendedor = db.Column(db.String(), primary_key=True)
    nome_vendedor = db.Column(db.String(), nullable=False)
    login = db.Column(db.String(), nullable=False)
    senha = db.Column(db.String(), nullable=False)

    def __init__(self, id_vendedor, nome_vendedor, login, senha):
        self.id_vendedor = id_vendedor
        self.nome_vendedor = nome_vendedor
        self.login = login
        self.senha = senha

@app.route('/test', methods=['GET'])
def test():
    return {
        'test': 'test1'
    }, 200

# A simple test for the db connection
@app.route('/test_db_connection', methods=['GET'])
def test_db_test_db_connection():
    all_user = user.query.all()
    output = []
    for usuario in all_user:
        current_user = {}
        current_user['id_usuario'] = usuario.id_usuario
        current_user['fk_id_categoria_usuario'] = usuario.fk_id_categoria_usuario
        current_user['login'] = usuario.login
        current_user['senha'] = usuario.senha
        output.append(current_user)
    return jsonify(output), 200

