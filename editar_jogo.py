from flask import flash
from projeto_final import banco
from projeto_final.models import Jogos

class Editar_jogo():

    @staticmethod
    def editar_capa(id, nvCapaJogo):
        fCapa = str(nvCapaJogo).strip()
        if fCapa != '':
            capaDoJogo = "static/imagens/{}".format(nvCapaJogo)
            jogo = Jogos.query.get_or_404(id)
            jogo.capaJogo = capaDoJogo
            banco.session.commit()

            return 'Atualizado'

    @staticmethod
    def editar_nome(id, nvNomeJogo):
        fNome = str(nvNomeJogo).strip()
        if fNome != '':
            jogo = Jogos.query.get_or_404(id)
            jogo.nomeJogo = nvNomeJogo
            banco.session.commit()

            return 'Atualizado'

    @staticmethod
    def editar_preco(id, nvPreco):
        fPreco = str(nvPreco).strip()
        if fPreco != '':
            try:
                preco = float(fPreco)

                if preco >= 0:
                    jogo = Jogos.query.get_or_404(id)
                    jogo.preco = preco
                    banco.session.commit()

                    return 'Atualizado'

                else:
                    flash('Preço do jogo não pode ser negativo', 'alerta')

            except:
                flash('Digite o preço como float, exemplo (100.99)', 'alerta')

    @staticmethod
    def editar_plataforma(id, nvPlataforma):
        fPlataforma = str(nvPlataforma).strip()
        if fPlataforma != '':
            jogo = Jogos.query.get_or_404(id)
            jogo.plataforma = nvPlataforma
            banco.session.commit()

            return 'Atualizado'

    @staticmethod
    def editar_status(id, nvStatus):
        fStatus = str(nvStatus).strip()
        if fStatus != '':
            jogo = Jogos.query.get_or_404(id)
            jogo.status = nvStatus
            banco.session.commit()

            return 'Atualizado'

