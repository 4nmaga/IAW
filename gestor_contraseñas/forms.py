from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, IntegerField, BooleanField, SelectMultipleField, RadioField
from wtforms.validators import DataRequired, Email, Length


# Formulario de registro.

class Registro(FlaskForm):
    Nombre = StringField('Nombre de usuario:', validators=[DataRequired(), Length(max=45)])
    Email = StringField('Email:', validators=[DataRequired(), Email(), Length(max=45)])
    Password = PasswordField('Contraeña:', validators=[DataRequired(), Length(max=30)])
    submit = SubmitField('Registro')


# Formulario inicio sesion.

class Inicio_sesion(FlaskForm):
    Nombre = StringField('Nombre de usuario:', validators=[DataRequired(), Length(max=45)])
    Password = PasswordField('Contraeña:', validators=[DataRequired(), Length(max=30)])
    submit = SubmitField('Inicio')


# Formulario informacion usuario.

class KEY_VALUE(FlaskForm):

    Descripcion = StringField('Introduce una descripcion del servicio:', validators=[Length(max=120)])
    Usuario = StringField('Usuario de la cuenta:', validators=[DataRequired(), Email(), Length(max=45)])
    Password = PasswordField('Contraeña a guardar:', validators=[DataRequired(), Length(max=30)])
    submit = SubmitField('Guardar')
