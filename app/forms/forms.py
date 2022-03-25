from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, DateField
from wtforms.validators import InputRequired, Email, Length

class LoginForm(FlaskForm):
    usuario = StringField('Usuario',validators=[InputRequired(),Length(min=4,max=15)])
    password = PasswordField('Contraseña',validators=[InputRequired(),Length(min=4,max=15)])

class RegistroForm(FlaskForm):
    usuario = StringField('Usuario',validators=[InputRequired(),Length(min=4,max=20)])
    nombre = StringField('Nombre',validators=[InputRequired(),Length(min=4,max=20)])
    apellido = StringField('Apellido',validators=[InputRequired(),Length(min=4,max=20)])
    telefono = StringField('Teléfono',validators=[InputRequired(),Length(min=4,max=20)])
    nacimiento = DateField('Fecha de nacimiento')
    primera_dosis = BooleanField('Tengo la primera dosis')
    paciente_riesgo = BooleanField('Soy paciente de riesgo')
    password = PasswordField('Escriba una contraseña',validators=[InputRequired(),Length(min=4,max=15)])
    password2 = PasswordField('Repita la contraseña',validators=[InputRequired(),Length(min=4,max=15)])
    email = StringField('Email', validators=[InputRequired(), Email(message='Email inválido'), Length(max=50)])
    dni = StringField('Dni',validators=[InputRequired(),Length(min=4,max=15)])

class EnfermeroForm(FlaskForm):
    nombre = StringField('Nombre',validators=[InputRequired(),Length(min=4,max=20)])
    apellido = StringField('Apellido',validators=[InputRequired(),Length(min=4,max=20)])
    telefono = StringField('Teléfono',validators=[InputRequired(),Length(min=4,max=20)])
    email = StringField('Email', validators=[InputRequired(), Email(message='Email inválido'), Length(max=50)])
    password = PasswordField('Escriba una contraseña',validators=[InputRequired(),Length(min=4,max=15)])
    password2 = PasswordField('Repita la contraseña',validators=[InputRequired(),Length(min=4,max=15)])
    dni = StringField('Dni',validators=[InputRequired(),Length(min=4,max=15)])
    sede = StringField('Sede',validators=[InputRequired(),Length(min=4,max=20)])