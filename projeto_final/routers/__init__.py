from flask import render_template, url_for, redirect, flash
from projeto_final.forms import FormLogin, FormCadastro, FormRecado, FormCadJg
from projeto_final import app, banco, bcrypt
from projeto_final.models import Conta, Recado, Jogos, Compras
from flask_login import login_required, logout_user, login_user, current_user
from datetime import datetime

usuario = 'admsupremo'
senha = 'senhafraca'

@app.route("/", methods=['GET', 'POST'])
def login():
    formLogin = FormLogin()
    if formLogin.validate_on_submit():
            user = Conta.query.filter_by(usuario=formLogin.usuario.data).first()
            if formLogin.usuario.data == usuario and formLogin.senha.data == senha:
                login_user(user)
                return redirect(url_for('gamezone'))

            else:
                if user and bcrypt.check_password_hash(user.senha, formLogin.senha.data):
                    login_user(user)
                    flash('Login feito com sucesso', 'sucesso')
                    return redirect(url_for('gamezone'))

                else:
                    flash('Usuário ou senha incorreto', 'alerta')
                    return redirect(url_for('login'))

    return render_template('login.html', formLogin=formLogin)

@app.route("/cadastro", methods=['GET', 'POST'])
def cadastro():
    formCadastro = FormCadastro()
    if formCadastro.validate_on_submit():
        try:
            if formCadastro.senha.data == formCadastro.confirmarSenha.data:
                criptoSenha = bcrypt.generate_password_hash(formCadastro.senha.data)
                user = Conta(usuario=formCadastro.usuario.data, email=formCadastro.email.data, telefone=formCadastro.telefone.data, senha=criptoSenha)
                banco.session.add(user)
                banco.session.commit()
                flash('Usuário cadastrado com sucesso', 'sucesso')
                return redirect(url_for('login'))

            else:
                flash('Usuário ou e-mail já existente', 'alerta')

        except:
            flash('Houve um erro no cadastro', 'alerta')

        return redirect(url_for('cadastro'))

    return render_template("cadastro.html", formCadastro=formCadastro)

@app.route("/gamezone", methods=['GET', 'POST'])
@login_required
def gamezone():
    formRecado = FormRecado()
    listaJogos = Jogos.query.all()
    if formRecado.validate_on_submit():
        try:
            msg = Recado(nomeCompleto=formRecado.nomeCompleto.data, emailRecado=formRecado.emailRecado.data, menssagem=formRecado.menssagem.data)
            banco.session.add(msg)
            banco.session.commit()

            flash('Menssagem enviada com sucesso', 'sucesso')
            return redirect(url_for('gamezone'))

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
        logout_user()
        flash('Acesso restrito', 'falha')
        return redirect(url_for('login'))

@app.route('/cadastrar_jogos', methods=['GET', 'POST'])
@login_required
def cadastrar_jogos():
    if current_user.usuario == usuario:
        formCadJg = FormCadJg()
        if formCadJg.validate_on_submit():
            try:
                status = 'Disponivel'
                CapaDoJogo = "static/imagens/{}".format(formCadJg.capaJogo.data)
                capaV = Jogos.query.filter_by(capaJogo=formCadJg.capaJogo.data).first()
                if capaV != formCadJg.capaJogo.data:
                    if formCadJg.status.data:
                        status = 'Indisponivel'

                    game = Jogos(capaJogo=CapaDoJogo, nomeJogo=formCadJg.nomeJogo.data, plataforma=formCadJg.plataforma.data, preco=formCadJg.preco.data, status=status)
                    banco.session.add(game)
                    banco.session.commit()
                    flash('Jogo cadastrado com sucesso', 'sucesso')
                    return redirect(url_for('cadastrar_jogos'))

                else:
                    flash('Essa capa já está sendo usada', 'alerta')

            except:
                flash('Houve um erro no cadastro', 'alerta')

            return redirect(url_for('cadastrar_jogos'))

        return render_template("cadastro_jogos.html", formCadJg=formCadJg)

    else:
        logout_user()
        flash('Acesso restrito', 'falha')
        return redirect(url_for('login'))

@app.route('/comprar_jogo/<int:id>', methods=['POST'])
@login_required
def comprar_jogo(id):
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