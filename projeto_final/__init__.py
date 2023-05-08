from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__, static_url_path='/static')
app.config['SECRET_KEY'] = 'c17619ef1f9809d4eabfb9670075a797'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projetoFinal.db'

banco = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'alerta'
login_manager.login_message = 'Faça um login para poder acessar a página'

from projeto_final import routers
