from flask import render_template, flash, redirect, session, url_for
from requests.exceptions import HTTPError
from app import app, firebase, db, auth
from .forms import LoginForm, SignupForm
from .decorators import logged_in, not_logged_in


@app.route('/')
@app.route('/index')
def index():
    user = None
    if 'idToken' in session:
        user = auth.get_account_info(session['idToken'])
        print("Found session for user.")

    return render_template("index.html", title='Home', user=user)

@app.route('/signup', methods=['GET', 'POST'])
@not_logged_in
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        user = None
        try:
            user = auth.create_user_with_email_and_password(form.email.data, form.password.data)
        except HTTPError: pass

        if user is not None:
            auth.send_email_verification(user['idToken'])
            # save details in the user data table
            userdata = { "firstname": form.firstname.data,
                        "lastname": form.lastname.data }
            db.child("users").push(userdata, user['idToken'])

            flash('Thanks for signing up!')
            return redirect(url_for('login'))
        else:
            # TODO this message may not be accurate
            flash('An account already exists for that email address!')
            return redirect(url_for('signup'))
    else:
        return render_template('signup.html', title='Sign up', form=form)


@app.route('/login', methods=['GET', 'POST'])
@not_logged_in
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # try to authenticate
        user = None
        try:
            user = auth.sign_in_with_email_and_password(form.email.data, form.password.data)
        except HTTPError: pass

        if user is not None:
            # if auth succeeds, see if email is verified
            accountInfo = auth.get_account_info(user['idToken'])

            if (not accountInfo['users'][0]['emailVerified']):
                flash('Please verify your email address!')
                return redirect(url_for('index'))
            else:
                # create new user session
                session['idToken'] = user['idToken']
                flash('Login complete for email="%s"' % (form.email.data))
        else:
            flash('Sorry, we couldn\'t find those credentials!')

        return redirect(url_for('index'))
    else:
        return render_template('login.html', title='Sign in', form=form)

@app.route('/logout')
@logged_in
def logout():
    session.pop('idToken', None) # end user session
    return redirect(url_for('index'))







