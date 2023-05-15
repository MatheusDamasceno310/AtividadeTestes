from flask import render_template, url_for, redirect, flash
from projeto_final.forms import FormLogin, FormCadastro, FormRecado, FormCadJg, FormEditJg
from projeto_final import app, banco, bcrypt
from projeto_final.models import Conta, Recado, Jogos, Compras
from flask_login import login_required, logout_user, login_user, current_user
from datetime import datetime
import os
from editar_jogo import Editar_jogo
from cadastrar_jogo import Cadastrar_jogo

usuario = 'admsupremo'
senha = 'senhafraca'

@app.route("/", methods=['GET', 'POST'])
def login():
    formLogin = FormLogin()
    if formLogin.validate_on_submit():
            user = Conta.query.filter_by(usuario=formLogin.usuario.data).first()
            if user:
                if bcrypt.check_password_hash(user.senha, formLogin.senha.data):
                    login_user(user)
                    flash('Login feito com sucesso', 'sucesso')
                    return redirect(url_for('gamezone'))

                else:
                    flash('Senha incorreta', 'alerta')

            else:
                flash('Usuário não cadastrado', 'alerta')

            return redirect(url_for('login'))

    return render_template('login.html', formLogin=formLogin)

@app.route("/cadastro", methods=['GET', 'POST'])
def cadastro():
    formCadastro = FormCadastro()
    if formCadastro.validate_on_submit():
        user = Conta.query.filter_by(usuario=formCadastro.usuario.data).first()
        email = Conta.query.filter_by(email=formCadastro.email.data).first()

        try:
            fUsuario = str(formCadastro.usuario.data).strip()
            fEmail = str(formCadastro.email.data).strip()
            fTelefone = str(formCadastro.telefone.data).strip()
            fSenha = str(formCadastro.senha.data).strip()

            if fUsuario != '' and fEmail != '' and fTelefone != '' and fSenha != '':
                if formCadastro.senha.data == formCadastro.confirmarSenha.data:
                    if formCadastro.email.data[-10:] == '@gmail.com':
                        if not user:
                            if not email:
                                criptoSenha = bcrypt.generate_password_hash(formCadastro.senha.data)
                                user = Conta(usuario=formCadastro.usuario.data, email=formCadastro.email.data, telefone=formCadastro.telefone.data, senha=criptoSenha)
                                banco.session.add(user)
                                banco.session.commit()
                                flash('Usuário cadastrado com sucesso', 'sucesso')
                                return redirect(url_for('login'))

                            else:
                                flash('Email já existente', 'alerta')

                        else:
                            flash('Usuário já existente', 'alerta')

                    else:
                        flash("Tá faltando '@gmail.com' no email", 'alerta')

                else:
                    flash('Senhas não correspondentes', 'alerta')

            else:
                flash('Preencha todos os campos', 'alerta')

        except:
            flash('Houve um erro ao fazer o cadastro', 'alerta')

        return redirect(url_for('cadastro'))

    return render_template("cadastro.html", formCadastro=formCadastro)

@app.route("/gamezone", methods=['GET', 'POST'])
@login_required
def gamezone():
    formRecado = FormRecado()
    listaJogos = Jogos.query.all()
    if formRecado.validate_on_submit():
        try:
            fNome = formRecado.nomeCompleto.data
            fEmail = formRecado.emailRecado.data
            fMsg = formRecado.menssagem.data

            if fNome.strip() != '' and fEmail.strip() != '' and fMsg.strip() != '':
                if formRecado.emailRecado.data[-10:] == '@gmail.com':
                    msg = Recado(nomeCompleto=formRecado.nomeCompleto.data, emailRecado=formRecado.emailRecado.data, menssagem=formRecado.menssagem.data)
                    banco.session.add(msg)
                    banco.session.commit()

                    flash('Menssagem enviada com sucesso', 'sucesso')

                else:
                    flash("Tá faltando '@gmail.com' no email", 'alerta')

            else:
                flash('Preencha todos os campos', 'alerta')

        except:
            flash('Não foi possível enviar a menssagem', 'alerta')

        return redirect(url_for('gamezone'))

    return render_template('tela_main.html', formRecado=formRecado, listaJogos=listaJogos)

@app.route('/usuarios')
@login_required
def usuarios():
    if current_user.usuario == usuario:
        users = Conta.query.all()
        return render_template('excluir_usuarios.html', usuarios=users)

    else:
        logout_user()
        flash('Acesso restrito', 'falha')
        return redirect(url_for('login'))

@app.route('/excluir_usuario/<int:id>', methods=['POST'])
@login_required
def excluir_usuario(id):
    if current_user.usuario == usuario:
        user = Conta.query.get_or_404(id)
        banco.session.delete(user)
        banco.session.commit()
        return redirect(url_for('usuarios'))

    else:
        flash('Acesso restrito', 'falha')
        logout_user()
        return redirect(url_for('login'))

@app.route('/cadastrar_jogos', methods=['GET', 'POST'])
@login_required
def cadastrar_jogos():
    if current_user.usuario == usuario:
        formCadJg = FormCadJg()
        if formCadJg.validate_on_submit():
            try:

                fCapa = str(formCadJg.capaJogo.data)
                fNome = str(formCadJg.nomeJogo.data)
                fPlaraforma = str(formCadJg.plataforma.data)
                fPreco = str(formCadJg.preco.data)

                status = 'Disponivel'
                capaDoJogo = "static/imagens/{}".format(formCadJg.capaJogo.data)
                pasta = os.path.dirname(os.path.abspath(__file__))
                pasta = pasta.replace("\\routers", '')
                rotaCapa = "static\imagens\{}".format(formCadJg.capaJogo.data)
                caminhoFoto = os.path.join(pasta, rotaCapa)
                if os.path.exists(caminhoFoto):
                    if formCadJg.status.data:
                        status = 'Indisponivel'

                    if fCapa.strip() != '' and fNome.strip() != '' and fPlaraforma.strip() != '' and fPreco.strip() != '':
                        try:
                            precoJogo = float(formCadJg.preco.data)
                            if precoJogo >= 0:
                                Cadastrar_jogo.cadastrar_jogo(capaDoJogo, formCadJg.nomeJogo.data, formCadJg.plataforma.data, precoJogo, status)
                                return redirect(url_for('cadastrar_jogos'))

                            else:
                                flash('Valor do jogo não pode ser negativo', 'alerta')

                        except:
                            flash('Digite o preço como float, exemplo (100.99)', 'alerta')

                    else:
                        flash('Preencha todos os campos', 'alerta')

                else:
                    flash('Capa não está na pasta imagens da aplicação', 'alerta')

            except:
                flash('Houve um erro no cadastro', 'alerta')

            return redirect(url_for('cadastrar_jogos'))

        return render_template("cadastro_jogos.html", formCadJg=formCadJg)

    else:
        flash('Acesso restrito', 'falha')
        logout_user()
        return redirect(url_for('login'))

@app.route('/jogos_cadastrados', methods=['GET', 'POST'])
@login_required
def jogos_cadastrados():
    if current_user.usuario == usuario:
        formEditJg = FormEditJg()
        listaJogos = Jogos.query.all()
        if formEditJg.validate_on_submit():

            return redirect(url_for('jogos_cadastrados'))

        return render_template("editar_excluir.html", formEditJg=formEditJg, listaJogos=listaJogos)

    else:
        flash('Acesso restrito', 'falha')
        logout_user()
        return redirect(url_for('login'))

@app.route('/excluir_jogo/<int:id>', methods=['POST'])
@login_required
def excluir_jogo(id):
    if current_user.usuario == usuario:
        game = Jogos.query.get_or_404(id)
        banco.session.delete(game)
        banco.session.commit()
        return redirect(url_for('jogos_cadastrados'))

    else:
        flash('Acesso restrito', 'falha')
        logout_user()
        return redirect(url_for('login'))

@app.route('/editar_jogos/<int:id>', methods=['GET', 'POST'])
@login_required
def editar_jogos(id):
    if current_user.usuario == usuario:
        formEditJg = FormEditJg()
        if formEditJg.validate_on_submit():
            try:
                pasta = os.path.dirname(os.path.abspath(__file__))
                pasta = pasta.replace("\\routers", '')
                rotaCapa = "static\imagens\{}".format(formEditJg.nvCapa.data)
                caminhoFoto = os.path.join(pasta, rotaCapa)
                if os.path.exists(caminhoFoto):
                    capa = Editar_jogo.editar_capa(id, formEditJg.nvCapa.data)

                else:
                    flash('Capa não está na pasta imagens da aplicação', 'alerta')

                nome = Editar_jogo.editar_nome(id, formEditJg.nvNome.data)
                preco = Editar_jogo.editar_preco(id, formEditJg.nvPreco.data)
                plataforma = Editar_jogo.editar_plataforma(id, formEditJg.nvPlataforma.data)
                status = Editar_jogo.editar_status(id, formEditJg.nvStatus.data)


                if capa == 'Atualizado' or nome == 'Atualizado' or preco == 'Atualizado' or plataforma == 'Atualizado' or status == 'Atualizado':
                    flash('Houve atualização com sucesso', 'sucesso')

            except:
                flash('Houve um erro na alteração', 'alerta')

            return redirect(url_for('editar_jogos', id=id))

        return render_template("editar_jogo.html", formEditJg=formEditJg)

    else:
        flash('Acesso restrito', 'falha')
        logout_user()
        return redirect(url_for('login'))

@app.route('/comprar_jogo/<int:id>', methods=['POST'])
@login_required
def comprar_jogo(id):
    flash('Compra realizada com sucesso', 'sucesso')
    game = Jogos.query.get_or_404(id)
    data = datetime.now()
    comprador = current_user.usuario
    compra = Compras(comprador=comprador, jogo=game.nomeJogo, preco=game.preco, data=data)
    banco.session.add(compra)
    banco.session.commit()
    return redirect(url_for('gamezone'))

@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash('Logout bem sucedido', 'sucesso')
    return redirect(url_for('login'))