from flask import Flask, render_template, url_for, request, flash, redirect
from forms import FormCriarConta, FormLogin
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


app.config['SECRET_KEY'] = 'bar_mazzolla'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///barmazzolla.bd'

database = SQLAlchemy(app)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/sobre')
def sobre():
    return render_template('sobre.html')


@app.route('/localizacao')
def localizacao():
    return render_template('localizacao.html')


@app.route('/lista-usuarios')
def usuarios():
    userList = ['Sandro', 'Marina', 'Augusto', 'Jean']
    return render_template('user.html', userList=userList)


@app.route('/login', methods=['GET', 'POST'])
def login():
    formLogin = FormLogin()
    formCriarConta = FormCriarConta()

    if formLogin.validate_on_submit() and 'btn_submit_login' in request.form:
        flash('{} logado com sucesso!'.format(formLogin.email.data), 'alert-sucess')
        return redirect(url_for('home'))
    if formCriarConta.validate_on_submit() and 'btn_submit_signup' in request.form:
        flash('Conta criado com sucesso para o e-mail: {}'.format(formCriarConta.email.data), 'alert-sucess')
        return redirect(url_for('home'))

    return render_template('login.html', formLogin=formLogin, formCriarConta=formCriarConta)


if __name__ == '__main__':
    app.run(debug=True)
