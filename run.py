from app import create_app
from enum import unique
from wsgiref.validate import validator
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, logout_user, login_required
from app.forms.forms import EnfermeroForm, LoginForm, RegistroForm, VacunaForm
from app.model.user import User
from app.model.vacunas import Vacuna
from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta
from app.model.turnos import Turno



from app import create_app

app = create_app()

sedes = ["Cementerio","Terminal","Municipal"]

@app.route('/')
def index():
    return redirect(url_for('login'))



@app.route('/login', methods=['GET','POST'])
def login():
    if 'tipo' in session:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        username = form.usuario.data
        user = User.get_by_username(username)
        if user: 
            if verifica_pass(form.password.data, user.password):
                session["tipo"]= user.tipo
                session["id_user"] = user.id
                session["sede"] = user.sede
                return redirect(url_for('home'))
        else:
            user = User.get_by_dni(username)
            if user: 
                if verifica_pass(form.password.data, user.password):
                    session["tipo"]= user.tipo
                    session["id_user"] = user.id
                    session["sede"] = user.sede
                    return redirect(url_for('home'))
            else:
                user = User.get_by_email(username)
                if user: 
                    if verifica_pass(form.password.data, user.password):
                        session["tipo"]= user.tipo
                        session["id_user"] = user.id
                        session["sede"] = user.sede
                        #return render_template('index.html',tipo = session["tipo"], id=session["id_user"])
                        return redirect(url_for('home'))
            flash("Usuario o clave incorrecto","danger")
            return render_template('login.html',form=form)
    return render_template('login.html',form=form) 


@app.route('/home')
def home():
    if "tipo" in session:
        return render_template('index.html',tipo = session["tipo"], id=session["id_user"])
    else:
        return redirect(url_for('login'))

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
            flash("Las contraseñas no coinciden!!!","danger")
            return render_template('registro.html',form=form)
        usr = User.get_by_username(form.usuario.data)
        if usr:
            flash("El usuario ya existe","danger")
            return render_template('registro.html',form=form)
        dni = User.get_by_dni(form.dni.data)
        if dni:
            flash("El dni pertenece a un usuario del sistema", "danger")
            return render_template('registro.html',form=form)
        email = User.get_by_email(form.email.data)
        if email:
            flash("El email pertenece a un usuario del sistema","danger")
            return render_template('registro.html',form=form)
        
        usuario = User(usuario=form.usuario.data, nombre = form.nombre.data, 
        apellido=form.apellido.data, 
        telefono= form.telefono.data, nacimiento= form.nacimiento.data, 
        primera_dosis=form.primera_dosis.data,
        paciente_riesgo=form.paciente_riesgo.data,fiebre_amarilla=form.fiebre_amarilla.data,
        password=form.password.data, email=form.email.data, dni=form.dni.data, 
        sede_preferida= form.sede_preferida.data, sede=0)
        usuario.save()
        
        #calcula edad de la persona que se registra
        fecha_nacimiento = form.nacimiento.data
        edad = relativedelta(datetime.now(), fecha_nacimiento)
        #print(f"{edad.years} años, {edad.months} meses y {edad.days} días")
        #aca si es mayor de 60 se registra un turno para covid
        if edad.years > 60 or usuario.paciente_riesgo == 1:
            usrturno = User.get_by_dni(usuario.dni)
            hoy = datetime.now()
            fecha_turno = hoy + timedelta(days=7)
            turno = Turno(usrturno.id,fecha_turno,usrturno.sede_preferida,"Covid",False)
            turno.save() 
            flash("Se le asignó un turno para Covid!!!","success")
            #asignar turno para gripe
        if edad.years > 60:
            usrturno = User.get_by_dni(usuario.dni)
            hoy = datetime.now()
            fecha_turno = hoy + timedelta(days=7)
            turno = Turno(usrturno.id,fecha_turno,usrturno.sede_preferida,"Gripe",False)
            flash("Se le asignó un turno para la Gripe!!!","success")
            turno.save()

        flash("Usuario agregado!!!","success")
        return redirect(url_for('login'))
    return render_template('registro.html',form=form) 


@app.route('/enfermeros')
def enfermeros():
    enfermeros = User.get_by_tipo(tipo=2)
    return render_template('enfermeros.html',enfermeros=enfermeros,tipo = session["tipo"], id=session["id_user"]) 

@app.route('/mis_turnos')
def mis_turnos():
    misturnos = Turno.get_by_id_usuario(session["id_user"])
    return render_template('mis_turnos.html',misturnos=misturnos,tipo = session["tipo"], id=session["id_user"]) 

@app.route('/cancela_turno/<int:id>')
def cancela_turno(id):
    misturnos = Turno.get_by_id(id)
    misturnos.estado = 1
    misturnos.save()
    flash("El turno fue cancelado","danger")
    return redirect(url_for('mis_turnos'))




@app.route('/sacar_turno')
def sacar_turno():
    vacuns = Vacuna.get_all()
    vacunas=[]
    min= datetime.now()
    min = min + timedelta(days=7)
    for v in vacuns:
        vacunas.append(v.nombre)
    return render_template('pedir_turno.html',min=min,sedes=sedes,vacunas=vacunas,tipo = session["tipo"], id=session["id_user"]) 



@app.route('/registra_turno', methods=['GET','POST'])
def registra_turno():
    if request.method=='POST':
        fecha_turno = request.form['fecha_turno']
        sede = request.form['sede']
        vacuna = request.form['vacuna']
        id_usuario=session["id_user"]
        fecha_turno = request.form['fecha_turno']
        sede =request.form['sede']
        vacuna = request.form['vacuna']
        estado = 0
        #estado 0 = pendiente de vacunarse
        #estado 1 = cancelado por el usuario
        #estado 2 = atendido por el enfermero
        #estado 3 = rechazado por el administrador si es fiebre amarilla
        turno = Turno(id_usuario,fecha_turno,sede,vacuna,estado)
        turno.save()
    flash("pediste un re turno","success")
    return redirect(url_for('sacar_turno'))


@app.route('/edit_enfermero/<int:id>', methods=['GET','POST'])
def edit_enfermero(id):
    #sedes = ["Cementerio","Terminal","Municipal"]
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
            return redirect(url_for('enfermeros'))
    return render_template('edit_enfermero.html',sedes=sedes, enfermero=enfermero,tipo = session["tipo"], id=session["id_user"])


@app.route('/borra_vacuna/<int:id>')
def borra_vacuna(id):
    Vacuna.delete(id)
    vacunas = Vacuna.get_all()
    flash("Eliminado","success")
    return redirect(url_for('vacunas'))


@app.route('/edit_vacuna/<int:id>', methods=['GET','POST'])
def edit_vacuna(id):
    vacuna= Vacuna.get_by_id(id)
    if vacuna != None:
        if request.method=='POST':
            vacuna.nombre = request.form['nombre']
            vacuna.save()
            flash("Datos actualizados","success")
            return redirect(url_for('vacunas'))
    return render_template('edit_vacuna.html', vacuna=vacuna,tipo = session["tipo"], id=session["id_user"])


@app.route('/borra_enfermero/<int:id>')
def borra_enfermero(id):
    User.delete(id)
    enfermeros = User.get_by_tipo(tipo=2)
    flash("Eliminado","success")
    return render_template('enfermeros.html',enfermeros=enfermeros,tipo = session["tipo"], id=session["id_user"]) 



@app.route('/turnos_hoy')
def turnos_hoy():
    hoy = date.today()
    sede = session["sede"]
    turnos = Turno.get_by_fecha(hoy,sede)
    return render_template('turnos_hoy.html',sede=sede,turnos=turnos,tipo = session["tipo"], id=session["id_user"]) 



@app.route('/ver_paciente/', methods=['GET'])
def ver_paciente():
    id_paciente = request.args.get("idusr")
    id_turno = request.args.get("idt")
    paciente = User.get_by_id(id_paciente)
    turno = Turno.get_by_id(id_turno)
    return render_template('ver_paciente.html',paciente = paciente, turno=turno,tipo = session["tipo"], id=session["id_user"]) 



@app.route('/vacunas')
def vacunas():
    vacunas = Vacuna.get_all()
    return render_template('vacunas.html',vacunas=vacunas, tipo = session["tipo"], id=session["id_user"]) 


@app.route('/agrega_vacuna', methods=['GET','POST'])
def agrega_vacuna():
    form = VacunaForm()
    if form.validate_on_submit():
        vacuna = Vacuna.get_by_nombre(form.nombre.data)
        if vacuna:
            flash("La vacuna ya existe!!!","error")
            return render_template('agrega_vacuna.html',form=form,tipo = session["tipo"], id=session["id_user"]) 
        vacuna = Vacuna(form.nombre.data)
        vacuna.save()
        flash("Vacuna guardada!!!","error")
        return redirect(url_for('vacunas'))
    return render_template('agrega_vacuna.html',form=form,tipo = session["tipo"], id=session["id_user"]) 




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
