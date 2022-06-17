import datetime
from wsgiref.validate import validator
from flask_wtf import FlaskForm
from pymysql import Date
from wtforms import StringField, PasswordField, BooleanField, DateField, SelectField, Form, IntegerField
from wtforms.validators import InputRequired, Email, Length, NumberRange



class LoginForm(FlaskForm):
    usuario = IntegerField('Dni',validators=[InputRequired(),NumberRange(min=1000000, max=99999999, message='Longitud inválida')])
    password = PasswordField('Contraseña',validators=[InputRequired(),Length(min=4,max=50)])


class RecuperarClave(FlaskForm):
    email = StringField('Ingrese su email',validators=[InputRequired(), Email(message='Email inválido'), Length(max=100)])



class NullableDateField(DateField):
    """Native WTForms DateField throws error for empty dates.
    Let's fix this so that we could have DateField nullable."""
    def process_formdata(self, valuelist):
        if valuelist:
            date_str = ' '.join(valuelist).strip()
            if date_str == '':
                self.data = None
                return
            try:
                self.data = datetime.datetime.strptime(date_str, self.format[0]).date()
            except ValueError:
                self.data = None
                raise ValueError(self.gettext('No es una fecha válida'))



class RegistroForm(FlaskForm):
    nombre = StringField('Nombre *',validators=[InputRequired(),Length(min=4,max=100)])
    apellido = StringField('Apellido *',validators=[InputRequired(),Length(min=4,max=100)])
    telefono = IntegerField('Teléfono *',validators=[InputRequired()])
    nacimiento = DateField('Fecha de nacimiento *',validators=[InputRequired('Fecha de nacimiento inválida')])
    primera_dosis = BooleanField('Tengo la primera dosis de covid')
    fecha_primera_dosis = NullableDateField('Primera dósis de Covid')
    segunda_covid = BooleanField('Tengo dos dosis de covid')
    fecha_ultima_gripe = NullableDateField('Última vacuna de Gripe')
    fiebre_amarilla = BooleanField('Estoy vacunado para la fiebre amarilla')
    paciente_riesgo = BooleanField('Soy paciente de riesgo')
    password = PasswordField('Escriba una contraseña *',validators=[InputRequired(),Length(min=4,max=100)])
    password2 = PasswordField('Repita la contraseña *',validators=[InputRequired(),Length(min=4,max=100)])
    email = StringField('Email *', validators=[InputRequired(), Email(message='Email inválido'), Length(max=100)])
    dni = IntegerField('Dni *',validators=[InputRequired(),NumberRange(min=4000, max=99999999, message='Longitud inválida')])
    sede_preferida = SelectField("Sede Preferida",choices=[("Municipal","Municipal"),("Terminal","Terminal"),("Cementerio","Cementerio")])
    
    #validators=[NumberRange(min=1, max=5, message='Invalid length')]

    def validate(self):
        if not Form.validate(self):
            if self.nombre.data == None or self.apellido.data == None or self.telefono.data == None or self.nacimiento.data == None or self.dni.data == None or self.email.data == None:
                return False
            else:
                print("primera dosis ---> ",self.fecha_primera_dosis.data)
                return True
        else:
            return True
    
    def validate_date(form, field):
        return None
    
  


class EnfermeroForm(FlaskForm):
    nombre = StringField('Nombre',validators=[InputRequired(),Length(min=4,max=100)])
    apellido = StringField('Apellido',validators=[InputRequired(),Length(min=4,max=100)])
    telefono = IntegerField('Teléfono',validators=[InputRequired()])
    email = StringField('Email *', validators=[InputRequired(), Email(message='Email inválido'), Length(min=4,max=100)])
    password = PasswordField('Escriba una contraseña',validators=[InputRequired(),Length(min=4,max=100)])
    password2 = PasswordField('Repita la contraseña',validators=[InputRequired(),Length(min=4,max=100)])
    dni = IntegerField('Dni',validators=[InputRequired()])
    sede = SelectField("Sede",choices=[("Municipal","Municipal"),("Terminal","Terminal"),("Cementerio","Cementerio")])

class VacunaForm(FlaskForm):
    nombre = StringField('Nombre',validators=[InputRequired(),Length(min=4,max=100)])

