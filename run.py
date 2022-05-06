from sched import scheduler

from sqlalchemy import null
from app import create_app
from enum import unique
from wsgiref.validate import validator
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, logout_user, login_required
from app.forms.forms import EnfermeroForm, LoginForm, RegistroForm, VacunaForm, RecuperarClave
from app.model.user import User
from app.model.vacunas import Vacuna
from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta
from app.model.turnos import Turno
from flask_mail import Mail
from flask_mail import Message
from random import choice
from datetime import datetime
import time
import os
from subprocess import call
from pytz import utc
from apscheduler.schedulers.background import BackgroundScheduler


from app import create_app

app = create_app()
mail = Mail(app)


sedes = ["Cementerio","Terminal","Municipal"]


def genera_clave():
    longitud = 8
    valores = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    p = ""
    p = p.join([choice(valores) for i in range(longitud)])
    return p


def enviar_mail(destinatario,mensaje):
    try:
        msg = Message("Email-title",sender="vacunatorioing2g36@gmail.com",body=mensaje,recipients=[destinatario])
        mail.send(msg)
        return True
    except:
        return False


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
                flash("Usuario o clave incorrecto","danger")
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


@app.route('/recuperar_clave')
def recuperar_clave():
    form = RecuperarClave()
    return render_template('recuperar_clave.html', form = form)


@app.route('/enviar_clave', methods=['POST'])
def enviar_clave():
    form = RecuperarClave()
    if form.validate_on_submit():
        email = form.email.data
        user = User.get_by_email(email)
        if user: 
            clave = genera_clave()
            msj = "Su clave nueva es: "+ clave
            if not enviar_mail(email,msj):
                flash("No se pudo enviar el email!!!","danger")
                return render_template('recuperar_clave.html',form=form)
            else:
                flash("La contraseña fue enviada al mail ingresado!!!","success")
                user.cambiar_clave(clave)
                return redirect(url_for('login'))
        else:
            flash("No existe el mail en el sistema!!!","danger")
            return render_template('recuperar_clave.html',form=form)
    return render_template('recuperar_clave.html', form = form)


def verifica_pass(pass1,pass2):
    return pass1==pass2


@app.route('/registro', methods=['GET','POST'])
def registro():
    form = RegistroForm()
    if form.validate_on_submit():
        if form.password.data != form.password2.data:
            flash("Las contraseñas no coinciden!!!","danger")
            return render_template('registro.html',form=form)
        dni = User.get_by_dni(form.dni.data)
        if dni:
            flash("El dni pertenece a un usuario del sistema", "danger")
            return render_template('registro.html',form=form)
        email = User.get_by_email(form.email.data)
        if email:
            flash("El email pertenece a un usuario del sistema","danger")
            return render_template('registro.html',form=form)
        
        usuario = User(nombre = form.nombre.data, 
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
    flash("El turno fue cancelado","success")
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
        usuario = User.get_by_id(id_usuario)
        fecha_de_turno = datetime.strptime(fecha_turno,'%Y-%m-%d').date() #fecha del turno
        vigentes = Turno.get_by_id_usuario_vigente(vacuna,id_usuario)
   
        if len(vigentes) > 0 and vacuna != "Fiebre amarilla":
            flash("Tiene turno vigente para la vacuna seleccionada","danger")
            return redirect(url_for('sacar_turno'))

        if vacuna == 'Fiebre amarilla':
            if usuario.fiebre_amarilla == 1:    #si fue vacunado por fiebre amarilla no acepta el turno
                flash("Usted ya fue vacunado por la fiebre amarilla","danger")
                return redirect(url_for('sacar_turno'))
            edad = relativedelta(datetime.now(), usuario.nacimiento)
            if edad.years > 60:    #si el paciente es mayor de 60 no acepta el turno
                flash("Usted no puede vacunarse por fiebre amarilla","danger")
                return redirect(url_for('sacar_turno'))
            amarilla = Turno.get_amarilla_vigente(id_usuario)
            if len(amarilla) > 0:
                flash("Usted tiene turno vigente para fiebre amarilla","danger")
                return redirect(url_for('sacar_turno'))
            amarilla = Turno.get__amarilla_espera_confirmacion(id_usuario)
            if len(amarilla) > 0:
                flash("Usted tiene turno esperando confirmación para fiebre amarilla","danger")
                return redirect(url_for('sacar_turno'))
            #get__amarilla_rechazado
            amarilla = Turno.get__amarilla_rechazado(id_usuario)
            if len(amarilla) > 0:
                flash("Usted tiene turnos rechazados para fiebre amarilla","danger")
                return redirect(url_for('sacar_turno'))

            estado = 4  #esperar que acepte el administrador
        
        if vacuna == 'Gripe':
            fecha_ultima_gripe = usuario.fecha_ultima_gripe
            if fecha_ultima_gripe != None:
               # fecha_ultima_gripe = datetime.strptime(fecha_ultima_gripe,'%Y-%m-%d').date()
                fecha_ult_grip = fecha_de_turno-timedelta(365)    #fecha de ultima vacuna de gripe
                if fecha_ult_grip < fecha_ultima_gripe:
                    flash("La fecha del turno debe superar el año de la última vacuna de gripe","danger")
                    return redirect(url_for('sacar_turno'))

        if vacuna == 'Covid':
            if usuario.fecha_primera_dosis != None and usuario.fecha_ultima_covid != None:
                flash("Usted ya tiene las dos dósis de Covid","danger")
                return redirect(url_for('sacar_turno'))
            
            fecha_ultima_covid = usuario.fecha_ultima_covid
            if fecha_ultima_covid != None:
                fecha_ult_covi = fecha_de_turno-timedelta(90) 
                if fecha_ult_covi < fecha_ultima_covid:
                    flash("La fecha del turno debe superar 90 días de la última vacuna de Covid","danger")
                    return redirect(url_for('sacar_turno'))


             #asigna un turno para la proxima dosis en 90 dias


        #estado 0 = pendiente de vacunarse
        #estado 1 = cancelado por el usuario
        #estado 2 = atendido por el enfermero
        #estado 3 = rechazado por el administrador si es fiebre amarilla
        #estado 4 = esperando confirmacion del administrador

        turno = Turno(id_usuario,fecha_turno,sede,vacuna,estado)
        turno.save()
    flash("Su turno fue registrado","success")
    return redirect(url_for('sacar_turno'))


@app.route('/edit_enfermero/<int:id>', methods=['GET','POST'])
def edit_enfermero(id):
    #sedes = ["Cementerio","Terminal","Municipal"]
    enfermero = User.get_by_id(id)
    if enfermero != None:
        if request.method=='POST':
            enfermero.sede= request.form['sede']
            enfermero.save()
            flash("Datos actualizados","success")
            return redirect(url_for('enfermeros'))
    return render_template('edit_enfermero.html',sedes=sedes, enfermero=enfermero,tipo = session["tipo"], id=session["id_user"])

@app.route('/guardar_perfil/<int:id>', methods=['GET','POST'])
def guardar_perfil(id):
    sedes = ["Cementerio","Terminal","Municipal"]
    usuario = User.get_by_id(id)
    if usuario != None:
        if request.method=='POST':
            usuario.telefono = request.form['telefono']
            usuario.mail= request.form['mail']
            usr= User.get_by_email(request.form['mail'])
            usuario.sede_preferida= request.form['sede_preferida']
            if usr != None:
                print(usr)
                flash("El mail ya existe", "danger")
                return redirect(url_for('edit_perfil'))
            usuario.save()
            flash("Datos actualizados", "success")
            return redirect(url_for('edit_perfil'))
    return render_template('perfil.html',sedes=sedes, usuario=usuario,tipo = session["tipo"], id=session["id_user"])

@app.route('/edit_perfil')
def edit_perfil():
    sedes = ["Cementerio","Terminal","Municipal"]
    usuario= User.get_by_id(session["id_user"])
    return render_template('editar_perfil.html',sedes=sedes, usuario=usuario)

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
    if session["tipo"] == 1:
        turnos = Turno.get_by_fecha_sedes(hoy)
    else:
        turnos = Turno.get_by_fecha(hoy,sede)
    return render_template('turnos_hoy.html',sede=sede,turnos=turnos,tipo = session["tipo"], id=session["id_user"]) 



@app.route('/turnos_fiebre_amarilla')
def turnos_fiebre_amarilla():
    hoy = date.today()
    turnos = Turno.get_by_fiebre_amarilla()
    return render_template('turnos_fiebre_amarilla.html',turnos=turnos,tipo = session["tipo"], id=session["id_user"]) 



@app.route('/ver_paciente/', methods=['GET'])
def ver_paciente():
    id_paciente = request.args.get("idusr")
    id_turno = request.args.get("idt")
    paciente = User.get_by_id(id_paciente)
    turno = Turno.get_by_id(id_turno)
    #############################
    edad = relativedelta(datetime.now(), paciente.nacimiento)
    #############################

    if datetime.strptime(datetime.today().strftime('%Y-%m-%d'),'%Y-%m-%d') > datetime.strptime(turno.fecha_turno.strftime('%Y-%m-%d'),'%Y-%m-%d'):
        turno.asistio = False
    return render_template('ver_paciente.html',edad=edad,paciente = paciente, turno=turno,tipo = session["tipo"], id=session["id_user"]) 



@app.route('/ver_paciente_fiebre/', methods=['GET'])
def ver_paciente_fiebre():
    id_paciente = request.args.get("idusr")
    print(request.args.get("idusr") )
    id_turno = request.args.get("idt")
    paciente = User.get_by_id(id_paciente)

    turno = Turno.get_by_id(id_turno)
    #############################
    edad = relativedelta(datetime.now(), paciente.nacimiento)
    #############################

    
    if datetime.strptime(datetime.today().strftime('%Y-%m-%d'),'%Y-%m-%d') > datetime.strptime(turno.fecha_turno.strftime('%Y-%m-%d'),'%Y-%m-%d'):
        turno.asistio = False

    return render_template('ver_paciente_fiebre.html',edad=edad, paciente = paciente, turno=turno,tipo = session["tipo"], id=session["id_user"]) 


@app.route('/aceptar_fiebre_amarilla', methods=['GET','POST'])
def marcar_fiebre_amarilla():
    if request.method=='POST':
        if 'aceptado' in request.form:
            idturno = request.form['idturno']
            turno = Turno.get_by_id(idturno)
            estado = request.form['aceptado']
            if estado == 'aceptado':
                turno.estado = 0
                flash("El turno fue aceptado!!","success")
            else:
                if estado == 'rechazado':
                   turno.estado = 3
                   flash("El turno fue rechazado!!","success")
                else:
                    if estado == 'esperando':
                        flash("El turno sigue en espera!!","success")
                        turno.estado = 4
            turno.save()       
    return redirect(url_for('turnos_fiebre_amarilla'))



@app.route('/marcar_vacunado', methods=['GET','POST'])
def marcar_vacunado():
    if request.method=='POST':
        if 'vacunado' in request.form:
            idturno = request.form['idturno']
            turno = Turno.get_by_id(idturno)
            usuario = User.get_by_id(turno.id_usuario)
            if turno.vacuna == "Covid":     #registra fecha en ultima dosis de covid en el usuario
                if usuario.fecha_primera_dosis == None:
                    usuario.fecha_primera_dosis = datetime.today()
                    td = timedelta(90)      #asigna un turno para la proxima dosis en 90 dias
                    nuevafecha=datetime.today()+td
                    turnoproximo = Turno(turno.id_usuario,nuevafecha,turno.sede,turno.vacuna,0)
                    turnoproximo.save()
                    flash("Se asignó un nuevo turno en 90 dás","success")
                else: 
                    usuario.fecha_ultima_covid  == None and usuario.fecha_primera_dosis != None
                    usuario.fecha_ultima_covid = datetime.today()
     
                usuario.save()
            if turno.vacuna == "Fiebre amarilla":
                usuario.fiebre_amarilla = 1
                usuario.save()
            if turno.vacuna == "Gripe":
                usuario.fecha_ultima_gripe = datetime.today()
                usuario.save()
            turno.estado=2
            turno.asistio = True
            turno.save()       
            
            flash("El turno fue actualizado !!","success")
    return redirect(url_for('turnos_hoy'))


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

 # Aca hago las estadisticas por Sede

@app.route('/estadisticas', methods=['GET'])
def estadisticas():
    return render_template('estadisticas.html', tipo=session["tipo"], id=session["id_user"])

@app.route('/ver_perfil', methods=['GET'])
def ver_perfil():
    user = User.get_by_id(session['id_user'])
    return render_template('perfil.html', tipo=session["tipo"], id=session["id_user"], user=user)


@app.route('/cambiar_contrasena', methods=['GET','POST'])
def cambiar_contrasena():
    if request.method=='POST':
    
        password = request.form['password']
        if len(password) < 4:
            flash("La contraseña debe superar los 3 caracteres!!","danger")
            return redirect(url_for('ver_perfil'))
        user = User.get_by_id(session['id_user'])
        user.cambiar_clave(password)
        flash("Cambio su contraseña correctamente!!","success")
    return redirect(url_for('ver_perfil'))



@app.route('/vacunas_por_sede', methods=['GET'])
def vacunas_por_sede():
    cantidad_por_sede = []
    cementerio = ["cementerio",len(Turno.cant_by_sede("Cementerio"))]
    cantidad_por_sede.append(cementerio)
    terminal = ["terminal", len(Turno.cant_by_sede("Terminal"))]
    cantidad_por_sede.append(terminal)
    municipal = ["municipal", len(Turno.cant_by_sede("Municipal"))]
    cantidad_por_sede.append(municipal)

    print(cantidad_por_sede)
    print(len(Turno.cant_by_sede("Cementerio")))
    print(len(Turno.cant_by_sede("Terminal")))
    print(len(Turno.cant_by_sede("Municipal")))
    return redirect(url_for('estadisticas'))



        
#def job():
#    print("")
#    call(['python', 'scheduler/main.py'])


if __name__ == '__main__':
 #   scheduler = BackgroundScheduler()
 #   scheduler.configure(timezone=utc)
 #   scheduler.add_job(job, 'interval', seconds=10)
 #   scheduler.start()
 #   print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

 #   try:
        # This is here to simulate application activity (which keeps the main thread alive).
        app.run(debug=True, use_reloader=True)
 #   except (KeyboardInterrupt, SystemExit):
        # Not strictly necessary if daemonic mode is enabled but should be done if possible
#        scheduler.shutdown() 
