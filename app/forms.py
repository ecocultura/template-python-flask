from flask_wtf import FlaskForm #cada que se inicie hay que instalar --- pip install flask-wtf
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField("nombre del usuario", validators=[DataRequired()])
    password = PasswordField("contraseña", validators=[DataRequired()])
    submit = SubmitField("enviar datos", validators=[DataRequired()])