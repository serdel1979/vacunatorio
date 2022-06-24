from app import db
from flask_login import UserMixin, login_manager




class Laboratorio(db.Model, UserMixin):
    __tablename__ = 'laboratorios'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))

    def __init__(self,nombre):
        self.nombre = nombre

    @classmethod
    def get_lab_by_id(cls, id):
        return cls.query.filter(cls.id==id).first()

    @classmethod
    def get_by_nombre(cls, nombre):
        return cls.query.filter_by(nombre=nombre).first()

    @classmethod
    def get_all(cls):
        return cls.query.all()

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def delete(cls, id):
        lab = cls.query.get(id)
        db.session.delete(lab)
        db.session.commit()