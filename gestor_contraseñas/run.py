from flask import Flask, render_template, request, redirect, url_for
from models import db, User, Service
from forms import Registro, KEY_VALUE, Inicio_sesion
import forms
import config
from flask_bootstrap import Bootstrap


app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)
Bootstrap(app)


# Menu de seleccion Registro--Inicio_sesion.
@app.route("/")
def inicio():
    return render_template("reg_inic.html")


# Registro usuario.
@app.route("/registro", methods=["GET", "POST"])
def registro_user():
    form = forms.Registro()
    if form.validate_on_submit():
        usuario = form.Nombre.data
        email = form.Email.data
        Password = form.Password.data
        user = User(Usuario=usuario, Email=email, Password=Password)
        user.set_Password(Password)
        user.save()

        return redirect(
            url_for("http://127.0.0.1:5000/inicio_sesion")
        )  # Redirigimos a inicio_sesion.

    return render_template("registro_user.html", form=form)


# Comprobar registro.(Aun no esta hecho)
@app.route("/inicio_sesion")
def sesion():
    return render_template("recop_datos.html")


# Servicios del usuario.
@app.route("/datos", methods=["GET", "POST"])
def datos():
    form = forms.KEY_VALUE()
    if form.validate_on_submit():
        usuario = form.Usuario.data
        descripcion = form.Descripcion.data
        Password = form.Password.data
        service = Service(User=usuario, Descripcion=descripcion, password=Password)
        service.set_Password(Password)
        service.save()

        return redirect(url_for("gestion"))

    return render_template("recop_datos.html", form=form)


with app.app_context():
    users = User.query.all()  # Obtener todos los usuarios.
    services = Service.query.all()  # Obtener todos los servicios.
    print(users)  # Imprimir en terminal los usuarios.
    print(services)  # Imprimir en terminal los servicios.


if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Creamos las tablas si no estan creadas.
        db.session.commit()  # Guardamos los cambios realizados.
    app.run(debug=True)
