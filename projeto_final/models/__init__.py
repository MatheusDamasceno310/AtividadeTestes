from projeto_final import banco, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_login(id_login):
    return Conta.query.get(int(id_login))

class Conta(banco.Model, UserMixin):
    id = banco.Column(banco.Integer, primary_key=True)
    usuario = banco.Column(banco.String, nullable=False, unique=True)
    email = banco.Column(banco.String, nullable=False, unique=True)
    telefone = banco.Column(banco.String, nullable=False)
    senha = banco.Column(banco.String, nullable=False)

class Recado(banco.Model):
    idRecado = banco.Column(banco.Integer, primary_key=True)
    nomeCompleto = banco.Column(banco.String, nullable=False)
    emailRecado = banco.Column(banco.String, nullable=False)
    menssagem = banco.Column(banco.String, nullable=False)

class Jogos(banco.Model):
    idCadJg = banco.Column(banco.Integer, primary_key=True)
    capaJogo = banco.Column(banco.String, nullable=False, unique=True)
    nomeJogo = banco.Column(banco.String, nullable=False)
    plataforma = banco.Column(banco.String, nullable=False)
    preco = banco.Column(banco.String, nullable=False)
    status = banco.Column(banco.String, nullable=False)

class Compras(banco.Model):
    idCompra = banco.Column(banco.Integer, primary_key=True)
    comprador = banco.Column(banco.String, nullable=False)
    jogo = banco.Column(banco.String, nullable=False)
    preco = banco.Column(banco.String, nullable=False)
    data = banco.Column(banco.String, nullable=False)




