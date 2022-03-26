from app import create_app
from enum import unique
from wsgiref.validate import validator
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, logout_user, login_required
from app.forms.forms import EnfermeroForm, LoginForm, RegistroForm
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
        if user: 
            if verifica_pass(form.password.data, user.password):
                session["tipo"]= user.tipo
                session["id_user"] = user.id
                return render_template('index.html',tipo = session["tipo"], id=session["id_user"])
        else:
            user = User.get_by_dni(username)
            if user: 
                if verifica_pass(form.password.data, user.password):
                    session["tipo"]= user.tipo
                    session["id_user"] = user.id
                    return render_template('index.html',tipo = session["tipo"], id=session["id_user"])
            else:
                user = User.get_by_email(username)
                if user: 
                    if verifica_pass(form.password.data, user.password):
                        session["tipo"]= user.tipo
                        session["id_user"] = user.id
                        return render_template('index.html',tipo = session["tipo"], id=session["id_user"])
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
        flash("Usuario agregado!!!","success")
        return redirect(url_for('login'))
    return render_template('registro.html',form=form) 


@app.route('/enfermeros')
def enfermeros():
    enfermeros = User.get_by_tipo(tipo=2)
    return render_template('enfermeros.html',enfermeros=enfermeros,tipo = session["tipo"], id=session["id_user"]) 


@app.route('/edit_enfermero/<int:id>', methods=['GET','POST'])
def edit_enfermero(id):
    sedes = ["Cementerio","Terminal","Municipal"]
    enfermero = User.get_by_id(id)
    if enfermero != None:
        if request.method=='POST':
            enfermero.nombre = request.form['nombre']
            enfermero.apellido = request.form['apellido']
            enfermero.dni=request.form['dni']
            enfermero.telefono = request.form['telefono']
            enfermero.sede= request.form['sede']
            enfermero.save()
            flash("Datos actualizados","success")
            return render_template('edit_enfermero.html',sedes=sedes, enfermero=enfermero,tipo = session["tipo"], id=session["id_user"])

    return render_template('edit_enfermero.html',sedes=sedes, enfermero=enfermero,tipo = session["tipo"], id=session["id_user"])


@app.route('/borra_enfermero/<int:id>')
def borra_enfermero(id):
    User.delete(id)
    enfermeros = User.get_by_tipo(tipo=2)
    flash("Eliminado","success")
    return render_template('enfermeros.html',enfermeros=enfermeros,tipo = session["tipo"], id=session["id_user"]) 


@app.route('/agrega_enfermero', methods=['GET','POST'])
def agrega_enfermero():
    form = EnfermeroForm()
    if  form.validate_on_submit():
        if form.password.data != form.password2.data:
            flash("Las contraseñas no coinciden!!!","error")
            return render_template('agrega_enfermero.html', form=form, tipo = session["tipo"], id=session["id_user"])
        usr = User.get_by_username(form.usuario.data)
        if usr:
            flash("El usuario ya existe","error")
            return render_template('agrega_enfermero.html', form=form, tipo = session["tipo"], id=session["id_user"])
        dni = User.get_by_dni(form.dni.data)
        if dni:
            flash("El dni pertenece a un usuario del sistema", "error")
            return render_template('agrega_enfermero.html', form=form, tipo = session["tipo"], id=session["id_user"])
        email = User.get_by_email(form.email.data)
        if email:
            flash("El email pertenece a un usuario del sistema","error")
            return render_template('agrega_enfermero.html', form=form, tipo = session["tipo"], id=session["id_user"])
        usuario = User(usuario=form.usuario.data, nombre = form.nombre.data, apellido=form.apellido.data, 
        telefono= form.telefono.data, nacimiento= None, primera_dosis=None,
        paciente_riesgo=None, password=form.password.data, email=form.email.data, dni=form.dni.data, tipo=2, sede=form.sede.data)
       
        usuario.save()
        flash("Enfermero agregado!!!","success")
        return redirect(url_for('enfermeros'))
    return render_template('agrega_enfermero.html', form=form, tipo = session["tipo"], id=session["id_user"]) 

 




if __name__ == "__main__":
    app.run(debug=True)
