from flask_sqlalchemy import SQLAlchemy

import datetime

db = SQLAlchemy()

class Alumnos(db.Model):
    __tablename__ = 'alumnos'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    apellidos = db.Column(db.String(50))
    email = db.Column(db.String(50))
    #fecha_nacimiento = db.Column(db.DateTime, default=datetime.datetime.now)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)
    #updated_at = db.Column(db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)
""" 
    def __init__(self, nombre, apellidos, email):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email

    def __repr__(self):
        return '<Alumno %r>' % self.nombre """