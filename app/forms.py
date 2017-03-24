from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators, Form, TextField, TextAreaField, SubmitField
#from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    email = StringField('email', [validators.Email()])
    password = PasswordField('password')

class SignupForm(FlaskForm):
    firstname = StringField('First Name', [validators.Length(min=1, max=50)])
    lastname = StringField('Last Name', [validators.Length(min=1, max=50)])
    email = StringField('Email Address', [validators.Email(), validators.Regexp(r'.+(columbia|barnard)\.edu$', message="Please fill in a Columbia-affiliated email")])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match'),
        validators.Length(min=6) # Firebase will complain otherwise
    ])
    confirm = PasswordField('Repeat Password')

class ContactForm(Form):
  message = TextAreaField("Message",  [validators.Required("Please enter a message.")])
  submit = SubmitField("Send")