<<<<<<< HEAD
from flask_wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class LoginForm(Form):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)
=======
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators
#from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    email = StringField('email', [validators.Email()])
    password = PasswordField('password')

class SignupForm(FlaskForm):
    firstname = StringField('First Name', [validators.Length(min=1, max=50)])
    lastname = StringField('Last Name', [validators.Length(min=1, max=50)])
    email = StringField('Email Address', [validators.Email()])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match'),
        validators.Length(min=6) # Firebase will complain otherwise
    ])
    confirm = PasswordField('Repeat Password')

>>>>>>> 9d7a5a5fc67db80d976357610eceb6c9f4d3b26e
