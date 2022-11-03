from flask import render_template, redirect, url_for, flash, request, abort
from sitebarmazzolla import app, database, bcrypt
from sitebarmazzolla.forms import FormLogin, FormCriarConta, FormEditarPerfil, FormCriarPost
from sitebarmazzolla.models import Usuario, Post
from flask_login import login_user, logout_user, current_user, login_required
import secrets
import os
from PIL import Image


@app.route('/')
def home():
    posts = Post.query.order_by(Post.id.desc())
    return render_template('home.html', posts=posts)


@app.route('/sobre')
def sobre():
    return render_template('sobre.html')


@app.route('/localizacao')
def localizacao():
    return render_template('localizacao.html')


@app.route('/usuarios')
@login_required
def usuarios():
    userList = Usuario.query.all()
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
            par_next = request.args.get('next')
            if par_next:
                return  redirect(par_next)
            else:
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

@app.route('/sair')
@login_required
def sair():
    logout_user()
    return redirect(url_for('home'))

@app.route('/perfil')
@login_required
def perfil():
    foto_perfil = url_for('static', filename='fotos_perfil/{}'.format(current_user.foto_perfil))
    return render_template('perfil.html', foto_perfil=foto_perfil)

@app.route('/post/criar', methods=['GET', 'POST'])
@login_required
def criar_post():
    form = FormCriarPost()
    if form.validate_on_submit():
        post = Post(titulo=form.titulo.data, corpo=form.corpo.data, autor=current_user)
        database.session.add(post)
        database.session.commit()
        flash('Conversa Iniciada com Sucesso!', 'alert-success')
        return redirect(url_for('home'))
    return render_template('criar_post.html', form=form)

def salvar_imagem(imagem):
    codigo = secrets.token_hex(8)
    nome, extensao = os.path.splitext(imagem.filename)
    nome_arquivo = nome + codigo + extensao
    caminho_completo = os.path.join(app.root_path, 'static/fotos_perfil', nome_arquivo)
    tamanho = (155, 155)
    imagem_reduzida = Image.open(imagem)
    imagem_reduzida.thumbnail(tamanho)
    imagem_reduzida.save(caminho_completo)
    return nome_arquivo

@app.route('/perfil/editar', methods=['GET', 'POST'])
@login_required
def editar_perfil():
    form = FormEditarPerfil()
    if form.validate_on_submit():
        current_user.email = form.email.data
        current_user.username = form.username.data
        if form.foto_perfil.data:
            nome_imagem = salvar_imagem(form.foto_perfil.data)
            current_user.foto_perfil = nome_imagem
        database.session.commit()
        flash('Perfil atualizado com sucesso.', 'alert-sucess')
        return redirect(url_for('perfil'))
    elif request.method == "GET":
        form.email.data = current_user.email
        form.username.data = current_user.username
    foto_perfil = url_for('static', filename='fotos_perfil/{}'.format(current_user.foto_perfil))
    return render_template('editarperfil.html', foto_perfil=foto_perfil, form=form)

@app.route('/post/<post_id>', methods=['GET', 'POST'])
@login_required
def exibir_post(post_id):
    post = Post.query.get(post_id)
    if current_user == post.autor:
        form = FormCriarPost()
        if request.method == "GET":
            form.titulo.data = post.titulo
            form.corpo.data = post.corpo
        elif form.validate_on_submit():
            post.titulo = form.titulo.data
            post.corpo = form.corpo.data
            database.session.commit()
            flash('Conversa Editada com Sucesso!')
            return redirect(url_for('home'))
    else:
        form = None
    return render_template('post.html', post=post, form=form)

@app.route('/post/<post_id>/excluir',  methods=['GET', 'POST'])
@login_required
def excluir_post(post_id):
    post = Post.query.get(post_id)
    if current_user == post.autor:
        database.session.delete(post)
        database.session.commit()
        flash('Conversa Excluida com Sucesso')
        return redirect(url_for('home'))
    else:
        abort(403)