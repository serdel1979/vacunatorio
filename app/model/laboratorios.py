from app import db
from flask_login import UserMixin, login_manager




class Laboratorio(db.Model, UserMixin):
    __tablename__ = 'laboratorios'
    id = db.Column(db.Integer, primary_key=True)
    id_vacuna = db.Column(db.Integer)
    nombre = db.Column(db.String(100))

    def __init__(self,id_vacuna,nombre):
        self.id_vacuna = id_vacuna
        self.nombre = nombre

    @classmethod
    def get_lab_de_vacuna(cls, id_vacuna):
        return cls.query.filter(cls.id_vacuna==id_vacuna).all()

    @classmethod
    def get_by_id(cls, id):
        return cls.query.filter_by(id=id).first()


    def save(self):
        db.session.add(self)
        db.session.commit()