from flask import render_template, flash, redirect
from app import app
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
        flash('Login requested for ID="%s", remember_me=%s' %
              (form.id.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html',
                            title='Sign in',
                            form=form)