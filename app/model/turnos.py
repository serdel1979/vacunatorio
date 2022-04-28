from app import db
from flask_login import UserMixin, login_manager
from datetime import date, datetime, timedelta




class Turno(db.Model, UserMixin):
    __tablename__ = 'turnos'
    id = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer)
    fecha_solicitud = db.Column(db.Date)
    fecha_turno = db.Column(db.Date)
    sede= db.Column(db.String(20))
    vacuna= db.Column(db.String(20))
    estado= db.Column(db.Integer)
    asistio= db.Column(db.Boolean)

    def __init__(self,id_usuario,fecha_turno,sede,vacuna,estado):
        self.id_usuario=id_usuario
        self.fecha_solicitud = datetime.now()
        self.fecha_turno = fecha_turno
        self.sede =sede
        self.vacuna = vacuna
        self.estado = estado
        self.asistio = False
    
        
    @classmethod
    def get_by_id_usuario(cls, id_usuario):
        return cls.query.filter_by(id_usuario=id_usuario).all()
        
    @classmethod
    def get_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def get_by_nombre_vacuna(cls, nombre_vacuna):
        return cls.query.filter_by(nombre_vacuna=nombre_vacuna).all()

    
    @classmethod
    def get_by_fecha(cls, fecha_turno, sede):
        return cls.query.filter(cls.fecha_turno==fecha_turno, cls.sede==sede).all()

    @classmethod
    def get_by_fiebre_amarilla(cls):
        return cls.query.filter(cls.vacuna==bytes('Fiebre amarilla', 'utf-8')).all()

    @classmethod
    def get_by_fecha_sedes(cls, fecha_turno):
        return cls.query.filter(cls.fecha_turno==fecha_turno).all()



    @classmethod
    def get_by_sede(cls, sede):
        return cls.query.filter_by(sede=sede).all()



    @classmethod
    def get_all(cls):
        return cls.query.all()


    @classmethod
    def delete(cls, id):
        usr = cls.query.get(id)
        db.session.delete(usr)
        db.session.commit()

    def save(self):
        db.session.add(self)
        db.session.commit()