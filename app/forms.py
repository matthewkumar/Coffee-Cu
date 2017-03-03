from flask_wtf import FlaskForm
from wtforms import validators, StringField, PasswordField, SelectField, TextAreaField, FileField, BooleanField
from app import majors

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


class ProfileForm(FlaskForm):
    # uni
    #image = FileField('Profile picture', [validators.regexp(u'^[^/\\]\.jpg$')])
    school = SelectField('School', choices=[
            ('cc', 'Columbia College'),
            ('seas', 'Columbia Engineering'),
            ('barnard', 'Barnard College'),
            ('gs', 'General Studies')
        ])
    year = SelectField('Year', choices=[
            ('2017', '2017'),
            ('2018', '2018'),
            ('2019', '2019'),
            ('2020', '2020')
        ])
    major = SelectField('Major', choices=[(key, majors[key]) for key in majors])
    about = TextAreaField('Tell the world a little bit more about yourself', [validators.Length(max=400)])
    likes = TextAreaField('What do you like?', [validators.Length(max=150)])
    contactfor = TextAreaField('What are some things people should contact you for?', [validators.Length(max=250)])
    twitter = StringField('Twitter')
    facebook = StringField('Facebook')
    linkedin = StringField('LinkedIn')
    website = StringField('Website')
    make_public = BooleanField('Make your profile public to the world?')

    #def validate_image(form, field):
