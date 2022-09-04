from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class FormCriarConta(FlaskForm):
    username = StringField('Nome de Usuário', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha',
                          validators=[DataRequired(), Length(8, 20, 'Sua senha deve conter entre 8 e 20 caracteres.')])
    confirmaSenha = PasswordField('Confirmar Senha', validators=[DataRequired(), EqualTo('senha')])
    btn_submit_signup = SubmitField('Criar Conta')


class FormLogin(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(8, 20)])
    btn_submit_login = SubmitField('Fazer Login')
