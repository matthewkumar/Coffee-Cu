from flask import render_template
from app import app

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