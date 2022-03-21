from app import create_app
from enum import unique
from wsgiref.validate import validator
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from app.forms.forms import LoginForm, RegistroForm
from app.model.user import User

from app import create_app

app = create_app()


@app.route('/')
def index():
    return render_template('index.html')



@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return '<h1>'+form.usuario.data+' '+form.password.data+'</h1>'
    return render_template('login.html',form=form) 



@app.route('/registro', methods=['GET','POST'])
def registro():
    form = RegistroForm()
    if form.validate_on_submit():
        #return '<h1>'+form.usuario.data+' '+str(form.nacimiento.data)+' '+str(form.paciente_riesgo.data)+'</h1>'
        usuario = User(usuario=form.usuario.data, nombre = form.nombre.data, apellido=form.apellido.data, 
        telefono= form.telefono.data, nacimiento= form.nacimiento.data, primera_dosis=form.primera_dosis.data,
        paciente_riesgo=form.paciente_riesgo.data, password=form.password.data, email=form.email.data, dni=form.dni.data)
        
        usuario.save()
    return render_template('registro.html',form=form) 


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html') 




if __name__ == "__main__":
    app.run(debug=True)
