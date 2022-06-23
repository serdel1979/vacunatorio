from sched import scheduler

from sqlalchemy import null
from app import create_app
from enum import unique
from wsgiref.validate import validator
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, logout_user, login_required
from app.forms.forms import EnfermeroForm, LoginForm, RegistroForm, VacunaForm, RecuperarClave
from app.model.laboratorio_vacuna import Laboratorio_Vacuna
from app.model.laboratorios import Laboratorio
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


def enviar_mail(destinatario,mensaje,asunto):
    try:
        msg = Message(asunto,sender="vacunatorioing2g36@gmail.com",body=mensaje,recipients=[destinatario])
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
                session["dni"] = user.dni
                return redirect(url_for('home'))
            else:
                flash("Usuario o clave incorrecto","danger")
        else:
            user = User.get_by_dni(username)
            if user: 
                if verifica_pass(form.password.data, user.password) and user.tipo == 2:
                    session["tipo"]= user.tipo
                    session["id_user"] = user.id
                    session["sede"] = user.sede
                    session["dni"] = user.dni
                    return redirect(url_for('turnos_hoy'))

                if verifica_pass(form.password.data, user.password):
                    session["tipo"]= user.tipo
                    session["id_user"] = user.id
                    session["sede"] = user.sede
                    session["dni"] = user.dni
                    return redirect(url_for('home'))
                
            else:
                user = User.get_by_email(username)
                if user: 
                    if verifica_pass(form.password.data, user.password):
                        session["tipo"]= user.tipo
                        session["id_user"] = user.id
                        session["sede"] = user.sede
                        session["dni"] = user.dni
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
            if not enviar_mail(email,msj,asunto="NUEVA PASSWORD"):
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
        #validacion de fechas y nombres

        if form.nombre.data != None: 
            if not checkstr(form.nombre.data):
                flash("El nombre tiene caracteres inválidos!!!","danger")
                return render_template('registro.html',form=form)

        if form.apellido.data != None: 
            if not checkstr(form.apellido.data):
                flash("El apellido tiene caracteres inválidos!!!","danger")
                return render_template('registro.html',form=form)

        if form.nacimiento.data != None: 
            if date.today() < form.nacimiento.data:
                flash("Las fecha de nacimiento es incorrecta!!!","danger")
                return render_template('registro.html',form=form)

        if form.fecha_primera_dosis.data != None: 
            if date.today() < form.fecha_primera_dosis.data:
                flash("La fecha en la primera dósis de covid es incorrecta!!!","danger")
                return render_template('registro.html',form=form)
        
        if form.fecha_primera_dosis.data != None: 
            if form.nacimiento.data > form.fecha_primera_dosis.data:
                flash("Error en la fecha de vacunación por covid con respecto al nacimiento!!!","danger")
                return render_template('registro.html',form=form)

        if form.fecha_ultima_gripe.data != None: 
            if form.nacimiento.data > form.fecha_ultima_gripe.data:
                flash("Error en la fecha de vacunación de gripe con respecto al nacimiento!!!","danger")
                return render_template('registro.html',form=form)

        #fecha_ultima_gripe
        if form.fecha_ultima_gripe.data != None: 
            if date.today() < form.fecha_ultima_gripe.data:
                flash("La fecha en la dósis de gripe es incorrecta!!!","danger")
                return render_template('registro.html',form=form)
   
 
        ################
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
        primera_dosis=form.segunda_covid.data, fecha_primera_dosis=form.fecha_primera_dosis.data,
        ultima_gripe=form.fecha_ultima_gripe.data,
        paciente_riesgo=form.paciente_riesgo.data,fiebre_amarilla=form.fiebre_amarilla.data,
        password=form.password.data, email=form.email.data, dni=form.dni.data, 
        sede_preferida= form.sede_preferida.data, sede=0)
        usuario.save()
        
        usuario = User.get_by_dni(form.dni.data)
        numero_dosis = 1
    
        #calcula edad de la persona que se registra
        fecha_nacimiento = form.nacimiento.data
        edad = relativedelta(datetime.now(), fecha_nacimiento)
        #print(f"{edad.years} años, {edad.months} meses y {edad.days} días")
        #aca si es mayor de 60 se registra un turno para covid
        hoy = datetime.now().date()
        if (edad.years > 60 or usuario.paciente_riesgo == 1) and usuario.primera_dosis == 0: #y si no tiene las dos dósis(primera dosis es segunda jaj)
            
            if usuario.fecha_primera_dosis != None:
                fecha_seg_covid = usuario.fecha_primera_dosis+timedelta(21) #calcula fecha que le iría si tuviera una dósis de covid
                numero_dosis = 2
            else:
                numero_dosis = 2
                fecha_seg_covid = hoy + timedelta(days=7)
            
            if hoy > fecha_seg_covid:
                fecha_turno = hoy + timedelta(days=7) #si se pasaron de los 21 días le da el turno para la próxima semana
                turno = Turno(usuario.id,fecha_turno,usuario.sede_preferida,"Covid",False)
                turno.numero_dosis=numero_dosis
                turno.save() 
                flash("Se le asignó un turno para Covid!!!","success")
            else:
                turno = Turno(usuario.id,fecha_seg_covid,usuario.sede_preferida,"Covid",False)
                turno.numero_dosis=numero_dosis
                turno.save() 
                flash("Se le asignó un turno para Covid!!!","success")

            #asignar turno para gripe
        if edad.years > 60:
            if usuario.fecha_ultima_gripe != None:
                fecha_ult_grip = usuario.fecha_ultima_gripe+timedelta(365) #calcula fecha que le iría si tuviera una dósis de covid
            else:
                fecha_ult_grip = hoy + timedelta(days=30)
            hoy = datetime.now().date()
            if hoy > fecha_ult_grip:
                fecha_turno = hoy + timedelta(days=30)
                turno = Turno(usuario.id,fecha_turno,usuario.sede_preferida,"Gripe",False)
                flash("Se le asignó un turno para la Gripe!!!","success")
                turno.save()
            else:
                turno = Turno(usuario.id,fecha_ult_grip,usuario.sede_preferida,"Gripe",False)
                flash("Se le asignó un turno para la Gripe!!!","success")
                turno.save()


        flash("Usuario agregado!!!","success")
        return redirect(url_for('login'))
    return render_template('registro.html',form=form) 


def checkstr(nombre):
    for c in nombre:
        if c not in " abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZáéíóúÁÉÍÓÚ":
            return False
    return True


@app.route('/enfermeros')
def enfermeros():
    enfermeros = User.get_by_tipo(tipo=2)
    return render_template('enfermeros.html',enfermeros=enfermeros,tipo = session["tipo"], id=session["id_user"]) 

@app.route('/mis_turnos')
def mis_turnos():
    misturnos = Turno.get_by_id_usuario(session["id_user"])
    cantidad_turnos = len(misturnos)
    return render_template('mis_turnos.html',misturnos=misturnos,tipo = session["tipo"], id=session["id_user"], cantidad_turnos=cantidad_turnos)


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
        id_usuario=session["id_user"]
        fecha_turno = request.form['fecha_turno']
        sede =request.form['sede']
        vacuna = request.form['vacuna']
        estado = 0
        usuario = User.get_by_id(id_usuario)
        fecha_de_turno = datetime.strptime(fecha_turno,'%Y-%m-%d').date() #fecha del turno
        vigentes = Turno.get_by_id_usuario_vigente(vacuna,id_usuario)

        numero_dosis = 1
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
            flash("El turno queda pendiente de aceptación","warning")
        
        if vacuna == 'Gripe':
            fecha_ultima_gripe = usuario.fecha_ultima_gripe
            if fecha_ultima_gripe != None:
               # fecha_ultima_gripe = datetime.strptime(fecha_ultima_gripe,'%Y-%m-%d').date()
                fecha_ult_grip = fecha_de_turno-timedelta(365)    #fecha de ultima vacuna de gripe
                if fecha_ult_grip < fecha_ultima_gripe:
                    flash("La fecha del turno debe superar el año de la última vacuna de gripe","danger")
                    return redirect(url_for('sacar_turno'))

        if vacuna == 'Covid':
            if (usuario.fecha_primera_dosis != None and usuario.fecha_ultima_covid != None) or usuario.primera_dosis: #si ya fue vacunado las dos dósis o se registro con 2 dósis directamente
                flash("Usted ya tiene las dos dósis de Covid","danger")
                return redirect(url_for('sacar_turno'))
            
            fecha_ultima_covid = usuario.fecha_ultima_covid
            if fecha_ultima_covid != None:
                fecha_ult_covi = fecha_de_turno-timedelta(21) 
                numero_dosis = 2
                if fecha_ult_covi < fecha_ultima_covid:
                    flash("La fecha del turno debe superar 21 días de la última vacuna de Covid","danger")
                    return redirect(url_for('sacar_turno'))


            #asigna un turno para la proxima dosis en 90 dias


        #estado 0 = pendiente de vacunarse
        #estado 1 = cancelado por el usuario
        #estado 2 = atendido por el enfermero
        #estado 3 = rechazado por el administrador si es fiebre amarilla
        #estado 4 = esperando confirmacion del administrador
        #estado 5 = ausente

        turno = Turno(id_usuario,fecha_turno,sede,vacuna,estado)
        turno.numero_dosis = numero_dosis
        turno.save()
    if estado != 4:
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
            if usuario.tipo == 3:
                if(usuario.email == request.form['mail'] and usuario.telefono == request.form['telefono'] and usuario.sede_preferida == request.form['sede_preferida'] and usuario.nombre == request.form['nombre'] and usuario.apellido == request.form['apellido'] and usuario.dni == request.form['dni']):
                    flash("No actualizó ningun dato", "warning")
                    return redirect(url_for('edit_perfil'))
                usr= User.get_by_email(request.form['mail'])
                if usr != None:
                    if usuario.id != usr.id:
                        flash("El mail ya existe", "danger")
                        return redirect(url_for('edit_perfil'))
                usr= User.get_by_dni(request.form['dni'])
                if usr != None:
                    if usuario.id != usr.id:
                        flash("El dni ya existe", "danger")
                        return redirect(url_for('edit_perfil'))
            else:
                if(usuario.email == request.form['mail'] and usuario.telefono == request.form['telefono'] and usuario.nombre == request.form['nombre'] and usuario.apellido == request.form['apellido'] and usuario.dni == request.form['dni']):
                    flash("No actualizó ningun dato", "warning")
                    return redirect(url_for('edit_perfil'))
                usr= User.get_by_email(request.form['mail'])
                if usr != None:
                    if usuario.id != usr.id:
                        flash("El mail ya existe", "danger")
                        return redirect(url_for('edit_perfil'))
                usr= User.get_by_dni(request.form['dni'])
                if usr != None:
                    if usuario.id != usr.id:
                        flash("El dni ya existe", "danger")
                        return redirect(url_for('edit_perfil'))
            usuario.nombre = request.form['nombre']
            usuario.dni = request.form['dni']
            usuario.apellido = request.form['apellido']
            usuario.telefono = request.form['telefono']
            usuario.email = request.form['mail']
            if usuario.tipo == 3:
                usuario.sede_preferida= request.form['sede_preferida']
            usuario.save()
            flash("Datos actualizados", "success")
            return redirect(url_for('edit_perfil'))
    return render_template('perfil.html',sedes=sedes, usuario=usuario,tipo = session["tipo"], id=session["id_user"])

@app.route('/edit_perfil')
def edit_perfil():
    sedes = ["Cementerio","Terminal","Municipal"]
    usuario= User.get_by_id(session["id_user"])
    return render_template('editar_perfil.html',sedes=sedes, usuario=usuario,tipo = session["tipo"], id=session["id_user"])


@app.route('/borra_vacuna/<int:id>')
def borra_vacuna(id):
    Vacuna.delete(id)
    vacunas = Vacuna.get_all()
    flash("Eliminado","success")
    return redirect(url_for('vacunas'))


@app.route('/edit_vacuna/<int:id>', methods=['GET','POST'])
def edit_vacuna(id):
    vacuna= Vacuna.get_by_id(id)
    labs = Laboratorio.get_all()
    laboratorios_de_vacuna = Laboratorio_Vacuna.get_laboratorios_de_vacuna(id)
    
   
    if request.method=='POST':
           if 'id_lab' in request.form:
                busca = Laboratorio_Vacuna.buscar_laboratorios_de_vacuna(id,request.form['id_lab'])
                if len(busca) > 0:
                    flash("Ese laboratorio ya está agregado","warning")
                    return redirect(url_for('edit_vacuna',id=id))
                lab = Laboratorio_Vacuna(request.form['id_lab'],id)
                lab.save()
                return redirect(url_for('edit_vacuna',id=id))
                
           if 'id_lab_sacar' in request.form:
                busca = Laboratorio_Vacuna.buscar_laboratorios_de_vacuna(id,request.form['id_lab_sacar'])
                if len(busca) > 0:
                    print(busca[0][1].id)
                    Laboratorio_Vacuna.delete(busca[0][1].id)
                    return redirect(url_for('edit_vacuna',id=id))

    return render_template('edit_vacuna.html',labs_vac = laboratorios_de_vacuna ,laboratorios = labs, vacuna=vacuna,tipo = session["tipo"], id=session["id_user"])


@app.route('/borra_enfermero/<int:id>')
def borra_enfermero(id):
    User.delete(id)
    flash("Eliminado","success")
    return redirect(url_for('enfermeros'))



@app.route('/turnos_hoy')
def turnos_hoy():
    hoy = date.today()
    sede = session["sede"]
    if session["tipo"] == 1:
        usuarios = Turno.get_by_fecha_sedes(hoy)
    else:
        usuarios = Turno.usuario_hoy(hoy,sede)
    cantidad = len(usuarios)
    return render_template('turnos_hoy.html',sede=sede,tipo = session["tipo"], id=session["id_user"], cantidad = cantidad, usuarios=usuarios) 


@app.route('/historial_hoy')
def historial_hoy():
    hoy = date.today()
    sede = session["sede"]
    if session["tipo"] == 1:
        usuarios = Turno.historial_by_fecha(hoy)
    else:
        usuarios = Turno.usuario_hoy_historial(hoy,sede)
    cantidad = len(usuarios)
    return render_template('historial_hoy.html',sede=sede,tipo = session["tipo"], id=session["id_user"], cantidad=cantidad, usuarios=usuarios) 



@app.route('/turnos_fiebre_amarilla')
def turnos_fiebre_amarilla():
    hoy = date.today()
    turnos = Turno.get_by_fiebre_amarilla()
    return render_template('turnos_fiebre_amarilla.html',turnos=turnos,tipo = session["tipo"], id=session["id_user"]) 


@app.route('/ver_historial_paciente/<int:id>', methods=['GET','POST'])
def ver_historial_paciente(id):
    paciente = User.get_by_id(id)
    historial = Turno.usuario_historial_general(id)
    cantidad = len(historial)
    dos_dosis = False
    fiebre_amarilla = False
    fecha_primera_dosis = None
    ultima_gripe = None
    if paciente.primera_dosis: #el campo primera dosis indica si tiene dos dosis de covid
            dos_dosis = True
    if paciente.fiebre_amarilla:
            fiebre_amarilla = True
    if paciente.fecha_primera_dosis:
            fecha_primera_dosis = paciente.fecha_primera_dosis
    if paciente.fecha_ultima_gripe:
            ultima_gripe = paciente.fecha_ultima_gripe
    edad = relativedelta(datetime.now(), paciente.nacimiento)
    return render_template('ver_historial_paciente.html',cantidad=cantidad, data = historial, paciente=paciente,  edad=edad.years, tipo = session["tipo"], id=session["id_user"],dos_dosis=dos_dosis, fiebre_amarilla=fiebre_amarilla,fecha_primera_dosis=fecha_primera_dosis,ultima_gripe=ultima_gripe) 


@app.route('/ver_historial_paciente_fiebre/<int:id>', methods=['GET','POST'])
def ver_historial_paciente_fiebre(id):
    paciente = User.get_by_id(id)
    historial = Turno.usuario_historial_general(id)
    cantidad = len(historial)
    dos_dosis = False
    fiebre_amarilla = False
    fecha_primera_dosis = None
    ultima_gripe = None
    if paciente.primera_dosis: #el campo primera dosis indica si tiene dos dosis de covid
            dos_dosis = True
    if paciente.fiebre_amarilla:
            fiebre_amarilla = True
    if paciente.fecha_primera_dosis:
            fecha_primera_dosis = paciente.fecha_primera_dosis
    if paciente.fecha_ultima_gripe:
            ultima_gripe = paciente.fecha_ultima_gripe
    edad = relativedelta(datetime.now(), paciente.nacimiento)
    return render_template('ver_paciente_fiebre_amarilla_historial.html',cantidad=cantidad, data = historial, paciente=paciente,  edad=edad.years, tipo = session["tipo"], id=session["id_user"],dos_dosis=dos_dosis, fiebre_amarilla=fiebre_amarilla,fecha_primera_dosis=fecha_primera_dosis,ultima_gripe=ultima_gripe) 



@app.route('/ver_paciente/', methods=['GET'])
def ver_paciente():
    id_paciente = request.args.get("idusr")
    id_turno = request.args.get("idt")
    paciente = User.get_by_id(id_paciente)
    turno = Turno.get_by_id(id_turno)
    #############################
    edad = relativedelta(datetime.now(), paciente.nacimiento)
    #############################
    vacunas = Turno.get_historial(id_paciente)
    cantidad = len(vacunas)
    dos_dosis = False
    fiebre_amarilla = False
    fecha_primera_dosis = None
    ultima_gripe = None
    if paciente.primera_dosis: #el campo primera dosis indica si tiene dos dosis de covid
            dos_dosis = True
    if paciente.fiebre_amarilla:
            fiebre_amarilla = True
    if paciente.fecha_primera_dosis:
            fecha_primera_dosis = paciente.fecha_primera_dosis
    if paciente.fecha_ultima_gripe:
            ultima_gripe = paciente.fecha_ultima_gripe
    if datetime.strptime(datetime.today().strftime('%Y-%m-%d'),'%Y-%m-%d') > datetime.strptime(turno.fecha_turno.strftime('%Y-%m-%d'),'%Y-%m-%d'):
        turno.asistio = False
    return render_template('ver_paciente.html',edad=edad,paciente = paciente, turno=turno,tipo = session["tipo"], id=session["id_user"], vacunas = vacunas, cantidad = cantidad, dos_dosis=dos_dosis, fiebre_amarilla=fiebre_amarilla,fecha_primera_dosis=fecha_primera_dosis,ultima_gripe=ultima_gripe) 



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



@app.route('/aceptar_turno_fiebre', methods=['GET','POST'])
def aceptar_turno_fiebre():
    idturno = request.form['idturno']
    turno = Turno.get_by_id(idturno)
    turno.estado=0
    turno.save()
    flash("El turno fue aceptado","success")
    return redirect(url_for('turnos_fiebre_amarilla'))


@app.route('/marcar_vacunado', methods=['GET','POST'])
def marcar_vacunado():
        idturno = request.form['idturno']
        lab = request.form['laboratorio']
        lot = request.form['lote']
        if lot == None or lot == "":
            flash("Ingrese el número de lote","danger")
            return redirect(url_for("turnos_hoy"))
        turno = Turno.get_by_id(idturno)
        usuario = User.get_by_id(turno.id_usuario)
        if turno.vacuna == "Covid":     #registra fecha en ultima dosis de covid en el usuario
            if usuario.fecha_primera_dosis == None:
                usuario.fecha_primera_dosis = datetime.today()
                td = timedelta(21)      #asigna un turno para la proxima dosis en 21 dias
                nuevafecha=datetime.today()+td
                turnoproximo = Turno(turno.id_usuario,nuevafecha,turno.sede,turno.vacuna,0)
                turnoproximo.numero_dosis = 2
                turnoproximo.save()
                flash("Se le asignó un turno para el dia: " + turnoproximo.fecha_turno.strftime('%d/%m/%Y'),"success")
            else: 
                if usuario.fecha_ultima_covid  == None and usuario.fecha_primera_dosis != None:
                    usuario.fecha_ultima_covid = datetime.today()
            usuario.save()
        if turno.vacuna == "Fiebre amarilla":
            usuario.fiebre_amarilla = 1
            usuario.save()
        if turno.vacuna == "Gripe":
            usuario.fecha_ultima_gripe = datetime.today()
            usuario.save()
        turno.estado=2
        turno.laboratorio = lab
        turno.lote = lot
        turno.asistio = True
        turno.save()       
            
        flash("El turno fue actualizado !!","success")
        return redirect(url_for('turnos_hoy'))


@app.route('/marcar_ausente/<int:id>')
def marcar_ausente(id):
        turno = Turno.get_by_id(id)
        turno.estado=5
        turno.asistio = False
        turno.save()         
        flash("El turno fue actualizado !!","success")
        return redirect(url_for('turnos_hoy'))




@app.route('/turnos_notificar', methods=['GET','POST'])
def turnos_notificar():
    min=datetime.now()
    if request.method=='POST':
        min=request.form['buscar']
        pendientes=Turno.get_pendientes_fecha(request.form['buscar'])
        return render_template('turnos_para_notificar.html',min=min,pendientes=pendientes,tipo = session["tipo"], id=session["id_user"]) 
    
    pendientes = Turno.get_pendientes()
    return render_template('turnos_para_notificar.html',min=min,pendientes=pendientes,tipo = session["tipo"], id=session["id_user"]) 

@app.route('/notificar', methods=['GET','POST'])
def notificar():
    if request.method=='POST':
        email = request.form['email']
        idturno = request.form['idturno']
        turno = Turno.get_by_id(idturno)
        msg='Estimado, le recordamos que tiene un turno el día '+turno.fecha_turno.strftime('%d/%m/%Y')+' para vacunarse por '+turno.vacuna
        if enviar_mail(email,msg,"RECORDATORIO"):
            turno.notificado = 1
            turno.save()
            flash("Se notificó al usuario exitosamente","success")
        else:
            flash("Hubo un error en la notificación","danger")
    return redirect(url_for('turnos_notificar'))


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
            flash("La vacuna ya existe!!!","danger")
            return render_template('agrega_vacuna.html',form=form,tipo = session["tipo"], id=session["id_user"]) 
        vacuna = Vacuna(form.nombre.data)
        vacuna.save()
        flash("Vacuna guardada!!!","success")
        return redirect(url_for('vacunas'))
    return render_template('agrega_vacuna.html',form=form,tipo = session["tipo"], id=session["id_user"]) 




@app.route('/agrega_enfermero', methods=['GET','POST'])
def agrega_enfermero():
    form = EnfermeroForm()
    if  form.validate_on_submit():
        if form.password.data != form.password2.data:
            flash("Las contraseñas no coinciden!!!","danger")
            return render_template('agrega_enfermero.html', form=form, tipo = session["tipo"], id=session["id_user"])
        dni = User.get_by_dni(form.dni.data)
        if dni:
            flash("El dni pertenece a un usuario del sistema", "danger")
            return render_template('agrega_enfermero.html', form=form, tipo = session["tipo"], id=session["id_user"])
        email = User.get_by_email(form.email.data)
        if email:
            flash("El email pertenece a un usuario del sistema","danger")
            return render_template('agrega_enfermero.html', form=form, tipo = session["tipo"], id=session["id_user"])
        usuario = User(nombre = form.nombre.data, apellido=form.apellido.data, 
        telefono= form.telefono.data, nacimiento= None, primera_dosis=None,
        paciente_riesgo=None, password=form.password.data, email=form.email.data, dni=form.dni.data, tipo=2, sede=form.sede.data)
       
        usuario.save()
        flash("Enfermero agregado!!!","success")
        return redirect(url_for('enfermeros'))
    return render_template('agrega_enfermero.html', form=form, tipo = session["tipo"], id=session["id_user"]) 

 # Aca hago las estadisticas por Sede

@app.route('/estadisticas', methods=['GET','POST'])
def estadisticas():
    fecha1 = date.today()
    fecha2= fecha1

    if request.method=='POST':

            fecha1 = request.form['fecha1']
            fecha2 = request.form['fecha2']

            if fecha1 == "" or fecha2 == "":

                flash("Ingrese las fechas","danger")
                return redirect(url_for('estadisticas'))


            if fecha1 > fecha2:
                flash("La fecha 1 no puede ser mayor a la fecha 2","danger")
                return redirect(url_for('estadisticas'))
            

            cantidad_por_sede = []
            for sede in sedes:
                cantidad_por_sede.append([sede,len(Turno.cant_by_sede(sede))])
            
            vacunas = Vacuna.get_all()
            enfermedades = []
            for enfermedad in vacunas:
                enfermedades.append(enfermedad.nombre)
            cantidad_por_enfermedad = []

            for enf in enfermedades:
                cantidad_por_enfermedad.append([enf,len(Turno.cant_by_enfermedad_fecha(enf,fecha1,fecha2))])

            
            por_rango_edad = []
            por_rango_edad.append(["Menor de 18 ",len(Turno.cantidad_menor_18_fecha(fecha1,fecha2))])
            por_rango_edad.append(["Entre 18 y 60",len(Turno.cantidad_entre_18_y_60_fecha(fecha1,fecha2))])
            por_rango_edad.append(["Mayor de 60",len(Turno.cantidad_mayor_60_fecha(fecha1,fecha2))])


    else:
            cantidad_por_sede = []
            for sede in sedes:
                cantidad_por_sede.append([sede,len(Turno.cant_by_sede(sede))])
            
            vacunas = Vacuna.get_all()
            enfermedades = []
            for enfermedad in vacunas:
                enfermedades.append(enfermedad.nombre)
            cantidad_por_enfermedad = []

            for enf in enfermedades:
                cantidad_por_enfermedad.append([enf,len(Turno.cant_by_enfermedad(enf))])

            
            por_rango_edad = []
            por_rango_edad.append(["Menor de 18 ",len(Turno.cantidad_menor_18())])
            por_rango_edad.append(["Entre 18 y 60",len(Turno.cantidad_entre_18_y_60())])
            por_rango_edad.append(["Mayor de 60",len(Turno.cantidad_mayor_60())])
    
    return render_template('estadisticas.html', tipo=session["tipo"], id=session["id_user"], fecha1=fecha1, fecha2=fecha2, cant_por_sedes = cantidad_por_sede, cant_por_enfermedad = cantidad_por_enfermedad, por_edades = por_rango_edad)



@app.route('/ver_perfil', methods=['GET'])
def ver_perfil():
    user = User.get_by_id(session['id_user'])
    if user.paciente_riesgo == 1:
        riesgo = True
    else:
        riesgo = False
    return render_template('perfil.html', tipo=session["tipo"], id=session["id_user"], user=user, riesgo = riesgo)



@app.route('/mis_vacunas' , methods=['GET'])
def mis_vacunas():
    dos_dosis = False
    fiebre_amarilla = False
    fecha_primera_dosis = None
    ultima_gripe = None
    usuario = User.get_by_id(session['id_user'])
    if usuario.primera_dosis: #el campo primera dosis indica si tiene dos dosis de covid
            dos_dosis = True
    if usuario.fiebre_amarilla:
            fiebre_amarilla = True
    if usuario.fecha_primera_dosis:
            fecha_primera_dosis = usuario.fecha_primera_dosis
    if usuario.fecha_ultima_gripe:
            ultima_gripe = usuario.fecha_ultima_gripe
    mis_vacunas = Turno.get_mis_vacunas(session['id_user'])
    cantidad_vacunas = len(mis_vacunas)
    return render_template('mis_vacunas.html', tipo=session["tipo"], id=session["id_user"], vacunas=mis_vacunas, cantidad_vacunas = cantidad_vacunas, dos_dosis= dos_dosis, fiebre_amarilla=fiebre_amarilla, fecha_primera_dosis = fecha_primera_dosis, ultima_gripe=ultima_gripe)

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

@app.route('/cambiar_contrasena', methods=['GET','POST'])
def cambiar_contrasena():
    if request.method=='POST':
        password = request.form['password']
        password_new = request.form['password_new']
        re_password = request.form['re-password']
        usuario = User.get_by_id(session["id_user"])
        print(usuario.id)
        if len(password) < 4 or usuario.password != password:
            flash("Contraseña actual incorrecta","danger")
            return render_template('cambiar_contrasena.html', tipo=session["tipo"], id=session["id_user"])
        if usuario.password == password and password_new != re_password:
            flash("Las contraseñas ingresadas no coinciden","danger")
            return render_template('cambiar_contrasena.html', tipo=session["tipo"], id=session["id_user"])
        if len(password_new) < 4 or len(re_password) < 4:
            flash("La contraseña nueva debe tener mas de 3 caracteres","danger")
            return render_template('cambiar_contrasena.html', tipo=session["tipo"], id=session["id_user"])
        usuario.cambiar_clave(password_new)
        flash("Cambio su contraseña correctamente!!","success")
    return render_template('cambiar_contrasena.html', tipo=session["tipo"], id=session["id_user"])


@app.route('/modificar_contrasena/', methods=['GET'])
def modificar_contrasena(): 
    return render_template('cambiar_contrasena.html', tipo=session["tipo"], id=session["id_user"])
        

@app.route('/pacientes', methods=['GET','POST'])
def pacientes():
    if request.method=='POST':
        pacientes = User.by_username(request.form['buscar'])
    else:
        pacientes = User.get_by_tipo(3)
    return render_template('pacientes.html', tipo=session["tipo"], id=session["id_user"], pacientes = pacientes)


@app.route('/ver_historial/<int:id>', methods=['GET','POST'])
def ver_historial(id):
    vacunas = Turno.get_historial(id)
    cantidad = len(vacunas)
    return render_template('historial_paciente.html', tipo=session["tipo"], id=session["id_user"], vacunas = vacunas, cantidad= cantidad)

@app.route('/buscar_paciente_turno', methods=['POST'])
def buscar_paciente():
    sede = session["sede"]
    hoy = date.today()
    dni = request.form['buscar']
    if(dni == ""):
        flash("No se ingresó ningun DNI", "warning")
        return redirect(url_for('turnos_hoy'))
    usr = User.get_by_dni(dni)
    if(usr == None):
        flash("El DNI ingresado no existe", "warning")
        return redirect(url_for('turnos_hoy'))
    if request.method=='POST':
        if usr != None:
            usuarios = Turno.historial_usuario_hoy(hoy,usr,sede)
        else:
            usuarios = Turno.usuario_hoy(hoy,sede)
    cantidad = len(usuarios)
    return render_template('turnos_hoy.html', sede=sede,tipo=session["tipo"], id=session["id_user"], usuarios = usuarios, cantidad=cantidad)

@app.route('/rechazar_fiebre_amarilla/<int:id>')
def rechazar_fiebre_amarilla(id):
    turno = Turno.get_by_id(id)
    turno.estado=3
    turno.save()         
    flash("El turno fue rechazado !!","success")
    return redirect(url_for('turnos_fiebre_amarilla'))

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
