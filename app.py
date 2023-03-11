from flask import Flask, redirect, render_template, flash
from flask import request
from flask import url_for
import forms

from flask import jsonify
from config import DevelopmentConfig #archivo config con el debug y la conexion a mysql
from flask_wtf.csrf import CSRFProtect
from models import db 
# mapeo de la base de datos
from models import Alumnos # mapeo de la tabla alumnos

app = Flask(__name__)
app.config.from_object(DevelopmentConfig) # generar configuracion de bd ( servidor, usuario, pass, puesto), cadena de conexion
csrf = CSRFProtect()

@app.route("/", methods = ['GET', 'POST'])
def index():
    create_form = forms.UserForm(request.form)
    if request.method == 'POST':
        #objeto que permite pasarselo al db para guardarlo en la base de datos
        alum = Alumnos(nombre = create_form.nombre.data,
                       apellidos = create_form.apellidos.data,
                       email = create_form.email.data)
        db.session.add(alum)
        db.session.commit()
        return redirect(url_for('ABCompleto'))
    return render_template('index.html', form = create_form)

@app.route("/ABCompleto", methods=['GET','POST'])
def ABCompleto():
    create_form = forms.UserForm(request.form)
    #select * from alumnos
    alumnos = Alumnos.query.all()
    return render_template('ABCompleto.html', form = create_form, alumnos = alumnos)

@app.route("/modificar", methods=['GET','POST'])
def modificar():
    create_form = forms.UserForm(request.form)
    if request.method == 'GET':
        id = request.args.get('id')
        #select * from alumnos where id = id
        alum1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        create_form.id.data = alum1.id
        create_form.nombre.data = alum1.nombre
        create_form.apellidos.data = alum1.apellidos
        create_form.email.data = alum1.email
    
    if request.method == 'POST':
        id = create_form.id.data
        alum = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        alum.nombre = create_form.nombre.data
        alum.apellidos = create_form.apellidos.data
        alum.email = create_form.email.data
        db.session.add(alum)
        db.session.commit()
        return redirect(url_for('ABCompleto'))
        
    return render_template('modificar.html', form = create_form)


@app.route("/eliminar", methods=['GET'])
def eliminar():
    id = request.args.get('id')
    #delete from alumnos where id = id
    alum1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()
    db.session.delete(alum1)
    db.session.commit()
    flash("Se ha eliminado el registro con id: {}".format(alum1.id))
    return redirect(url_for('ABCompleto'))


if __name__ == "__main__":
    csrf.init_app(app)
    db.init_app(app) # inicia la conexion en base de datos
    with app.app_context():
        db.create_all() # analizar archivo config para corroborar que esten mapeado, sino, crea el mapeo
    app.run(port=3000)