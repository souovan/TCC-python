import logging
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost/postgres'
app.debug = True
db = SQLAlchemy(app)

class users(db.Model):
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


@app.route('/test', methods=['GET'])
def test():
    return {
        'test': 'test1'
    }

# A simple test for the db connection
@app.route('/test_db_connection', methods=['GET'])
def test_db_test_db_connection():
    all_users = users.query.all()
    output = []
    for usuario in all_users:
        current_user = {}
        current_user['id_usuario'] = usuario.id_usuario
        current_user['fk_id_categoria_usuario'] = usuario.fk_id_categoria_usuario
        current_user['login'] = usuario.login
        current_user['senha'] = usuario.senha
        output.append(current_user)
    return jsonify(output)    

