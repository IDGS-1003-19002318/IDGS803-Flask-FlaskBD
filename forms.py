#from wtforms import Form, StringField, IntegerField, validators, EmailField

from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import  Form, StringField, IntegerField, validators, EmailField
from wtforms import validators

class UserForm(Form):
    id = IntegerField('Id')
    nombre = StringField('Nombre')
    apellidos = StringField('Apellidos')
    email = EmailField('Email')