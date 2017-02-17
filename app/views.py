from flask import render_template, flash, redirect
from app import app, firebase, db, auth
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'fake user'}  # fake user
    posts = [  # fake array of posts
        {
            'author': {'nickname': 'name1'},
            'body': 'message1'
        },
        {
            'author': {'nickname': 'name2'},
            'body': 'message2'
        }
    ]
    return render_template("index.html",
                           title='Home',
                           user=user,
                           posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():

    form = LoginForm()
    if form.validate_on_submit():

        user = None
        try:
            user = auth.sign_in_with_email_and_password(form.email.data, form.password.data)
        except: pass

        if user is not None:
            flash('Login complete for email="%s", password=%s'
                % (form.email.data, str(form.password.data)))
        else:
            flash('Failure')
        return redirect('/index')
    return render_template('login.html',
                            title='Sign in',
                            form=form)