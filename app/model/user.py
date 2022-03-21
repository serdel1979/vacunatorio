from app import db

class User(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(20), unique=True)
    nombre = db.Column(db.String(20))
    apellido = db.Column(db.String(20))
    telefono = db.Column(db.String(20))
    nacimiento = db.Column(db.String(20))
    primera_dosis = db.Column(db.String(20))
    paciente_riesgo = db.Column(db.String(20))
    password = db.Column(db.String(20))
    email = db.Column(db.String(20))
    dni = db.Column(db.String(20))

    def __init__(self,usuario,nombre,apellido,telefono,nacimiento,primera_dosis,paciente_riesgo,password,email,dni,tipo=3):
        self.usuario = usuario
        self.nombre = nombre
        self.apellido = apellido
        self.telefono =telefono
        self.nacimiento = nacimiento
        self.primera_dosis = primera_dosis
        self.paciente_riesgo = paciente_riesgo
        self.password = password
        self.email = email
        self.dni = dni
        self.tipo = tipo

        db.create_all()

    def save(self):
        db.session.add(self)
        db.session.commit()
    