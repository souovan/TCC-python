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
    nome_categoria_cliente = db.Column(db.Text(), nullable=False)

    def __init__(self, id_categoria_cliente, nome_categoria_cliente):
        self.id_categoria_cliente = id_categoria_cliente
        self.nome_categoria_cliente = nome_categoria_cliente

class provider_category(db.Model):
    __tablename__ = 'categoria_fornecedor'
    id_categoria_fornecedor = db.Column(db.String(), primary_key=True)
    nome_categoria_fornecedor = db.Column(db.Text(), nullable=False)

    def __init__(self, id_categoria_fornecedor, nome_categoria_fornecedor):
        self.id_categoria_fornecedor = id_categoria_fornecedor
        self.nome_categoria_fornecedor = nome_categoria_fornecedor

class product_category(db.Model):
    __tablename__ = 'categoria_produto'
    id_categoria_produto = db.Column(db.String(), primary_key=True)
    nome_categoria_produto = db.Column(db.Text(), nullable=False)

    def __init__(self, id_categoria_produto, nome_categoria_produto):
        self.id_categoria_produto = id_categoria_produto
        self.nome_categoria_produto = nome_categoria_produto

class user_category(db.Model):
    __tablename__ = 'categoria_usuario'
    id_categoria_usuario = db.Column(db.String(), primary_key=True)
    nome_categoria_usuario = db.Column(db.Text(), nullable=False)
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
    observacao = db.Column(db.Text(), nullable=False)

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
    nome_condicao_pagamento = db.Column(db.Text(), nullable=False)

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
    quantidade_produto = db.Column(db.Integer(), nullable=False)

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
    email = db.Column(db.String(), nullable=False)
    endereco = db.Column(db.String(), nullable=False)
    complemento = db.Column(db.String(), nullable=False)
    bairro = db.Column(db.String(), nullable=False)
    cidade = db.Column(db.String(), nullable=False)
    uf = db.Column(db.String(), nullable=False)
    cep = db.Column(db.String(), nullable=False)
    observacao = db.Column(db.Text(), nullable=False)

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
    nome_permissao = db.Column(db.Text(), nullable=False)

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

# @app.route('/test', methods=['GET'])
# def test():
#     return {
#         'test': 'test1'
#     }, 200

@app.route('/usuarios', methods=['GET'])
def all_users():
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

@app.route('/usuario/<id>', methods=['GET'])
def show_user(id):
    usuario = user.query.get(id)
    return jsonify([{
        'id_usuario': usuario.id_usuario,
        'fk_id_categoria_usuario': usuario.fk_id_categoria_usuario,
        'login': usuario.login,
        'senha': usuario.senha
    }]), 200

@app.route('/agendamentos', methods=['GET'])
def all_scheduling():
    all_scheduling = scheduling.query.all()
    output = []
    for agendamento in all_scheduling:
        current_scheduling = {}
        current_scheduling['id_agendamento'] = agendamento.id_agendamento
        current_scheduling['fk_id_usuario'] = agendamento.fk_id_usuario
        current_scheduling['fk_id_vendedor'] = agendamento.fk_id_vendedor
        current_scheduling['data_agendamento'] = agendamento.data_agendamento
        output.append(current_scheduling)
    return jsonify(output), 200

@app.route('/clientes', methods=['GET'])
def all_clients():
    all_clients = client.query.all()
    output = []
    for clientes in all_clients:
        current_clients = {}
        current_clients['id_cliente'] = clientes.id_cliente
        current_clients['fk_nome_categoria_cliente'] = clientes.fk_nome_categoria_cliente
        current_clients['nome'] = clientes.nome
        current_clients['razao_social'] = clientes.razao_social
        current_clients['cpf'] = clientes.cpf
        current_clients['cnpj'] = clientes.cnpj
        current_clients['endereco'] = clientes.endereco
        current_clients['numero_endereco'] = clientes.numero_endereco
        current_clients['complemento'] = clientes.complemento
        current_clients['bairro'] = clientes.bairro
        current_clients['cidade'] = clientes.cidade
        current_clients['uf'] = clientes.uf
        current_clients['cep'] = clientes.cep
        current_clients['celular'] = clientes.celular
        current_clients['email'] = clientes.email
        current_clients['observacao'] = clientes.observacao

        output.append(current_clients)
    return jsonify(output), 200

@app.route('/compras', methods=['GET'])
def all_purchase():
    all_purchases = purchase.query.all()
    output = []
    for compras in all_purchases:
        current_purchase = {}
        current_purchase['id_compra'] = compras.id_compra
        current_purchase['fk_id_cotacao_compra'] = compras.fk_id_cotacao_compra
        current_purchase['fk_id_condicao_pagamento'] = compras.fk_id_condicao_pagamento
        output.append(current_purchase)
    return jsonify(output), 200

@app.route('/estoque', methods=['GET'])
def all_inventory():
    all_inventory = inventory.query.all()
    output = []
    for estoques in all_inventory:
        current_inventory = {}
        current_inventory['id_estoque'] = estoques.id_estoque
        current_inventory['fk_id_produto'] = estoques.fk_id_produto
        current_inventory['quantidade_produto'] = estoques.quantidade_produto
        output.append(current_inventory)
    return jsonify(output), 200

@app.route('/fornecedores', methods=['GET'])
def all_providers():
    all_providers = provider.query.all()
    output = []
    for fornecedores in all_providers:
        current_providers = {}
        current_providers['id_fornecedor'] = fornecedores.id_fornecedor
        current_providers['fk_id_categoria_fornecedor'] = fornecedores.fk_id_categoria_fornecedor
        current_providers['razao_social'] = fornecedores.razao_social
        current_providers['telefone'] = fornecedores.telefone
        current_providers['celular'] = fornecedores.celular
        current_providers['email'] = fornecedores.email
        current_providers['endereco'] = fornecedores.endereco
        current_providers['complemento'] = fornecedores.complemento
        current_providers['bairro'] = fornecedores.bairro
        current_providers['cidade'] = fornecedores.cidade
        current_providers['uf'] = fornecedores.uf
        current_providers['cep'] = fornecedores.cep
        current_providers['observacao'] = fornecedores.observacao
        output.append(current_providers)
    return jsonify(output), 200

@app.route('/orcamentos', methods=['GET'])
def all_budgets():
    all_budgets = budget.query.all()
    output = []
    for orcamentos in all_budgets:
        current_budgets = {}
        current_budgets['id_item_orcamento'] = orcamentos.id_item_orcamento
        current_budgets['fk_id_cotacao_compra'] = orcamentos.fk_id_cotacao_compra
        current_budgets['fk_id_produto'] = orcamentos.fk_id_produto
        output.append(current_budgets)
    return jsonify(output), 200

@app.route('/produtos', methods=['GET'])
def all_products():
    all_products = product.query.all()
    output = []
    for products in all_products:
        current_products = {}
        current_products['id_produto'] = products.id_produto
        current_products['fk_id_categoria_produto'] = products.fk_id_categoria_produto
        current_products['codigo_barra'] = products.codigo_barra
        current_products['nome_produto'] = products.nome_produto
        current_products['preco_custo'] = products.preco_custo
        current_products['preco_venda'] = products.preco_venda
        current_products['fk_quantidade_produto'] = products.fk_quantidade_produto
        output.append(current_products)
    return jsonify(output), 200

@app.route('/titulos_a_pagar', methods=['GET'])
def all_title_to_pay():
    all_title_to_pay = title_to_pay.query.all()
    output = []
    for titles_to_pay in all_title_to_pay:
        current_title_to_pay = {}
        current_title_to_pay['fk_id_compra'] = titles_to_pay.fk_id_compra
        current_title_to_pay['data_documento'] = titles_to_pay.data_documento
        current_title_to_pay['data_vencimento'] = titles_to_pay.data_vencimento
        current_title_to_pay['valor_titulo'] = titles_to_pay.valor_titulo
        current_title_to_pay['desconto'] = titles_to_pay.desconto
        output.append(current_title_to_pay)
    return jsonify(output), 200

@app.route('/vendas', methods=['GET'])
def all_sales():
    all_sales = sale.query.all()
    output = []
    for sales in all_sales:
        current_sales = {}
        current_sales['id_venda'] = sales.id_venda
        current_sales['fk_id_orcamento'] = sales.fk_id_orcamento
        current_sales['fk_id_condicao_pagamento'] = sales.fk_id_condicao_pagamento
        output.append(current_sales)
    return jsonify(output), 200

@app.route('/vendedores', methods=['GET'])
def all_sellers():
    all_sellers = seller.query.all()
    output = []
    for sellers in all_sellers:
        current_sellers = {}
        current_sellers['id_vendedor'] = sellers.id_vendedor
        current_sellers['nome_vendedor'] = sellers.nome_vendedor
        current_sellers['login'] = sellers.login
        current_sellers['senha'] = sellers.senha
        output.append(current_sellers)
    return jsonify(output), 200