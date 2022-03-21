from wsgiref.validate import validator
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, DateField
from wtforms.validators import InputRequired, Email, Length


app = Flask(__name__)

app.config['SECRET_KEY']='Est4Cl4v3e5Sup3rS3cr3t4'

Bootstrap(app)


class LoginForm(FlaskForm):
    username = StringField('Usuario',validators=[InputRequired(),Length(min=4,max=15)])
    password = PasswordField('Contraseña',validators=[InputRequired(),Length(min=4,max=15)])

class RegistroForm(FlaskForm):
    usuario = StringField('Usuario',validators=[InputRequired(),Length(min=4,max=20)])
    nombre = StringField('Nombre',validators=[InputRequired(),Length(min=4,max=20)])
    apellido = StringField('Apellido',validators=[InputRequired(),Length(min=4,max=20)])
    telefono = StringField('Teléfono',validators=[InputRequired(),Length(min=4,max=20)])
    nacimiento = DateField('Fecha de nacimiento')
    primera_dosis = BooleanField('Tengo la primera dósis')
    paciente_riesgo = BooleanField('Soy paciente de riesgo')
    password = PasswordField('Escriba una contraseña',validators=[InputRequired(),Length(min=4,max=15)])
    email = StringField('Email', validators=[InputRequired(), Email(message='Email inválido'), Length(max=50)])
    dni = StringField('Dni',validators=[InputRequired(),Length(min=4,max=15)])



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html',form=form) 


@app.route('/registro')
def registro():
    form = RegistroForm()
    return render_template('registro.html',form=form) 


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html') 


if __name__ == '__main__':
    app.run(debug=True)