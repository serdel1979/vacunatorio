from app import db
from flask_login import UserMixin, login_manager
from app.model.laboratorios import Laboratorio

from app.model.vacunas import Vacuna




class Laboratorio_Vacuna(db.Model, UserMixin):
    __tablename__ = 'laboratorio_vacuna'
    id = db.Column(db.Integer, primary_key=True)
    id_laboratorio = db.Column(db.Integer)
    id_vacuna = db.Column(db.Integer)

    def __init__(self,id_laboratorio,id_vacuna):
        self.id_laboratorio = id_laboratorio
        self.id_vacuna = id_vacuna



    @classmethod
    def get_all(cls):
        return cls.query.all()




   # @classmethod
   # def get_labs_vacuna(cls,id_v):
   #     return db.session.query(Vacuna,
   #     Laboratorio_Vacuna).filter(Laboratorio_Vacuna.id_vacuna == id_v).filter(Vacuna.id == Laboratorio_Vacuna.id_vacuna).all()
        
   # @classmethod
   # def get_laboratorios_de_vacuna(cls, id_v):
   #     return cls.query.filter_by(id_vacuna=id_v).all()

    @classmethod
    def get_laboratorios_de_vacuna(cls, id_v):
        return db.session.query(
        Laboratorio, Laboratorio_Vacuna).filter(
        id_v == Laboratorio_Vacuna.id_vacuna).filter(Laboratorio_Vacuna.id_laboratorio==Laboratorio.id).all()
        
    @classmethod
    def buscar_laboratorios_de_vacuna(cls, id_v, id_lab):
        return db.session.query(
        Laboratorio, Laboratorio_Vacuna).filter(
        id_v == Laboratorio_Vacuna.id_vacuna).filter(Laboratorio_Vacuna.id_laboratorio==Laboratorio.id).filter(Laboratorio_Vacuna.id_laboratorio==id_lab).all()
        

    def save(self):
        db.session.add(self)
        db.session.commit()


    @classmethod
    def delete(cls, id):
        lab = cls.query.get(id)
        db.session.delete(lab)
        db.session.commit()