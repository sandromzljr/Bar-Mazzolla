from flask import render_template, redirect, url_for, flash, request
from sitebarmazzolla import app, database, bcrypt
from sitebarmazzolla.forms import FormLogin, FormCriarConta
from sitebarmazzolla.models import Usuario
from flask_login import login_user


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
        usuario = Usuario.query.filter_by(email=formLogin.email.data).first()
        if usuario and bcrypt.check_password_hash(usuario.senha, formLogin.senha.data):
            login_user(usuario, remember=formLogin.remember_me.data)
            flash('{} logado com sucesso!'.format(formLogin.email.data), 'alert-sucess')
            return redirect(url_for('home'))
        else:
            flash('Login incorreto. Verifique seu e-mail ou senha.', 'alert-danger')

    if formCriarConta.validate_on_submit() and 'btn_submit_signup' in request.form:
        senha_cript = bcrypt.generate_password_hash(formCriarConta.senha.data)
        usuario = Usuario(username=formCriarConta.username.data, email=formCriarConta.email.data, senha=senha_cript)
        database.session.add(usuario)
        database.session.commit()
        flash('Conta criado com sucesso para o e-mail: {}'.format(formCriarConta.email.data), 'alert-sucess')
        return redirect(url_for('home'))
    return render_template('login.html', formLogin=formLogin, formCriarConta=formCriarConta)
