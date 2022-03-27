from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, DateField, SelectField
from wtforms.validators import InputRequired, Email, Length



class LoginForm(FlaskForm):
    usuario = StringField('Usuario',validators=[InputRequired(),Length(min=4,max=100)])
    password = PasswordField('Contraseña',validators=[InputRequired(),Length(min=4,max=100)])

class RegistroForm(FlaskForm):
    usuario = StringField('Usuario',validators=[InputRequired(),Length(min=4,max=100)])
    nombre = StringField('Nombre',validators=[InputRequired(),Length(min=4,max=100)])
    apellido = StringField('Apellido',validators=[InputRequired(),Length(min=4,max=100)])
    telefono = StringField('Teléfono',validators=[InputRequired(),Length(min=4,max=100)])
    nacimiento = DateField('Fecha de nacimiento')
    primera_dosis = BooleanField('Tengo la primera dosis')
    paciente_riesgo = BooleanField('Soy paciente de riesgo')
    password = PasswordField('Escriba una contraseña',validators=[InputRequired(),Length(min=4,max=100)])
    password2 = PasswordField('Repita la contraseña',validators=[InputRequired(),Length(min=4,max=100)])
    email = StringField('Email', validators=[InputRequired(), Email(message='Email inválido'), Length(max=100)])
    dni = StringField('Dni',validators=[InputRequired(),Length(min=4,max=20)])

class EnfermeroForm(FlaskForm):
    usuario = StringField('Usuario',validators=[InputRequired(),Length(min=4,max=100)])
    nombre = StringField('Nombre',validators=[InputRequired(),Length(min=4,max=100)])
    apellido = StringField('Apellido',validators=[InputRequired(),Length(min=4,max=100)])
    telefono = StringField('Teléfono',validators=[InputRequired(),Length(min=4,max=100)])
    email = StringField('Email', validators=[InputRequired(), Email(message='Email inválido'), Length(max=100)])
    password = PasswordField('Escriba una contraseña',validators=[InputRequired(),Length(min=4,max=100)])
    password2 = PasswordField('Repita la contraseña',validators=[InputRequired(),Length(min=4,max=100)])
    dni = StringField('Dni',validators=[InputRequired(),Length(min=4,max=100)])
    sede = SelectField("Sede",choices=[("Municipal","Municipal"),("Terminal","Terminal"),("Cementerio","Cementerio")])

class VacunaForm(FlaskForm):
    nombre = StringField('Nombre',validators=[InputRequired(),Length(min=4,max=100)])

