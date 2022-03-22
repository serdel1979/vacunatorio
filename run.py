from app import create_app
from enum import unique
from wsgiref.validate import validator
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, logout_user, login_required
from app.forms.forms import LoginForm, RegistroForm
from app.model.user import User

from app import create_app

app = create_app()


@app.route('/')
def index():
    return redirect(url_for('login'))



@app.route('/login', methods=['GET','POST'])
def login():
    if 'tipo' in session:
        return render_template('index.html',tipo = session["tipo"], id=session["id_user"] )
    form = LoginForm()
    if form.validate_on_submit():
        username = form.usuario.data
        user = User.get_by_username(username)
        if user and verifica_pass(form.password.data, user.password):
            session["tipo"]= user.tipo
            session["id_user"] = user.id
            return render_template('index.html',tipo = session["tipo"], id=session["id_user"])
        else:
            flash("Usuario o clave incorrecto")
            return render_template('login.html',form=form)
    return render_template('login.html',form=form) 


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))



def verifica_pass(pass1,pass2):
    return pass1==pass2

@app.route('/registro', methods=['GET','POST'])
def registro():
    form = RegistroForm()
    if form.validate_on_submit():
        if form.password.data != form.password2.data:
            flash("Las contraseñas no coinciden!!!","error")
            return render_template('registro.html',form=form)
        usr = User.get_by_username(form.usuario.data)
        if usr:
            flash("El usuario ya existe","error")
            return render_template('registro.html',form=form)
        dni = User.get_by_dni(form.dni.data)
        if dni:
            flash("El dni pertenece a un usuario del sistema", "error")
            return render_template('registro.html',form=form)
        email = User.get_by_email(form.email.data)
        if email:
            flash("El email pertenece a un usuario del sistema","error")
            return render_template('registro.html',form=form)
        usuario = User(usuario=form.usuario.data, nombre = form.nombre.data, apellido=form.apellido.data, 
        telefono= form.telefono.data, nacimiento= form.nacimiento.data, primera_dosis=form.primera_dosis.data,
        paciente_riesgo=form.paciente_riesgo.data, password=form.password.data, email=form.email.data, dni=form.dni.data, sede=0)
       
        usuario.save()
        flash("Usuario agregado, ahora inicie sesión!!!","success")
        return redirect(url_for('login'))
    return render_template('registro.html',form=form) 


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html') 




if __name__ == "__main__":
    app.run(debug=True)
