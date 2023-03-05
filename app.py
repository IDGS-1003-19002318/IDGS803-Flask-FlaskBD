
from flask import Flask, render_template, redirect, url_for, request, make_response, flash, jsonify
import forms

from flask_sqlalchemy import SQLAlchemy
from config import DevelopmentConfig
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
from models import db, Alumnos

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf = CSRFProtect(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    create_form = forms.UserForm(request.form)
    
    if request.method == 'POST' and create_form.validate():
        alumno = Alumnos(nombre=create_form.nombre.data, 
                         apellidos=create_form.apellidos.data, 
                         email=create_form.email.data)
        db.session.add(alumno)
         db.session.commit()
        flash('Alumno creado correctamente')
        #return redirect(url_for('index'))
    
    return render_template('index.html', form=create_form)
    
    



if __name__ == '__main__':
    csrf.init_app(app)
    db.init_app(app)
    app.run(debug=True)