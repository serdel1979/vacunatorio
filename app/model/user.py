from app import db
from flask_login import UserMixin, login_manager




class User(db.Model, UserMixin):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(20), unique=True)
    nombre = db.Column(db.String(20))
    apellido = db.Column(db.String(20))
    telefono = db.Column(db.String(20))
    nacimiento = db.Column(db.String(20))
    primera_dosis = db.Column(db.String(20))
    fecha_primera_dosis = db.Column(db.String(20))
    fecha_ultima_gripe = db.Column(db.String(20))
    paciente_riesgo = db.Column(db.String(20))
    fiebre_amarilla = db.Column(db.String(20))
    password = db.Column(db.String(20))
    email = db.Column(db.String(20))
    dni = db.Column(db.String(20))
    sede_preferida = db.Column(db.String(20))
    tipo = db.Column(db.Integer)
    sede = db.Column(db.String(20))

    def __init__(self,usuario,nombre,apellido,telefono=None,nacimiento=None,primera_dosis=None,fecha_primera_dosis=None, ultima_gripe=None,paciente_riesgo=None,fiebre_amarilla=None,password=None,email=None,dni=None,tipo=3, sede_preferida=None,sede=None):
        self.usuario = usuario
        self.nombre = nombre
        self.apellido = apellido
        self.telefono =telefono
        self.nacimiento = nacimiento
        self.primera_dosis = primera_dosis
        self.fecha_primera_dosis = fecha_primera_dosis
        self.fecha_ultima_gripe = ultima_gripe
        self.fiebre_amarilla = fiebre_amarilla
        self.paciente_riesgo = paciente_riesgo
        self.password = password
        self.email = email
        self.dni = dni
        self.sede_preferida=sede_preferida
        self.tipo = tipo
        self.sede = sede

    @classmethod
    def get_all(cls):
        return cls.query.all()
        
    
    @classmethod
    def get_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    @classmethod
    def get_by_tipo(cls, tipo):
        return cls.query.filter_by(tipo=tipo)

    @classmethod
    def get_by_username(cls, username):
        return cls.query.filter_by(usuario=bytes(username, 'utf-8')).first()

    @classmethod
    def get_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def get_by_dni(cls, dni):
        return cls.query.filter_by(dni=dni).first()


    @classmethod
    def delete(cls, id):
        usr = cls.query.get(id)
        db.session.delete(usr)
        db.session.commit()

    
    def cambiar_clave(self, password):
        self.password = password
        db.session.commit()

    def save(self):
        db.session.add(self)
        db.session.commit()
    