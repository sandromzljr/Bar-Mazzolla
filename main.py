from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/localizacao')
def localizacao():
    return 'Estamos localizados na Rua Lucas Evangelista, 305 - Centro, Bebedouro - SP'

if __name__ == '__main__':
    app.run(debug=True)