from flask import flash
from projeto_final import banco
from projeto_final.models import Jogos
class Cadastrar_jogo():

    @staticmethod
    def cadastrar_jogo(capa, nome, plataforma, preco, status):
        game = Jogos(capaJogo=capa, nomeJogo=nome, plataforma=plataforma, preco=preco, status=status)
        banco.session.add(game)
        banco.session.commit()
        flash('Jogo cadastrado com sucesso', 'sucesso')