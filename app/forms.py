from flask_wtf import Form
from wtforms import TextField, PasswordField, validators
#from wtforms.validators import DataRequired

class LoginForm(Form):
    email = TextField('email')
    password = PasswordField('password')