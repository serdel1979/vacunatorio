from app import db
from flask_login import UserMixin, login_manager




class Vacuna(db.Model, UserMixin):
    __tablename__ = 'vacunas'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(20), unique=True)
    

    def __init__(self,nombre):
        self.nombre = nombre
        
    @classmethod
    def get_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def get_by_nombre(cls, nombre):
        return cls.query.filter_by(nombre=nombre).first()

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