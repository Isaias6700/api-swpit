
from sqlalchemy import Integer,Column,String,Boolean,ForeignKey,CHAR,Date,Time
from api.data.db import db

class AplicPorEst(db.Model):
    __tablename__ = "aplicporest"
    idAplocPorEst = Column(Integer, primary_key=True)
    FechaAplicacion = Column(Date, unique=False, nullable=False)
    HoraInicial = Column(Time, unique=False, nullable=False)
    HoraFinal = Column(Time, unique=False, nullable=False)

    idEstudiante = Column(Integer, ForeignKey('estudiantes.idEstudiante'))
    idAplicacion = Column(Integer,ForeignKey('aplicaciones.idAplicacion'))
    estudiante = db.relationship("Estudiantes", backref='aplicporest', order_by=idAplocPorEst)
    aplicacion = db.relationship("Aplicaciones", backref='aplicporest', order_by=idAplocPorEst)