from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)

app.config['SECRET_KEY'] = '5dc455d6e0c479aad983463161003105'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///barmazzolla.bd'

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from sitebarmazzolla import routes
