from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class FormLogin(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email(message='Digite um endereço de e-mail válido.')])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(8, 20, message='Sua senha deve conter entre 8 e 20 caracteres.')])
    btn_submit_login = SubmitField('Fazer Login')
    remember_me = BooleanField('Lembrar-me')


class FormCriarConta(FlaskForm):
    username = StringField('Nome de Usuário', validators=[DataRequired(message='Nome de usuário inválido.')])
    email = StringField('E-mail', validators=[DataRequired(), Email(message='Digite um endereço de e-mail válido.')])
    senha = PasswordField('Senha',
                          validators=[DataRequired(), Length(8, 20, message='Sua senha deve conter entre 8 e 20 caracteres.')])
    confirmaSenha = PasswordField('Confirmar Senha', validators=[DataRequired(message='Senha diferente da preenchida anteriormente.'), EqualTo('senha')])
    btn_submit_signup = SubmitField('Criar Conta')
