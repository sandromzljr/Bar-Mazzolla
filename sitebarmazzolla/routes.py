from flask import render_template, redirect, url_for, flash, request
from sitebarmazzolla import app
from sitebarmazzolla.forms import FormLogin, FormCriarConta


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

