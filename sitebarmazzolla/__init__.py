from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

app.config['SECRET_KEY'] = '5dc455d6e0c479aad983463161003105'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///barmazzolla.bd'

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Para visualizar este conteúdo, faça Login.'

from sitebarmazzolla import routes
