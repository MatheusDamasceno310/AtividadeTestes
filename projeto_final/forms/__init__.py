from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, FileField
from wtforms.validators import DataRequired, length, email

class FormLogin(FlaskForm):
    usuario = StringField('Usuário', validators=[DataRequired(), length(6)])
    senha = PasswordField('Senha',  validators=[DataRequired(), length(8, 30)])
    btn_entrar = SubmitField('Entrar')

class FormCadastro(FlaskForm):
    usuario = StringField('Usuário', validators=[DataRequired(), length(6)])
    email = StringField('E-mail', validators=[DataRequired()])
    telefone = StringField('Telefone', validators=[DataRequired(), length(9, 20)])
    senha = PasswordField('Senha',  validators=[DataRequired(), length(8, 30)])
    confirmarSenha = PasswordField('Confirmar Senha', validators=[DataRequired(), length(8, 30)])
    btn_cadastrar_usuario = SubmitField('Cadastrar')

class FormRecado(FlaskForm):
    nomeCompleto = StringField('Nome Completo', validators=[DataRequired(), length(2)])
    emailRecado = StringField('E-mail', validators=[DataRequired(), email()])
    menssagem = StringField('Menssagem', validators=[DataRequired(), length(1)])
    btn_mandar_recado = SubmitField('Enviar')

class FormCadJg(FlaskForm):
    capaJogo = FileField('Nome da Foto')
    nomeJogo = StringField('Nome do Jogo', validators=[DataRequired(), length(2)])
    plataforma = SelectField('Selecione uma plataforma', choices=[('', ''), ('PC', 'PC'), ('Console', 'Console')], validators=[DataRequired()])
    preco = StringField('Preço', validators=[DataRequired(), length(2)])
    status = BooleanField('Jogo Indisponivel')
    btn_cadastrar_jogo = SubmitField('Cadastrar')
