from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


app.config['SECRET_KEY'] = 'bar_mazzolla'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///barmazzolla.bd'

database = SQLAlchemy(app)