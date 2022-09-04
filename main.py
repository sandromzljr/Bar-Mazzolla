from flask import Flask, render_template, url_for
from forms import FormCriarConta, FormLogin

app = Flask(__name__)


app.config['SECRET_KEY'] = 'bar_mazzolla'


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


@app.route('/login')
def login():
    formLogin = FormLogin()
    formCriarConta = FormCriarConta()
    return render_template('login.html', formLogin=formLogin, formCriarConta=formCriarConta)


if __name__ == '__main__':
    app.run(debug=True)
